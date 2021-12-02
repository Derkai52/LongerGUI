import sys
from communication.hub import Hub
from config import *
import configparser


# TODO:主函数收录日志处理
# def logs.logger.info(msg):
#     print("[", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "]: Client ::", msg)

def read_config(config_path):
    conf = configparser.ConfigParser()
    conf.read(config_path, encoding="utf-8")
    server_ip = conf.get("CommunicationConfig", "mech_interface_ip")
    server_port = conf.get("CommunicationConfig", "mech_interface_port")
    connect_ip = conf.get("CommunicationConfig", "robot_server_agent_ip")
    connect_port = conf.get("CommunicationConfig", "robot_server_agent_port")
    return server_ip, server_port, connect_ip, connect_port



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")  # 初始化日志设置:等级：INFO，内容：【时间+消息】
    mech_interface_ip, mech_interface_port, robot_server_agent_ip, robot_server_agent_port = read_config(config_path="config.cfg") # 读取配置文件 # TODO:warning: 注意读取出来的是完整的值,并且统一为字符串
    print(mech_interface_ip)
    if True:
        client =Hub(serverIP=mech_interface_ip, serverPort=mech_interface_port,\
                    connectIP=robot_server_agent_ip, connectPort=robot_server_agent_port)
        client.run()
    else:
        print("Please input config.cfg path or connect information")
        print("Client configPath")
        print("Client serverIP serverPort connectIP connectPort")



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
#         print("Please input config.cfg path or connect information")
#         print("Client configPath")
#         print("Client serverIP serverPort connectIP connectPort")
