import sys
from communication.hub import Hub
from config import *
import configparser


# TODO:主函数收录日志处理
# def logs.logger.info(msg):
#     print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]: Client ::", msg)

def read_config(config_path):
    conf = configparser.ConfigParser()
    conf.read(config_path)
    server_ip = conf.get("Client", "ServerIP")
    server_port = conf.get("Client", "ServerPort")
    connect_ip = conf.get("Client", "ConnectIP")
    connect_port = conf.get("Client", "ConnectPort")
    return server_ip, server_port, connect_ip, connect_port



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")  # 初始化日志设置:等级：INFO，内容：【时间+消息】

    # if True:
    #     client =Hub(serverIP=mech_interface_ip, serverPort=mech_interface_port,\
    #                 connectIP=robot_server_agent_ip, connectPort=robot_server_agent_port)
    #     client.run()
    # else:
    #     print("Please input config path or connect information")
    #     print("Client configPath")
    #     print("Client serverIP serverPort connectIP connectPort")

    print(read_config(config_path="config")) # 读取配置文件


#
# print(sys.argv[1])
#     if len(sys.argv) == 2: # 从文件读取
#         config_path = sys.argv[1]
#         client = Hub(configPath=config_path)
#         client.run()
#     elif len(sys.argv) == 5: # 输入外参
#         client = Hub(serverIP=sys.argv[1], serverPort=sys.argv[2], connectIP=sys.argv[3], connectPort=sys.argv[4])
#         client.run()
#     else:
#         print("Please input config path or connect information")
#         print("Client configPath")
#         print("Client serverIP serverPort connectIP connectPort")
