from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal, QTranslator, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView, QDialog, QAction, QMenu, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap, QCursor, QColor
from resource.ui.pyqt_generated.UI_Settings import Ui_Setting
from util.message_box import information_box, warning_box, warning_box_yes_no, critical_box
from util.log_tool.log import logs
import re, sys, os, logging
from util.util_file import write_file
from util.setting_file import setting_file_path
from util.generator import configObject
from util import json_keys as jk



class Setting(QDialog, Ui_Setting): # 这个窗口继承了用QtDesignner绘制的窗口
    adapter_project_dir_changed = pyqtSignal(str)
    def __init__(self):
        super(Setting,self).__init__()
        self.setupUi(self)
        self.init_widget()
        self.fill_from_configfile()


    def init_widget(self):
        self.title_header = self.tr("SettingConfig Generator - ")

    def fill_from_configfile(self):
        """
        doc: 从配置文件读取配置值并填充,作为默认值
        :return:
        """
        self._fill_SoftWareConfig()
        self._fill_ConnectMechConfig()
        self._fill_ConnectRobotConfig()
        self._fill_LogConfig()
        self._fill_DisplayConfig()
        self._fill_OtherConfig()


################ 检查配置页是否出错 ##################
    def check_SoftwareConfig(self):
        """
        doc: 检查软件配置页配置
        :return: 若正常则返回None, 若存在错误情况则返回错误信息(str)
        """
        error_msg = ""

        projectName_text = self.lineEdit_projectName.text()
        if (projectName_text == None) | (projectName_text.find(" ") != -1): # 字符串不为空且没有空格
            error_msg += "工程名称非法,"
        # 新增检查项在此添加
        if error_msg != "":
            error_msg += ":"
        return error_msg

    def check_ConnectMechConfig(self): # TODO: 检查Mech连接配置页是否正确
        """
        doc: 检查与Mech通讯配置页配置
        :return: 若正常则返回None, 若存在错误情况则返回错误信息(str)
        """
        error_msg = ""
        # error_msg = "Mech网络连接"
        # 新增检查项在此添加

        if error_msg != "":
            error_msg += ":"
        return error_msg

    def check_ConnectRobotConfig(self): # TODO：检查机器人连接配置页是否正确
        """
        doc: 检查与Robot通讯配置页配置
        :return: 若正常则返回None, 若存在错误情况则返回错误信息(str)
        """
        error_msg = ""
        # error_msg = "Robot网络连接"
        # 新增检查项在此添加

        if error_msg != "":
            error_msg += ":"
        return error_msg

    def check_config(self):
        """
        doc: 检查全局配置(用于保存配置时)
        :return: 错误信息
        """
        error_msg = "" # 默认错误信息为空
        error_msg += self.check_SoftwareConfig()
        error_msg += self.check_ConnectMechConfig()
        error_msg += self.check_ConnectRobotConfig()
        print(error_msg)
        return error_msg # 返回包含错误信息的字符串(若正常则返回None， 若有错误情况则返回对应错误提示字符串)

