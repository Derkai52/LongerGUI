import sys
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
        self.robotServer = None    # 用于连接机器人端【用于通信的套接字】(本地作为服务端)
        self.listenRobot = None    # 用于连接机器人端【用于监听和接受客户端的连接请求的套接字】(本地作为服务端)
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
    #     if self.listenRobot is not None:
    #         self.listenRobot.shutdown(socket.SHUT_WR)
    #         self.listenRobot.close()


    def check_detection(self):
        """
        doc:校验检测
        return: 校验成功:True 校验失败:False
        """
        response = self.client.recv()
        logs.debug("从Mech返回的连接校验值：{}".format(response))
        # 仅返回消息为 “ACC” 时，建立连接
        if response.decode("utf-8") == '"' + "ACC" + '"':  # Warning:接受的字符串包括引号需要进行处理,所以此处才这么写
            return True
        return False


    def send_to_mech(self):
        """
        发送信息给Mech
        """
        while True:
            # sendMsg = bytes(input("\n请输入向Mech发送的消息:"), encoding="UTF8") # 仅供调试用
            # self.client.send(sendMsg)
            if self.is_connect_mech:
                sendMsg = input("\n请输入向Mech发送的消息: 例如101,1,1,1,-490.000,0,539.000,-90.000,90.000,180.000") # TODO: 预留给前端界面的输入接口
            else:
                sendMsg = "901" # 用于检查Mech准备状态
            msg_process(self.client, sendMsg, funcFlag = 1) # 信息处理并发送


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


    def thread_connect_robot(self):
        """
        doc:开启线程维持对Robot的连接
        """
        thread_3 = threading.Thread(target=self.connect_robot) # 连接机器人
        thread_3.setDaemon(True)
        thread_3.start()


    def connect_mech(self):
        """
        doc: 判断连接Mech标准接口是否成功，成功则开启一个后台线程用于
        return: 连接成功: True 连接失败: False
        """
        logs.debug("正在连接Mech服务器: %s %s" % (self.serverIP, self.serverPort))

        self.client.reconnect_server() # 尝试重新连接到Mech
        if self.client.is_connected(): # 如果连接成功
            logs.info("请求Mech服务器成功，正在校验连接...")
            # if self.check_detection(): # TODO:进行与Mech通讯的校验检测，当前暂未启用
            if True: # 未启用校验检测，校验返回值一定为True
                self.thread_connect_mech()  # 开启一个线程连接到Mech
                return True
            else:
                logs.error("与Mech服务器连接校验失败!")
                self.client.close()
        return False


    def run(self):
        """
        doc:持续循环检测与Mech的连接状态，可断线重连。
        """
        while True:
            if self.client.is_connected():              # 如果已经连接到Mech
                pass

            else:                                       # 如果未连接到Mech
                self.listenRobot = None                 # 强制关闭Robot接口监听套接字
                self.robotServer = None                 # 强制关闭Robot接口通讯套接字
                logs.debug("正在尝试重新连接到Mech: %s %s" % (self.serverIP, self.serverPort))
                if not self.connect_mech():             # 尝试连接Mech服务器
                    continue
            # time.sleep(10) # 固定检测周期


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


        self.listenRobot = self.robotServer
        logs.info("连接机器人成功! 机器人套接字信息已获取，为:{}, 机器人IP信息为:{}".format(self.listenRobot._client_connect, self.listenRobot._remote_addr)) # TODO:得想个更好的办法拿到机器人的套接字信息
        while True:
            response = self.listenRobot.recv()
            logs.debug("从机器人端收到的消息为: {}".format(response))
            # time.sleep(10)
            if response == b'':
                logs.info("关闭对机器人的连接")
                self.robotServer.close()
                self.listenRobot.close()
                self.listenRobot = None
                break
            self.client.send(response)
            logs.debug("转发给Mech的信息: {}".format(response))


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

        elif response == jk.CheckCodeMsg:  # 连接验证码通过
            logs.info("连接验证通过")
            # logs.info("正在连接机器人...")
            # if self.listenRobot is None:
            #     self.thread_connect_robot()  # 开启一个线程连接机器人
            return 2

        elif response == jk.CloseMsg: # 接受到关闭信号
            logs.warning("接收到关闭信号，将关闭socket连接")
            if self.listenRobot is not None:
                self.listenRobot.close()
                self.listenRobot = None
            return 2

        return 1


    def client_process(self):
        """
        doc: 将Mech信息转发给机器人
        """
        while True:
            if not self.client.is_connected(): # 如果连接丢失
                break

            # 1、从Mech获取消息
            recv_mech_msg = self.client.recv()

            # 3、通讯事件处理
            response = msg_process(self.client,recv_mech_msg, funcFlag=2) # 阻塞接收来自 Mech 的消息，例如b'101,1001,'# TODO:使用多线程技术完成全双工通信机制


            # 2、Mech通讯状态检测
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
            if self.listenRobot is None:
                logs.warning("当前没有检测到与机器人连接!正在尝试重连...")# TODO: 应当找个更合适安全的地方开启这个线程，比如保证与mech的通讯无误(比如拍个照并返回结果)
                self.thread_connect_robot()  # 开启一个线程连接机器人
                continue
            else:
                try:
                    self.listenRobot.send(response)
                    logs.debug("发送给机器人: {}".format(response))
                except Exception as e:
                    print(e)