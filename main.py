from communication.communication import TcpServer, TcpClient, HttpServer, Communication
from util.format_adapter import format_hex_bytes, check_ascii_character
import logging

# 通信部分
ip_address = "127.0.0.1"
intelface_ip_port = "50000" # 标准接口端口
robotsev_port = "50002" # RobotSev接口端口
ip_path = ip_address + ":" + intelface_ip_port
is_reconnect = False
msg = ""

# 日志部分
log_path = r'./logs/all.log'
lgo_level = 'debug'

# logr = Logger(log_path, level=lgo_level)
# Logger(r'./logs/error.logr', level='error').logger.error('error')
# TODO: 使用可继承的父子logger以提高日志模块化
# TODO: Warning: 日志事件时间记录以系统时间为准，可能是一个隐患
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s") # 初始化日志设置:等级：INFO，内容：【时间+消息】




# TODO:所有print显示部分仅供调试用，后期用日志替代
a = TcpClient(ip_path)
while True:
    if not a.is_connected(): # 如果未连接到服务器，尝试连接
        a.reconnect_server(is_reconnect)
        is_reconnect = True  # 仅初次连接服务器为 False
        logging.info("正在尝试重新连接,Attempting to reconnect...")
        continue
    else: # 已连接到服务器
        logging.info("连接成功,Connection succeeded!")
        msg = a.recv() # 监听数据

        if len(msg) == 0: # TODO:通常这种情况是与服务器断开连接的表现(接受长度为0)，普适性有待测试验证。
            a.close()
            continue
        elif len(msg) > 1:
                ## TODO: 消息可用性校验
            # if check_ascii_character(msg): # 对消息进行校验（适配QT窗口的LineText类型输入）
            logging.info("recv:{}".format(msg))
                # TODO: parse_event() 用于消息事件处理
            # else:
            #     print("消息内容无法处理")

        msg = bytes('Hello','utf-8')
        # msg = format_hex_bytes(msg)
        a.send(msg)