################### 初始化/填充 设置 ##############################
    def _fill_SoftWareConfig(self):
        self.lineEdit_projectName.setText(configObject.software_config.project_name) # 填充默认工程名称
        self.spinBox_projectVersion.setValue(configObject.software_config.project_version) # 填充默认工程版本号

        if configObject.software_config.third_party_equipment: # 是否使用第三方设备
            check_flag = True
        else:
            check_flag = False
        self.checkBox_ExistThirdParty.setChecked(check_flag)





    def _gather_SoftWareConfig(self):
        software_config = {}
        software_config[jk.project_name] = self.lineEdit_projectName.text()
        software_config[jk.project_version] = self.spinBox_projectVersion.value()
        software_config[jk.third_party_equipment] = self.checkBox_ExistThirdParty.checkState()


        return software_config

    def _fill_ConnectMechConfig(self):
        index_flag = None
        if configObject.mech_communication_config.communite_format == "InterFace":
            index_flag = 0
        # 若有新数据模式请在此处添加
        else:
            print("[通讯模式]配置文件出现错误") # TODO：[日志类]收录日志
        self.comboBox_CommuniteFormat.setCurrentIndex(index_flag) # 填充通讯模式(InterFace...)

        index_flag2 = None
        if configObject.mech_communication_config.is_ascii: # 是否为ASCII码
            index_flag2 = 0
        else:
            index_flag2 = 1
        # 若有新数据模式请在此处添加
        self.comboBox_CommuniteFormat_2.setCurrentIndex(index_flag2) # 填充通讯格式(ASCII、HEX...)

        self.lineEdit_MechCenter_IP.setText(configObject.mech_communication_config.mech_interface_ip) # 填充Mech-Center IP地址
        self.lineEdit_MechCenter_Port.setText(configObject.mech_communication_config.mech_interface_port) # 填充Mech-Center InterFace端口号

    def _gather_ConnectMechConfig(self):
        connect_mech_config = {}

        communite_format_list = ["InterFace"] # 新增通讯模式在此处添加
        # index_flag = communite_format_list.find(configObject.mech_communication_config.communite_format)
        connect_mech_config[jk.communite_format] = communite_format_list[self.comboBox_CommuniteFormat.currentIndex()]
        if self.comboBox_CommuniteFormat_2.currentIndex() == 0:
            connect_mech_config[jk.is_ascii] = True
        else:
            connect_mech_config[jk.is_ascii] = False
        connect_mech_config[jk.mech_interface_ip] = self.lineEdit_MechCenter_IP.text()
        connect_mech_config[jk.mech_interface_port] = self.lineEdit_MechCenter_Port.text()

        return connect_mech_config

    def _fill_ConnectRobotConfig(self):
        robot_vendor_list = ["ABB","FANUC","UR"] # 新增机器人品牌在此处添加 # TODO: [新增类]建议使用一个机器人类来便于管理多种机器人
        try:
            index_flag = robot_vendor_list.index(configObject.robot_communication_config.robot_vendor)
            self.comboBox_RobotVendor.setCurrentIndex(index_flag)  # 填充机器人品牌信息
        except Exception as e:
            print("[机器人型号]配置文件出现错误") # TODO：[日志类]收录日志

        robot_type_list = ["UR_5"]  # 新增机器人型号在此处添加 # TODO: [新增类]建议使用一个机器人类来便于管理多种机器人
        try:
            index_flag = robot_type_list.index(configObject.robot_communication_config.robot_type)
            self.comboBox_RobotType.setCurrentIndex(index_flag) # 填充机器人型号名
        except Exception as e:
            print("[机器人具体型号]配置文件出现错误") # TODO：[日志类]收录日志


        self.lineEdit_RobotIP.setText(configObject.robot_communication_config.robot_server_agent_ip) # 填充机器人接口 IP地址
        self.lineEdit_RobotPort.setText(configObject.robot_communication_config.robot_server_agent_port) # 填充机器人接口 端口号

    def _gather_ConnectRobotConfig(self):
        connect_robot_config = {}
        robot_vendor_list = ["ABB","FANUC","UR"] # 新增机器人在此处添加 # TODO: [新增类]建议使用一个机器人类来便于管理多种机器人
        connect_robot_config[jk.robot_vendor] = robot_vendor_list[self.comboBox_RobotVendor.currentIndex()]
        connect_robot_config[jk.robot_server_agent_ip] = self.lineEdit_RobotIP.text()
        connect_robot_config[jk.robot_server_agent_port] = self.lineEdit_RobotPort.text()

        return connect_robot_config

    def _fill_LogConfig(self):
        self.spinBox_log_days.setValue(configObject.log_config.log_back_count) # 填充默认日志记录有效期(不在有效期的历史日志将被清除)
        try:
            log_levels_list = ["debug", "info", "warning", "error"]
            index_flag = log_levels_list.index(configObject.log_config.log_save_level.lower())  # 将读取到的日志等级字符转为小写字符表示
            self.comboBox_log_levels.setCurrentIndex(index_flag)  # 填充默认日志等级
        except Exception as e:
            print("[日志等级设置]配置文件出现错误")  # TODO：[日志类]收录日志
        self.lineEdit_log_format.setText(configObject.log_config.log_format) # 填充默认日志格式
        self.lineEdit_log_save_path.setText(configObject.log_config.log_save_path) # 填充默认日志存储路径

    def _gather_LogConfig(self):
        log_config = {}
        log_config[jk.log_back_count] = self.spinBox_log_days.value()
        log_config[jk.log_save_level] = self.comboBox_log_levels.currentText().lower()  # 将读取到的日志等级字符转为小写字符表示
        return log_config

    def _fill_DisplayConfig(self):
        pass

    def _gather_DisplayConfig(self):
        display_config = {}


        return display_config

    def _fill_OtherConfig(self):
        self.lineEdit_update_doc_name.setText(configObject.other_config.update_doc_name)

    def _gather_OtherConfig(self):
        other_config = {}
        other_config[jk.update_doc_name] = self.lineEdit_update_doc_name.text()
        return other_config



#################### 点击 左侧的设置项直接跳转到对应设置项 ################
    @pyqtSlot()
    def on_pushButton_SoftWareConfig_clicked(self):
        self.main_config_widget.setCurrentIndex(0)

    @pyqtSlot()
    def on_pushButton_ConnectMech_clicked(self):
        self.main_config_widget.setCurrentIndex(1)

    @pyqtSlot()
    def on_pushButton_ConnectRobot_clicked(self):
        self.main_config_widget.setCurrentIndex(2)

    @pyqtSlot()
    def on_pushButton_ConnectThirdParty_clicked(self):
        self.main_config_widget.setCurrentIndex(3)


