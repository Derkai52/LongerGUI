"""
Config 配置文件模板(此备份用于重置还原配置)
"""


# 软件设置模板
softWareConfig_Template = """
# 配置文件写入说明:注释务必单独列行
# 【软件设置】
[SoftWareConfig]
software_name = LongerGUI
software_version = V0.1.1-alpha
project_name = default_template
project_version = 1
project_config_path = .
"""

# 通讯设置模板
CommunicationConfig_Template = """
# 【通信设置】
[CommunicationConfig]
# Mech Interface IP
mech_interface_ip = 127.0.0.1
# Mech Interface 端口号
mech_interface_port = 50000
# 连接机器人网口的IP
robot_server_agent_ip = 192.168.3.200
# 连接机器人网口的端口号
robot_server_agent_port = 3000
# 机器人设备商名称
robot_vendor = ABB
# robot_ip ==  # 机器人IP
# robot_port == 50 # 机器人端口号

# 是否为 ASCII 码
is_ascii = True
# Hex 格式用大端还是小端
endian = <
# 客户端发送给 Mech-Interface 的命令长度(bytes)
len_client_msg = 56
# Mech-Interface 发送给客户端的命令长度(bytes)
len_mech_msg = 660
# 数据接收默认长度(字节)
default_len_data = 1024
"""

# 日志设置模板
LogConfig_Template = """
# 【日志设置】
[LogConfig]
# 日志保存文件夹(路径相对于项目根目录)
log_save_path = logs
# 日志采集最低等级
log_save_level = info
# 备份文件的最大个数
log_backCount = 3
# log_when = "D" # 时间记录间隔
# 日志记录格式
log_format = '%(asctime)s - %(levelname)s: %(message)s'
#'%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
"""