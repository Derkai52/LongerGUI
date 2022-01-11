import logging
from os import path, mkdir
from struct import pack
from util import json_keys as jk
from util.util_file import write_file
from util.util_file import read_json_file, write_json_file
from util.translations import _translate
from util.setting_file import setting_file_path, sys_settings



class SoftWareConfig():
    """
    doc: 软件配置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        self.software_name = js.get(jk.software_name, "LongerGUI")
        self.software_version = js.get(jk.software_version, "0.1.1-alpha")
        self.project_name = js.get(jk.project_name, "")
        self.project_version = js.get(jk.project_version, 1)
        self.config_path = js.get(jk.config_path, setting_file_path)
        self.third_party_equipment = js.get(jk.third_party_equipment, False)


    def to_json(self):
        return {jk.software_name: self.software_name,
                jk.software_version: self.software_version,
                jk.project_name: self.project_name,
                jk.project_version: self.project_version,
                jk.config_path: self.config_path,
                jk.third_party_equipment: self.third_party_equipment}

class MechCommunicationConfig():
    """
    doc: Mech通讯配置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        self.mech_interface_ip = js.get(jk.mech_interface_ip, "")
        self.mech_interface_port = js.get(jk.mech_interface_port, "")
        self.communite_format = js.get(jk.communite_format, "InterFace")
        self.len_client_msg = js.get(jk.len_client_msg, "56")
        self.len_mech_msg = js.get(jk.len_mech_msg, "660")
        self.default_len_data = js.get(jk.default_len_data, 1024)
        self.is_ascii = js.get(jk.is_ascii, True)
        self.endian = js.get(jk.endian, "<")

    def to_json(self):
        return {jk.mech_interface_ip: self.mech_interface_ip,
                jk.mech_interface_port: self.mech_interface_port,
                jk.communite_format: self.communite_format,
                jk.len_client_msg: self.len_client_msg,
                jk.len_mech_msg: self.len_mech_msg,
                jk.default_len_data: self.default_len_data,
                jk.is_ascii: self.is_ascii,
                jk.endian: self.endian}

class RobotCommunicationConfig():
    """
    doc: 机器人通讯配置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        self.robot_server_agent_ip = js.get(jk.robot_server_agent_ip, "")
        self.robot_server_agent_port = js.get(jk.robot_server_agent_port, "")
        self.robot_vendor = js.get(jk.robot_vendor, "")
        self.robot_type = js.get(jk.robot_type, "")


    def to_json(self):
        return {jk.robot_server_agent_ip: self.robot_server_agent_ip,
                jk.robot_server_agent_port: self.robot_server_agent_port,
                jk.robot_vendor: self.robot_vendor,
                jk.robot_type: self.robot_type}

class LogConfig():
    """
    doc: 日志配置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        self.log_save_path = js.get(jk.log_save_path, "")
        self.log_save_level = js.get(jk.log_save_level, "warning")
        self.log_back_count = js.get(jk.log_back_count, 30)
        self.log_format = js.get(jk.log_format, "'%(asctime)s - %(levelname)s: %(message)s'") # bug

    def to_json(self):
        return {jk.log_save_path: self.log_save_path,
                jk.log_save_level: self.log_save_level,
                jk.log_back_count: self.log_back_count,
                jk.log_format: self.log_format}

class DisplayConfig():
    """
    doc: 展示配置页设置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        pass

    def to_json(self):
        pass

class OtherConfig():
    """
    doc: 其他配置页设置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        self.update_doc_name = js.get(jk.update_doc_name, "update_log.html")

    def to_json(self):
        return {jk.update_doc_name: self.update_doc_name}


# 单例模式装饰器
def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton

@singleton
class Generator(object):
    def __init__(self):
        self.deserialize_config()  # 当转化器初始化时，进行反序列化操作(解包json配置文件)

    # 反序列化操作(解包json配置文件设置并将其读取)
    def deserialize_config(self):
        configs = read_json_file(setting_file_path)
        self.software_config = SoftWareConfig(configs.get(jk.software, {}))
        self.mech_communication_config = MechCommunicationConfig(configs.get(jk.mech_communication, {}))
        self.robot_communication_config = RobotCommunicationConfig(configs.get(jk.robot_communication, {}))
        self.log_config = LogConfig(configs.get(jk.log, {}))
        self.display_config = DisplayConfig(configs.get(jk.display, {}))
        self.other_config = OtherConfig(configs.get(jk.other, {}))


    # 序列化操作：将各部分(网络、机器人、vision、viz、数据格式等)配置文件写入为json形式并保存到指定路径
    def serialize_config(self):
        configs = {}
        configs[jk.software] = self.software_config.to_json()
        configs[jk.mech_communication] = self.mech_communication_config.to_json()
        configs[jk.robot_communication] = self.robot_communication_config.to_json()
        configs[jk.log] = self.log_config.to_json()
        configs[jk.display] = self.display_config.to_json()
        configs[jk.other] = self.other_config.to_json()
        logging.info("保存配置信息:{}".format(configs))
        write_json_file(setting_file_path, configs)

    # 代码生成器(暂未启用)
    # def generate_adapter(self):
    #     self.serialize_config() # 序列化配置，打包配置内容为json文件
    #     try:
    #         if not path.exists(self.network_config.project_dir):
    #             mkdir(self.network_config.project_dir)
    #         self.adapter_class_name = self.network_config.adapter_name[0].upper() + self.network_config.adapter_name[1:]
    #         self._create_adapter_file()  # 按照模板创建代码文件
    #         self._create_widget_file()
    #         self._create_init_file()
    #     except Exception as e:
    #         logging.exception(e)

# 使用单例模式实例化配置生成器
configObject = Generator()