##################### 点击 下一步 ##################################
    @pyqtSlot()
    def on_pushButton_next_SoftwareConfig_clicked(self):
        error_msg = self.check_SoftwareConfig()
        if error_msg:
            critical_box(self, text=error_msg)
        else:
            self.main_config_widget.setCurrentIndex(1)

    @pyqtSlot()
    def on_pushButton_next_ConnectMechConfig_clicked(self):
        error_msg = self.check_ConnectMechConfig()
        if error_msg:
            critical_box(self, text=error_msg)
        else:
            self.main_config_widget.setCurrentIndex(2)

    @pyqtSlot()
    def on_pushButton_next_ConnectRobotConfig_clicked(self):
        error_msg = self.check_ConnectRobotConfig()
        if error_msg:
            critical_box(self, text=error_msg)
        else:
            self.main_config_widget.setCurrentIndex(3)

##################### 点击 标题栏按钮 #############
    @pyqtSlot()
    def on_pushButton_helpDoc_clicked(self):
        information_box(self, "设置说明手册", "LongerGUI {}\n\n有空记得把手册更新". \
                        format(configObject.software_config.software_version)) # TODO: 【文档类】更新设置项说明手册

    @pyqtSlot()
    def on_pushButton_ResetConfig_clicked(self):
        pass # TODO:[新增功能]重置配置

    def parse_error_msg(self, error_msg):
        """
        doc: 格式化生成报错信息用于显示
        :param error_msg: 报错信息(str)
        :return: 用于显示的报错信息(str)
        """
        msg_frame = ":配置错误\n" # 报错信息模板
        error_msg_list = re.split(":|,", error_msg) # 不同配置页用":"作为间隔符，配置页内不同配置项用","作为间隔符
        new_error_msg_list = [i for i in error_msg_list if i != ''] # 去除列表空值
        error_msgs = msg_frame.join(new_error_msg_list) # 插入报错模板完善报错信息
        error_msgs += msg_frame # 用于补齐最后一项(因为join是插空的)
        print(error_msgs)
        return error_msgs

    def choose_project_dir(self, title):
        """
        doc: 选择保存文件夹目录
        :param title: 窗口标题(暂未启用)
        :return: 选择保存文件夹目录路径
        """
        project_dir = QFileDialog.getExistingDirectory(self, self.tr("另存为配置文件为:"), os.path.expanduser("~"))
        if not project_dir:
            warning_box(self, text=self.tr("保存配置文件错误!"))
            return
        self.setWindowTitle(self.title_header + project_dir + "/" + configObject.software_config.project_name)
        return project_dir

    def save_config(self):
        """
        doc: 保存配置表到文件
        :return:
        """
        configObject.software_config.from_json(self._gather_SoftWareConfig())
        configObject.mech_communication_config.from_json(self._gather_ConnectMechConfig())
        configObject.robot_communication_config.from_json(self._gather_ConnectRobotConfig())
        configObject.log_config.from_json(self._gather_LogConfig())
        configObject.display_config.from_json(self._gather_DisplayConfig())
        configObject.other_config.from_json(self._gather_OtherConfig())
        configObject.serialize_config()

    def config_generator(self):
        """
        doc: 配置表文件生成器
        :return:
        """
        # if not self.on_check_configs_clicked():
        #     return
        project_dir = configObject.software_config.config_path
        print("生成目录为：",project_dir)
        if os.path.exists(project_dir):
            if warning_box_yes_no(self, text=project_dir + self.tr("该路径下文件已存在，是否覆盖它?")) == QMessageBox.No:
                return
        # configObject.generate_adapter() # 代码生成器(暂未启用)
        self.save_config()

        self.adapter_project_dir_changed.emit(project_dir)
        msg = self.tr("配置生成成功！")
        if os.path.exists(project_dir):
            msg += self.tr("请重启软件！")
        information_box(self, text=msg)
        self.close()



    ## 另存文件功能(未启用)
    # @pyqtSlot()
    # def on_pushButton_SaveConfigAsFile_clicked(self):
    #     error_msg = self.check_config() # 检查全局配置，并返回检查结果
    #     if len(error_msg) != 0:
    #         error_msgs = self.parse_error_msg(error_msg)
    #         critical_box(self, text=error_msgs)
    #
    #     if not self.choose_project_dir(self.tr("选择保存目录")):
    #         return
    #     print("文件另存为！")
    #     self.config_generator()


    @pyqtSlot()
    def on_pushButton_SaveConfig_clicked(self):
        error_msg = self.check_config() # 检查全局配置，并返回检查结果
        if len(error_msg) != 0:
            error_msgs = self.parse_error_msg(error_msg)
            critical_box(self, text=error_msgs)
        # if not configObject.software_config.config_path or configObject.software_config.config_path.split("/")[-1]\
        #         != self.lineEdit_config_path.text(): # 如果配置文件或目录不存在就选择路径新建配置文件
        #     if not self.choose_project_dir(self.tr("选择保存目录")):
        #         return
        print("文件保存！")
        self.config_generator()

