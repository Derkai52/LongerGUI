from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal, QTranslator, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView, QDialog, QAction, QMenu
from PyQt5.QtGui import QIcon, QFont, QPixmap, QCursor, QColor
from resource.ui.pyqt_generated.UI_Settings import Ui_Setting
from util.message_box import information_box, warning_box, warning_box_yes_no, critical_box
from util.log_tool.log import logs, readConfig
import re


class Setting(QDialog, Ui_Setting): # 这个窗口继承了用QtDesignner绘制的窗口
    def __init__(self):
        super(Setting,self).__init__()
        self.setupUi(self)
        self.fill_from_configfile()

    def fill_from_configfile(self):
        """
        doc: 从配置文件读取配置值并填充,作为默认值
        :return:
        """
        self._fill_SoftWareConfig()
        self._fill_ConnectMechConfig()
        self._fill_ConnectRobotConfig()


################ 检查配置页是否出错 ##################
    def check_SoftwareConfig(self):
        """
        doc: 检查软件配置页配置
        :return: 若正常则返回None, 若存在错误情况则返回错误信息(str)
        """
        error_msg = None
        # error_msg = "工程名称"
        # 新增检查项在此添加

        # error_msg += ":"
        return error_msg

    def check_ConnectMechConfig(self):
        """
        doc: 检查与Mech通讯配置页配置
        :return: 若正常则返回None, 若存在错误情况则返回错误信息(str)
        """
        error_msg = None
        # error_msg = "Mech网络连接"
        # 新增检查项在此添加

        # error_msg += ":"
        return error_msg

    def check_ConnectRobotConfig(self):
        """
        doc: 检查与Robot通讯配置页配置
        :return: 若正常则返回None, 若存在错误情况则返回错误信息(str)
        """
        error_msg = None
        # error_msg = "Robot网络连接"
        # 新增检查项在此添加

        # error_msg += ":"
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
        self.lineEdit_projectName.setText(readConfig["project_name"]) # 填充默认工程名称
        self.lineEdit_projectVersion.setText(readConfig["software_version"]) # 填充默认工程版本号

        check_flag = None
        if readConfig["third_party_equipment"]: # 是否使用第三方设备
            check_flag = True
        else:
            check_flag = False
        self.checkBox_ExistThirdParty.setChecked(check_flag)

    def _fill_ConnectMechConfig(self):
        index_flag = None
        if readConfig["communite_format"] == "InterFace":
            index_flag = 0
        # 若有新数据模式请在此处添加
        else:
            print("[通讯模式]配置文件出现错误") # TODO：[日志类]收录日志
        self.comboBox_CommuniteFormat.setCurrentIndex(index_flag) # 填充通讯模式(InterFace...)

        index_flag2 = None
        if readConfig["is_ascii"]: # 是否为ASCII码
            index_flag2 = 0
        else:
            index_flag2 = 1
        # 若有新数据模式请在此处添加
        self.comboBox_CommuniteFormat_2.setCurrentIndex(index_flag2) # 填充通讯格式(ASCII、HEX...)

        self.lineEdit_MechCenter_IP.setText(readConfig["mech_interface_ip"]) # 填充Mech-Center IP地址
        self.lineEdit_MechCenter_Port.setText(readConfig["mech_interface_port"]) # 填充Mech-Center InterFace端口号

    def _fill_ConnectRobotConfig(self):
        index_flag = None
        if readConfig["robot_vendor"] == "ABB": # TODO: [新增类]建议使用一个机器人类来便于管理多种机器人
            index_flag = 0
        elif readConfig["robot_vendor"] == "FANUC":
            index_flag = 1
        # 新增机器人在此处添加
        else:
            print("[机器人型号]配置文件出现错误") # TODO：[日志类]收录日志
        self.comboBox_RobotVendor.setCurrentIndex(index_flag) # 填充机器人型号

        self.lineEdit_RobotIP.setText(readConfig["robot_server_agent_ip"]) # 填充机器人接口 IP地址
        self.lineEdit_RobotPort.setText(readConfig["robot_server_agent_port"]) # 填充机器人接口 端口号





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
                        format(readConfig["software_version"])) # TODO: 【文档类】更新设置项说明手册

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

    @pyqtSlot()
    def on_pushButton_SaveConfig_clicked(self):
        error_msg = self.check_config() # 检查全局配置，并返回检查结果
        if len(error_msg) != 0:
            error_msgs = self.parse_error_msg(error_msg)
            critical_box(self, text=error_msgs)