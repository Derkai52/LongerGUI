import logging
from os import path, mkdir
from struct import pack
from util import json_keys as jk
from util.util_file import write_file
from util.util_file import read_json_file, write_json_file
from util.translations import _translate
from util.setting_file import setting_file_path, sys_settings
# from .adapter_snippet import *
# from interface import messages
# from interface.robot_euler_mapping import KNOWN_ROBOT_EULERS


class SoftWareConfig():
    """
    doc: 软件配置类
    """
    def __init__(self, js):
        self.from_json(js)

    def from_json(self, js):
        self.software_name = js.get(jk.software_name, "LongerGUI") # TODO:[配置读取] 建议读取配置表
        self.software_version = js.get(jk.software_version, "0.1.1-alpha")
        self.project_name = js.get(jk.project_name, "")
        self.project_version = js.get(jk.project_version, 1)
        self.config_path = js.get(jk.config_path, setting_file_path) # 默认保存路径为设定好的（详见setting_file.py）
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


# class DataFormatConfig():
#     def __init__(self, js):
#         self.from_json(js)
#
#     def from_json(self, js):
#         s_data = js.get(jk.data_sent, {})
#         r_data = js.get(jk.data_received, {})
#         codes = [str(messages.VISION_HAS_POSES), str(messages.CENTER_INVALID_COMMAND),
#                  str(messages.VISION_NOT_REGISTERED), str(messages.VISION_NO_POSES), str(messages.VISION_NO_CLOUD),
#                  str(messages.VIZ_COLLISION_CHECKED)]
#         self.status_codes = s_data.get(jk.status_codes, codes)
#         self.labels = s_data.get(jk.labels, [])
#         self.label_codes = s_data.get(jk.label_codes, [])
#         self.is_need_send_object_label = s_data.get(jk.is_need_send_object_label, False)
#         self.is_need_check_cloud = s_data.get(jk.is_need_check_cloud, False)
#         self.is_need_send_pose_num = s_data.get(jk.is_need_send_pose_num, True)
#         self.is_need_fixed_body = s_data.get(jk.is_need_fixed_body, False)
#         self.fixed_body = s_data.get(jk.fixed_body, "")
#         self.is_need_fixed_cmd_tail = s_data.get(jk.is_need_fixed_cmd_tail, False)
#         self.fixed_cmd_tail = s_data.get(jk.fixed_cmd_tail, "")
#         self.field_separator_sent = s_data.get(jk.field_separator, ",")
#         self.is_need_subfield_separator_sent = s_data.get(jk.is_need_subfield_separator_sent, False)
#         self.subfield_separator_sent = s_data.get(jk.subfield_separator, ",")
#         self.status_code_data_type = s_data.get(jk.status_code_data_type, "SHORT")
#         self.pose_num_data_type = s_data.get(jk.pose_num_data_type, "CHAR")
#         self.pose_data_type = s_data.get(jk.pose_data_type, "FLOAT")
#
#         self.field_num = r_data.get(jk.field_num, 1)
#         self.photo_command = r_data.get(jk.photo_command, "r")
#         self.field_separator_received = r_data.get(jk.field_separator, ",")
#         self.subfield_separator_received = r_data.get(jk.subfield_separator, ",")
#         self.is_need_subfield_separator_received = r_data.get(jk.is_need_subfield_separator_received, False)
#         self.is_multi_vision_project = r_data.get(jk.is_multi_vision_project, False)
#         self.vision_name_list = r_data.get(jk.vision_name_list, [])
#         self.vision_name_code_list = r_data.get(jk.vision_name_code_list, [])
#         self.vision_name_pos = r_data.get(jk.vision_name_pos, 1)
#         self.is_need_switch_model = r_data.get(jk.is_need_switch_model, False)
#         self.model_type_pos = r_data.get(jk.model_type_pos, 0)
#         self.subfield_received_start_pos = r_data.get(jk.subfield_received_start_pos, 0)
#         self.subfield_received_end_pos = r_data.get(jk.subfield_received_end_pos, 0)
#         self.hex_fields = r_data.get(jk.hex_fields, [])
#
#     def to_json(self):
#         s_data = {jk.status_codes: self.status_codes,
#                   jk.labels: self.labels,
#                   jk.label_codes: self.label_codes,
#                   jk.is_need_send_object_label: self.is_need_send_object_label,
#                   jk.is_need_check_cloud: self.is_need_check_cloud,
#                   jk.is_need_send_pose_num: self.is_need_send_pose_num,
#                   jk.is_need_fixed_body: self.is_need_fixed_body,
#                   jk.fixed_body: self.fixed_body,
#                   jk.is_need_fixed_cmd_tail: self.is_need_fixed_cmd_tail,
#                   jk.fixed_cmd_tail: self.fixed_cmd_tail,
#                   jk.field_separator: self.field_separator_sent,
#                   jk.is_need_subfield_separator_sent: self.is_need_subfield_separator_sent,
#                   jk.subfield_separator: self.subfield_separator_sent,
#                   jk.status_code_data_type: self.status_code_data_type,
#                   jk.pose_num_data_type: self.pose_num_data_type,
#                   jk.pose_data_type: self.pose_data_type}
#         r_data = {jk.field_num: self.field_num,
#                   jk.photo_command: self.photo_command,
#                   jk.field_separator: self.field_separator_received,
#                   jk.subfield_separator: self.subfield_separator_received,
#                   jk.is_need_subfield_separator_received: self.is_need_subfield_separator_received,
#                   jk.is_multi_vision_project: self.is_multi_vision_project,
#                   jk.vision_name_list: self.vision_name_list,
#                   jk.vision_name_code_list: self.vision_name_code_list,
#                   jk.vision_name_pos: self.vision_name_pos,
#                   jk.is_need_switch_model: self.is_need_switch_model,
#                   jk.model_type_pos: self.model_type_pos,
#                   jk.subfield_received_start_pos: self.subfield_received_start_pos,
#                   jk.subfield_received_end_pos: self.subfield_received_end_pos,
#                   jk.hex_fields: self.hex_fields}
#         return {jk.data_sent: s_data,
#                 jk.data_received: r_data}
#
#
# class ModelConfig():
#     def __init__(self, js):
#         self.from_json(js)
#
#     def from_json(self, js):
#         self.model_dir = js.get(jk.model_dir, "")
#         self.is_need_type_code = js.get(jk.is_need_type_code, False)
#         self.is_switch_model_in_ui = js.get(jk.is_switch_model_in_ui, True)
#         self.model_type_list = js.get(jk.model_type_list, [])
#         self.step_name_dict = js.get(jk.step_name_dict, {})
#
#     def to_json(self):
#         return {jk.model_dir: self.model_dir,
#                 jk.is_need_type_code: self.is_need_type_code,
#                 jk.is_switch_model_in_ui: self.is_switch_model_in_ui,
#                 jk.model_type_list: self.model_type_list,
#                 jk.step_name_dict: self.step_name_dict}


# adapter代码生成器类
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


    # 将各部件(网络、机器人、vision、viz、数据格式等)配置文件写入为json形式并保存到指定路径
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


    # 配置生成器(暂未启用)
    def generate_adapter(self):
        # 1、序列化配置，打包配置内容为json文件
        self.serialize_config()
        try:
            if not path.exists(self.network_config.project_dir):
                mkdir(self.network_config.project_dir)
            self.adapter_class_name = self.network_config.adapter_name[0].upper() + self.network_config.adapter_name[1:]
            self._create_adapter_file()  # 创建adapter文件
            self._create_widget_file()
            self._create_init_file()
        except Exception as e:
            logging.exception(e)