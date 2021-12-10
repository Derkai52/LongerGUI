import configparser
import os

"""
    Config 配置文件表
"""
SOFTWARE_NAME            = "software_name"
SOFTWARE_VERSION         = "software_version"
PROJECT_NAME             = "project_name"
PROHECT_VERSION          = "project_version"

MECH_INTERFACE_IP        = "mech_interface_ip"
MECH_INTERFACE_PORT      = "mech_interface_port"
ROBOT_SERVER_AGENT_IP    = "robot_server_agent_ip"
ROBOT_SERVER_AGENT_PORT  = "robot_server_agent_port"
ROBOT_VENDOR             = "robot_vendor"
IS_ASCII                 = "is_ascii"
ENDIAN                   = "endian"
LEN_CLIENT_MSG           = "len_client_msg"
LEN_MACH_MSG             = "len_mech_msg"
DEFAULT_LEN_DATA         = "default_len_data"

LOG_SAVE_PATH            = "log_save_path"
LOG_SAVE_LEVEL           = "log_save_level"
LOG_BACKCOUNT            = "log_backCount"
LOG_FORMAT               = "log_format"



class Config():
    def __init__(self, config_path, encodings="utf-8"): # TODO： 注意这里给了一个路径默认值，需要优化为从根目录读取
        self.conf = None # 配置文件句柄
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path, encoding=encodings) # TODO: 不确定这种只初始化一次的写法对于配置文件更新是否有作用

    def read_config_dict(self):
        """
        doc: 用于读取配置变量值
        :return: 包含配置参数的字典 Key:配置变量名称 Value:值
        """
        return {
            SOFTWARE_NAME: self.conf.get("SoftWareConfig", "software_name"),
            SOFTWARE_VERSION: self.conf.get("SoftWareConfig", "software_version"),
            PROJECT_NAME: self.conf.get("SoftWareConfig", "project_name"),
            PROHECT_VERSION: self.conf.get("SoftWareConfig", "project_version"),
            MECH_INTERFACE_IP: self.conf.get("CommunicationConfig", "mech_interface_ip"),
            MECH_INTERFACE_PORT: self.conf.get("CommunicationConfig", "mech_interface_port"),
            ROBOT_SERVER_AGENT_IP: self.conf.get("CommunicationConfig", "robot_server_agent_ip"),
            ROBOT_SERVER_AGENT_PORT: self.conf.get("CommunicationConfig", "robot_server_agent_port"),
            ROBOT_VENDOR: self.conf.get("CommunicationConfig","robot_vendor"),
            IS_ASCII: self.conf.get("CommunicationConfig","is_ascii"),
            ENDIAN: self.conf.get("CommunicationConfig","endian"),
            LEN_CLIENT_MSG: self.conf.get("CommunicationConfig","len_client_msg"),
            LEN_MACH_MSG: self.conf.get("CommunicationConfig","len_mech_msg"),
            DEFAULT_LEN_DATA: self.conf.get("CommunicationConfig","default_len_data"),
            LOG_SAVE_PATH: self.conf.get("LogConfig","log_save_path"),
            LOG_SAVE_LEVEL: self.conf.get("LogConfig","log_save_level"),
            LOG_BACKCOUNT: self.conf.get("LogConfig","log_backCount"),
            LOG_FORMAT: self.conf.get("LogConfig","log_format", raw=True), # TODO: 添加至开发手册： 若需要格式化的，需要加上第二个参数
        }

    def set_config_dict(self):
        """
        doc: 设置配置变量值
        :return:
        """
        pass

config_dir = os.path.join(os.path.dirname(__file__), "..", "config.cfg") # 读取配置文件路径(以本文件所在目录为起始点)
print(config_dir, type(config_dir))
configs = Config(config_dir) # 配置类实例化用于其他py文件快速读取

