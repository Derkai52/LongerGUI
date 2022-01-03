import sys, time
import threading
import configparser
from communite import TcpServer, TcpClient
from event.parse_event import msg_process
from util.log_tool.log import logs
from util import json_keys as jk
from util.generator import configObject


class Hub:
    """
    doc:作为信息中转分发的类
    """
    def __init__(self, serverIP="", serverPort="", connectIP="", connectPort=""):
        self.client = None         # 用于连接 Mech 服务器(本地作为客户端)
        self.robotServer = None    # 用于连接机器人端(本地作为服务端)
        self.is_connect_robot = False # 判断是否连接到机器人端

        self.serverIP = serverIP
        self.serverPort = serverPort
        self.connectIP = connectIP
        self.connectPort = connectPort
        self.mechAddr = self.serverIP + ":" + self.serverPort  # 生成Mech地址+端口
        self.robotAddr = self.connectIP + ":" + self.connectPort # 生成Robot地址+端口
        self.client = TcpClient(self.mechAddr) # 初始化client



# TODO: shutdown是一种更加优秀的socket生命周期管理方法
    # def __del__(self):
    #     self.client.shutdown(socket.SHUT_WR)
    #     self.client.close()
    #     if self.robotServer is not None:
    #         self.robotServer.shutdown(socket.SHUT_WR)
    #         self.robotServer.close()
    def run(self):
        """
        doc:持续循环检测与Mech的连接状态，可断线重连。
        """
        while True:
            time.sleep(2) # 固定检测周期(可能会导致进程间状态不同步)

            if self.client.is_connected():              # 如果已经连接到Mech
                pass

            else:                                       # 如果未连接到Mech
                self.robotServer = None                 # 强制关闭Robot接口监听套接字
                self.robotServer = None                 # 强制关闭Robot接口通讯套接字
                logs.debug("正在尝试重新连接到Mech: %s %s" % (self.serverIP, self.serverPort))
                if not self.connect_mech():             # 尝试连接Mech服务器
                    continue


    def check_detection(self):
        """
        doc:校验检测,用于检查Mech准备状态
        return: 校验成功:True 校验失败:False
        """

        try:
            self.client.send(bytes("901", encoding="UTF8"))
            response = self.client.recv()
            logs.debug("从Mech返回的连接校验值：{}".format(response))

            # 仅返回消息也符合Standrad-InterFace协议报文 “901” 时，建立连接
            if response.decode("utf-8").split(",")[0] == "901":  # Warning: 目前的校验值可能会随着Mech版本变更而失效
                self.thread_connect_robot()  # 开启一个线程提供机器人接口
                return True
            return False
        except Exception:
            logs.error("校验检测错误，请检查通讯或校验码是否有效！")
            return False


    def connect_mech(self):
        """
        doc: 判断连接Mech标准接口是否成功，成功则开启一个后台线程用于
        return: 连接成功: True 连接失败: False
        """
        logs.debug("正在连接Mech服务器: %s %s" % (self.serverIP, self.serverPort))

        self.client.reconnect_server() # 尝试重新连接到Mech
        if self.client.is_connected():
            logs.info("请求Mech服务器成功，正在校验连接...")
            if self.check_detection(): # 连接校验
                self.thread_connect_mech()  # 开启一个线程连接到Mech
                return True
            else:
                logs.error("与Mech服务器连接校验失败!")
                self.client.close()
        return False


    def thread_connect_mech(self):
        """
        doc:开启线程维持对Mech的连接
        """
        thread_1 = threading.Thread(target=self.client_process)  # 监听Mech的通信
        thread_1.setDaemon(True)  # 挂后台进程
        thread_1.start()
        logs.info("连接Mech成功!【监听】")

        thread_2 = threading.Thread(target=self.send_to_mech) # 发送Mech的通信
        thread_2.setDaemon(True)
        thread_2.start()
        logs.debug("连接Mech成功!【发送】")


    def client_process(self):
        """
        doc: 将Mech信息转发给机器人
        """
        while True:

            # 1、从Mech获取消息
            try:
                if not self.client.is_connected():  # 如果连接丢失
                    break
                recv_mech_msg = self.client.recv()

            except Exception as e:
                self.client.close()
                logs.warning("与Mech的连接中断")
                return

            # 2、通讯事件处理
            response = msg_process(self.client,recv_mech_msg, funcFlag=2) # 阻塞接收来自 Mech 的消息，例如b'101,1001,'# TODO:使用多线程技术完成全双工通信机制


            # 3、Mech通讯状态检测
            processResult = self.mech_status_process(response)
            if processResult == 1: # 普通信息，直接放行
                pass
            elif processResult == 2: # 心跳检测、正常关闭、连接验证通过
                continue
            elif processResult == 3: # 丢失连接
                break
            else:
                logs.error("检测到BUG【可能是未经收录的连接状态】")
                break

            logs.debug("从Mech获得的消息: {}".format(response))



            # 4、将消息转发给机器人
            if self.robotServer is None:
                logs.warning("当前没有检测到与机器人连接!正在尝试重连...")# TODO: 应当找个更合适安全的地方开启这个线程，比如保证与mech的通讯无误(比如拍个照并返回结果)
                self.thread_connect_robot()  # 开启一个线程连接机器人
                continue
            else:
                try:
                    self.robotServer.send(response)
                    logs.debug("发送给机器人: {}".format(response))
                except Exception as e:
                    print(e)


    def mech_status_process(self, response):
        """
        doc: 与Mech的通讯状态检测
        retrun: 直接放行:1 continue:2 break:3
        """

        if response == jk.LostConnectMsg:  # 丢失连接或通讯异常
            logs.warning("丢失与Mech服务器的连接")
            self.client.close()
            self.client = None
            return 3

        elif response == jk.FormatErrorMsg:  # 消息格式错误
            logs.warning("请检查与Mech通讯信息格式是否符合要求")
            return 2

        elif response == jk.HeartbeatMsg:  # 心跳检测
            logs.debug("心跳检测")
            return 2


        elif response == jk.CloseMsg: # 接受到关闭信号
            logs.warning("接收到关闭信号，将关闭socket连接")
            if self.robotServer is not None:
                self.robotServer.close()
                self.robotServer = None
            return 2

        return 1


    def send_to_mech(self):
        """
        发送信息给Mech
        """
        while True:
            # sendMsg = bytes(input("\n请输入向Mech发送的消息:"), encoding="UTF8") # 仅供调试用
            # self.client.send(sendMsg)
            if self.client.is_connected():
                sendMsg = input("\n请输入向Mech发送的消息: 例如101,1,1,1,-490.000,0,539.000,-90.000,90.000,180.000") # TODO: 预留给前端界面的输入接口
                msg_process(self.client, sendMsg, funcFlag = 1) # 信息处理并发送


    def thread_connect_robot(self):
        """
        doc:开启线程维持对Robot的连接
        """
        thread_3 = threading.Thread(target=self.connect_robot) # 开启机器人接口
        thread_3.setDaemon(True)
        thread_3.start()


    def connect_robot(self):
        """
        doc: 判断连接Mech标准接口是否成功
        return: 连接成功: True 连接失败: False
        """
        # 1、开启Robot接口服务器
        try:
            logs.debug("机器人接口信息:{}".format(self.robotAddr))
            self.robotServer = TcpServer(self.robotAddr) # 不确定是否在此初始化还是伴随Mech初始化后就初始化
        except Exception as e:
            logs.error("网口未能正常启动{}".format(e))
            return
        self.robotServer.accept() # Warning:默认设置的是最大仅允许1个套接字接入(.listen(1))

        logs.info("机器人连接成功! 机器人套接字信息已获取，为:{}, 机器人IP信息为:{}".format(self.robotServer._client_connect, self.robotServer._remote_addr)) # TODO:得想个更好的办法拿到机器人的套接字信息
        while True:
            response = self.robotServer.recv()
            logs.debug("从机器人端收到的消息为: {}".format(response))

            if response == jk.LostConnectMsg:
                logs.info("关闭对机器人接口")
                self.robotServer.close()
                self.robotServer = None
                break
            self.client.send(response)
            logs.debug("转发给Mech的信息: {}".format(response))