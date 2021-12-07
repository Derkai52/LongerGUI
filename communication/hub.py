import sys
import threading
import configparser
from communite import TcpServer, TcpClient
from event.parse_event import msg_process
from util.log import logs, readConfig


# 从文件读取
# def read_config(config_path):
#     conf = configparser.ConfigParser()
#     conf.read(config_path)
#     server_ip = conf.get("CommunicationConfig", "mech_interface_ip")
#     server_port = conf.get("CommunicationConfig", "mech_interface_port")
#     connect_ip = conf.get("CommunicationConfig", "robot_server_agent_ip")
#     connect_port = conf.get("CommunicationConfig", "robot_server_agent_port")
#     return server_ip, server_port, connect_ip, connect_port


class Hub:
    """
    doc:作为信息中转分发的类
    """
    def __init__(self, configPath="", serverIP="", serverPort="", connectIP="", connectPort=""):
        self.client = None         # 用于连接 Mech 服务器(本地作为客户端)
        self.listenRobot = None    # 用于连接机器人端【用于监听和接受客户端的连接请求的套接字】(本地作为服务端)
        self.toRobot = None        # 用于连接机器人端【用于通信的套接字】(本地作为服务端)
        self.msgflag = None        # 用于标识信息类型【发送的消息:1  接收的消息:2】

        if configPath == "":
            self.serverIP = serverIP
            self.serverPort = serverPort
            self.connectIP = connectIP
            self.connectPort = connectPort
            self.mechAddr = self.serverIP + ":" + self.serverPort  # 生成Mech地址+端口
            self.robotAddr = self.connectIP + ":" + self.connectPort # 生成Robot地址+端口
            self.client = TcpClient(self.mechAddr) # 初始化client
        else:
            self.serverIP, self.serverPort, self.connect_ip, self.connect_port = \
                readConfig["mech_interface_ip"],readConfig["mech_interface_port"],\
                readConfig["robot_server_agent_ip"],readConfig["robot_server_agent_port"]
            # TODO: 使用文件读取生成TcpClient

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
        logs.logger.info("从Mech返回的连接校验值：{}".format(response))
        # 仅返回消息为 “ACC” 时，建立连接
        if response.decode("utf-8") == '"' + "ACC" + '"':  # TODO: Warn:接受的字符串包括引号需要进行处理
            return True
        return False

    def send_to_mech(self):
        """
        发送信息给Mech
        """
        while True:
            # sendMsg = bytes(input("\n请输入向Mech发送的消息:"), encoding="UTF8")
            sendMsg = input("\n请输入向Mech发送的消息: 例如101,1,1,1,-490.000,0,539.000,-90.000,90.000,180.000") # TODO: 预留给前端界面的输入接口

            self.msgflag = 1 # TODO:可以用更好的方法解决，提高代码易读性和维护性
            msg_process(self.client, self.msgflag, sendMsg) # 信息处理并发送 # TODO: flag标识是处理发送信息还是接受信息
            self.msgflag = None

            # self.client.send(sendMsg)


    def thread_connect_mech(self):
        """
        doc:开启线程维持对Mech的连接
        """
        thread_1 = threading.Thread(target=self.client_process)  # 监听Mech的通信
        thread_1.setDaemon(True)  # 挂后台进程
        thread_1.start()
        logs.logger.info("连接Mech成功!【监听】")

        thread_2 = threading.Thread(target=self.send_to_mech) # 发送Mech的通信
        thread_2.setDaemon(True)
        thread_2.start()
        logs.logger.info("连接Mech成功!【发送】")


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
        logs.logger.info("正在连接Mech服务器: %s %s" % (self.serverIP, self.serverPort))
        self.client.reconnect_server() # 尝试重新连接到Mech
        if self.client.is_connected(): # 如果连接成功
            logs.logger.info("请求Mech服务器成功，正在校验连接...")
            # if self.check_detection(): # TODO:连接校验码检测
            if True:
                self.thread_connect_mech()  # 开启一个线程连接到Mech
                return True
            else:
                logs.logger.info("与Mech服务器连接校验失败!")
        return False

    def run(self):
        """
        doc:持续循环检测与Mech的连接状态，可断线重连。
        """
        while True:
            if self.client.is_connected():              # 如果已经连接到Mech
                pass
                # time.sleep(30) # 检测到已连接后的检测周期
                # logs.logger.info("已连接到服务端")
            else:                                       # 如果未连接到Mech
                logs.logger.info("正在尝试重新连接到Mech: %s %s" % (self.serverIP, self.serverPort))
                self.connect_mech() # 尝试连接Mech服务器
            # time.sleep(10) # 固定检测周期

    def connect_robot(self):
        """
        doc: 判断连接Mech标准接口是否成功
        return: 连接成功: True 连接失败: False
        """
        a = TcpServer(self.robotAddr) # TODO: 不确定是否在此初始化还是伴随Mech初始化后就初始化
        a.accept() # TODO: Warning:默认设置的是最大仅允许1个套接字接入(.listen(1))
        self.listenRobot = a
        logs.logger.info("连接机器人成功! 机器人套接字信息已获取，为:{}, 机器人IP信息为:{}".format(self.listenRobot._client_connect, self.listenRobot._remote_addr)) # TODO:得想个更好的办法拿到机器人的套接字信息
        while True:
            response = self.listenRobot.recv()
            logs.logger.info("从机器人端收到的消息为: {}".format(response))
            # time.sleep(10)
            if response == b'':
                logs.logger.info("关闭对机器人的连接")
                self.listenRobot.close()
                self.listenRobot = None
                break
            self.client.send(response)
            logs.logger.info("转发给Mech的信息: {}".format(response))

    def event_mech_process(self, response):
        """
        doc: 处理来自mech的消息事件
        retrun: 直接放行:1 continue:2 break:3
        """
        if response == b'':  # 丢失连接
            logs.logger.info("丢失与Mech服务器的连接")
            self.client.close()
            self.client = None
            return 3

        elif response == b"Heartbeat":  # 心跳检测
            return 2

        elif response == b"#CONNECT":  # 连接验证码通过
            # logs.logger.info("正在连接机器人...")
            # if self.listenRobot is None:
            #     self.thread_connect_robot()  # 开启一个线程连接机器人
            return 2

        elif response == b'#CLOSE': # 接受到关闭信号
            logs.logger.info("接收到关闭信号，将关闭socket连接")
            if self.listenRobot is not None:
                self.listenRobot.close()
                self.listenRobot = None
            return 2

        return 1


    def client_process(self):
        """
        doc: Mech与机器人消息的中转站
        """
        while True:
            if not self.client.is_connected(): # 如果连接丢失
                break
            # response = self.client.recv()
            self.msgflag = 2
            response = msg_process(self.client, self.msgflag) # 接收来自 Mech 的消息
            self.msgflag = None
            # logs.logger.info("从Mech获得的消息: {}".format(response))

            processResult = self.event_mech_process(response) # Mech消息事件处理
            if processResult == 1: # 普通信息，直接放行
                pass
            elif processResult == 2: # 心跳检测、正常关闭、连接验证通过
                continue
            elif processResult == 3: # 丢失连接
                break
            else: logs.logger.info("检测到BUG【可能是未经收录的事件】")



            if self.listenRobot is None:
                logs.logger.info("正在连接机器人...")  # TODO: 应当找个更合适安全的地方开启这个线程，比如保证与mech的通讯无误(比如拍个照并返回结果)
                if self.listenRobot is None:
                    self.thread_connect_robot()  # 开启一个线程连接机器人
                logs.logger.info("当前没有检测到与机器人连接!")
                continue
            else:
                try:
                    self.listenRobot.send(response)
                    logs.logger.info("发送给机器人: {}".format(response))
                except Exception as e:
                    print(e)