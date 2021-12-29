import configparser
import os
import logging # TODO: 无法导入log中的日志模块，因为这会形成一个import死循环，暂时直接用logging代替
from util.util_file import write_file
from config_tool.config_template import * # 获取配置文件模板


"""
    Config 配置文件表
"""
############### 软件设置 #############################
SOFTWARE_NAME            = "software_name"
SOFTWARE_VERSION         = "software_version"
PROJECT_NAME             = "project_name"
PROHECT_VERSION          = "project_version"
THIRD_PARTY_EQUIPMENT    = "third_party_equipment"

############### 通讯设置 ##############################
MECH_INTERFACE_IP        = "mech_interface_ip"
MECH_INTERFACE_PORT      = "mech_interface_port"
ROBOT_SERVER_AGENT_IP    = "robot_server_agent_ip"
ROBOT_SERVER_AGENT_PORT  = "robot_server_agent_port"
ROBOT_VENDOR             = "robot_vendor"
COMMUNITE_FORMAT         = "communite_format"
IS_ASCII                 = "is_ascii"
ENDIAN                   = "endian"
LEN_CLIENT_MSG           = "len_client_msg"
LEN_MACH_MSG             = "len_mech_msg"
DEFAULT_LEN_DATA         = "default_len_data"

################ 日志设置 ############################
LOG_SAVE_PATH            = "log_save_path"
LOG_SAVE_LEVEL           = "log_save_level"
LOG_BACKCOUNT            = "log_backCount"
LOG_FORMAT               = "log_format"

################ 展示性设置 ##########################


################ 其他设置 ############################
UPDATE_DOC_NAME          = "update_doc_name"


class Config():
    def __init__(self, config_path, encodings="utf-8"): # TODO： 注意这里给了一个路径默认值，需要优化为从根目录读取
        self.conf = None # 配置文件句柄
        self.conf = configparser.ConfigParser()
        self.conf_dir = config_path # 配置文件路径
        self.conf.read(self.conf_dir, encoding=encodings) # TODO: 不确定这种只初始化一次的写法对于配置文件更新是否有作用


    def read_config_dict(self):
        """
        doc: 用于读取配置变量值
        :return: 包含配置参数的字典 Key:配置变量名称 Value:值
        """
        return {
            SOFTWARE_NAME: self.conf.get("SoftWareConfig", "software_name"),
            SOFTWARE_VERSION: self.conf.get("SoftWareConfig", "software_version"),
            PROJECT_NAME: self.conf.get("SoftWareConfig", "project_name"),
            PROHECT_VERSION: self.conf.getint("SoftWareConfig", "project_version"),
            THIRD_PARTY_EQUIPMENT: self.conf.getboolean("SoftWareConfig", "third_party_equipment"),
            MECH_INTERFACE_IP: self.conf.get("CommunicationConfig", "mech_interface_ip"),
            MECH_INTERFACE_PORT: self.conf.get("CommunicationConfig", "mech_interface_port"),
            ROBOT_SERVER_AGENT_IP: self.conf.get("CommunicationConfig", "robot_server_agent_ip"),
            ROBOT_SERVER_AGENT_PORT: self.conf.get("CommunicationConfig", "robot_server_agent_port"),
            ROBOT_VENDOR: self.conf.get("CommunicationConfig","robot_vendor"),
            COMMUNITE_FORMAT: self.conf.get("CommunicationConfig", "communite_format"),
            IS_ASCII: self.conf.getboolean("CommunicationConfig","is_ascii"),
            ENDIAN: self.conf.get("CommunicationConfig","endian"),
            LEN_CLIENT_MSG: self.conf.get("CommunicationConfig","len_client_msg"),
            LEN_MACH_MSG: self.conf.get("CommunicationConfig","len_mech_msg"),
            DEFAULT_LEN_DATA: self.conf.get("CommunicationConfig","default_len_data"),
            LOG_SAVE_PATH: self.conf.get("LogConfig","log_save_path"),
            LOG_SAVE_LEVEL: self.conf.get("LogConfig","log_save_level"),
            LOG_BACKCOUNT: self.conf.getint("LogConfig","log_backCount"),
            LOG_FORMAT: self.conf.get("LogConfig","log_format", raw=True), # 若需要格式化的，需要加上raw参数为True
            UPDATE_DOC_NAME: self.conf.get("otherConfig","update_doc_name"),

        }


    def set_config_dict(self, section, option, value):
        """
        doc: 设置配置变量值
        :param section: 一级配置项(str)
        :param option: 二级配置项(str)
        :param value: 配置值(str)
        :return: None
        """
        try:
            self.conf.set(section, option, value) # 更改配置文件对象内容
            self.conf.write(open(self.conf_dir, mode="w+")) # 将更改后的配置文件写入
        except Exception as e:
            print(e)
            logging.error("修改配置项错误！") # TODO:此处日志未能被记录


    def reset_config_dict(self, section_name=None, option_name=None, Value=None, flag=1):
        """
        doc: 按配置备份模板重置设置(详见 config_template.py)
        :param section_name: 配置大类
        :param option_name: 配置项
        :param Value: 配置项值
        :param flag: 重置模式: [全部重置:1] [仅重置指定配置大类:2] [仅重置指定配置项:3] 默认为1
        :return:
        """
        try:
            if flag == 1: # 全部重置 # TODO: 这样子发生变更时，需要开发人员手动同步变更信息是一件很蠢的事情
                # 若有配置大项变更请同步更新此处
                context = softWareConfig_Template +\
                          CommunicationConfig_Template+ \
                          LogConfig_Template

                write_file(self.conf_dir, context) # 写入全部模板
            elif flag == 2:  # 仅重置指定配置大类(暂未启用)
                section = self.conf.sections()
                for sect in section:  # 从大类序列中获取
                    if sect == section_name:
                        pass
            elif flag == 3:  # 仅重置指定配置项(暂未启用)
                pass
        except Exception as e:
            print(e)
            logging.error("重置配置项出错！") # TODO:此处日志未能被记录


config_dir = os.path.join(os.path.dirname(__file__), "../..", "config.cfg") # 读取配置文件路径(以本文件所在目录为起始点)
configs = Config(config_dir) # 配置类实例化用于其他py文件快速读取
