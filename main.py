import sys
from communication.hub import Hub
from util.log.log import readConfig

if __name__ == "__main__":
    mech_interface_ip = readConfig["mech_interface_ip"]
    mech_interface_port = readConfig["mech_interface_port"]
    robot_server_agent_ip = readConfig["robot_server_agent_ip"]
    robot_server_agent_port = readConfig["robot_server_agent_port"]
    if True:
        client =Hub(serverIP=mech_interface_ip, serverPort=mech_interface_port,\
                    connectIP=robot_server_agent_ip, connectPort=robot_server_agent_port)
        client.run()
    else:
        print("Please input config.cfg path or connect information")
        print("Client configPath")
        print("Client serverIP serverPort connectIP connectPort")



# 预留接口，直接使用参数启动程序(已停止维护)
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
