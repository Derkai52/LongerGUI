import sys, os, threading, subprocess, logging
from util.log_tool.log import LoggingHandler, logs, readConfig
from util.message_box import information_box, warning_box, warning_box_yes_no, critical_box
from communication.hub import Hub # 通讯中心
from util.format_adapter import * # 可视化

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, Qt, pyqtSignal, QTranslator, QCoreApplication, QUrl
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView, QDialog, QAction, QMenu, QFileDialog, QTabWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont, QPixmap, QCursor, QColor, QImage, QDesktopServices, QTextCursor, QBrush

# 新子页面可在此处添加
from resource.ui.pyqt_generated.UI_MainWindow import Ui_MainWindow
from resource.ui.setting import Setting
from resource.ui.login_permission import LoginPermission


_translate = QCoreApplication.translate




class MainWindow(QMainWindow, Ui_MainWindow): #这个窗口继承了用QtDesignner 绘制的窗口

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Setting_dialog = Setting() # 设置页面,读取配置信息
        self.LoginPermission = LoginPermission() # 权限切换页面

        # 加载主页面日志信息
        self.logging_handler = LoggingHandler()
        self.logging_handler.newLogging.connect(self.output_center_logger)
        logs.addHandler(self.logging_handler)


    def init_sys(self):
        """
        doc: 初始化主程序
        :return:
        """
        mech_interface_ip = readConfig["mech_interface_ip"]
        mech_interface_port = readConfig["mech_interface_port"]
        robot_server_agent_ip = readConfig["robot_server_agent_ip"]
        robot_server_agent_port = readConfig["robot_server_agent_port"]
        if True:
            client = Hub(serverIP=mech_interface_ip, serverPort=mech_interface_port, \
                         connectIP=robot_server_agent_ip, connectPort=robot_server_agent_port)
            client.run()  # 主程序开始运行

        else:
            print("Please input config_tool.cfg path or connect information")
            print("Client configPath")
            print("Client serverIP serverPort connectIP connectPort")


    def start_app(self, app_name, args):
        """
        doc: 多线程应用程序启动器
        :param app_name: 应用程序名
        :param args: 应用程序参数
        :return: None
        """
        if self.setting_dialog.background_setting.start_programs_to_sys_tray:
            args += ["--show-mode", "1"]

        if not os.path.exists(args[0]):
            # critical_box(self, text=self.tr("Please set {} path.").format(app_name))
            print("请先设置应用程序路径！")
            return None
        if self.is_app_started(app_name):
            # critical_box(self, text=self.tr("The {} is already running.").format(app_name))
            print("该应用程序已运行！")
            return None
        self.sub_process_list[app_name] = subprocess.Popen(args, creationflags=subprocess.CREATE_NEW_CONSOLE,
                                                           stdout=subprocess.PIPE,
                                                           stderr=subprocess.STDOUT, shell=True)

        threading.Thread(target=self.read_app_output,
                         args=[self.sub_process_list[app_name], app_name, args[0]]).start()

    def output_center_logger(self, log_level, msg):
        """
        doc: 输出日志信息并显示到文本框
        :param log_level: 日志等级数值(int)
        :param msg: 日志信息(str)
        :return: None
        """
        tf = self.PlainTextEdit_logText.currentCharFormat()
        tf.setForeground(
            QBrush(
                ansiColor(
                    logging_to_log_code.get(
                        log_level,
                        LOG_CODE_DEBUG) - # 若找不到该等级，默认值为 LOG_CODE_DEBUG 等级，详见 dict.get() 中 default参数用法
                    TextColorStart)))
        cursor = self.PlainTextEdit_logText.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(msg, tf)
        cursor.insertText('\n')
        scrollbar = self.PlainTextEdit_logText.verticalScrollBar()
        if scrollbar:
            scrollbar.setSliderPosition(scrollbar.maximum())

    # 启动程序
    @pyqtSlot()
    def on_pushButton_start_clicked(self): # TODO：应当变更为服务注册机制
        # self.output_center_logger("wefwfes24r2t2\nwfrw4rg")
        thread_main = threading.Thread(target=self.init_sys)  # 开启一个线程启动主程序
        thread_main.setDaemon(True)  # 挂后台进程
        thread_main.start()
        logs.info("主程序启动成功")
        self.pushButton_start.setEnabled(False) # 检测到按下后就不可使用


    # 菜单栏/帮助/关于
    @pyqtSlot()
    def on_action_about_triggered(self):
        information_box(self, "关于软件", "LongerGUI {}\n\nCopyright 1999-2021 BLonger Ltd. All rights reserved.".\
                        format(readConfig["software_version"]))

    # 菜单栏/帮助/文档
    @pyqtSlot()
    def on_action_docs_triggered(self):
        # is_english = self.setting_dialog.current_language_name() == QLocale(QLocale.English).name() # 若不考虑做国际化语言，可忽略
        # change_log_file = "change_log.html" if is_english else "change_log_zh.html"
        change_log_file = readConfig["update_doc_name"]
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),"..","update_logs", change_log_file)))
        print(os.path.join(os.path.dirname(__file__),"..", "update_logs", change_log_file))

    # 设置/系统设置
    @pyqtSlot()
    def on_action_systemSetting_triggered(self):
        self.Setting_dialog.show()
        self.label_status.setStyleSheet("color: rgb(255, 0, 0);\n"
                                        "font: 48pt \"Constantia\";\n"
                                        "border-width: 0px;")
        self.label_status.setText(_translate("MainWindow", "NG")) # TODO:提示符通过标志变量获取
        # TODO: 连接至子窗口(设置页)

    # 设置/登录权限
    @pyqtSlot()
    def on_action_loginAuthority_triggered(self):
        self.LoginPermission.show()
        print("登录权限")

    def setImage(self, image): # 指定在 label 中显示
        self.label_leftImage.setPixmap(QPixmap.fromImage(image))

    def imageprocessing(self, flag):
        """
        doc: 获取一张2D图像并显示在指定label控件上
        :return: None
        """
        print("Show Image...") # TODO: 目前并不能保证图像能以合适的比例进行缩放。因为目前取决与Label尺寸比例
        imgName,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)") # 窗口标题、首先定位目录(以当前目录为基准)、显示可筛选文件类型

        #利用qlabel显示图片
        print(str(imgName))
        png = QtGui.QPixmap(imgName).scaled(self.label_leftImage.width(), self.label_leftImage.height())  # 适应设计label时的大小
        if flag == 1:
            self.label_leftImage.setPixmap(png)
        if flag == 2:
            self.label_rightImage.setPixmap(png)


    # 文件/打开
    @pyqtSlot()
    def on_action_openFile_triggered(self):
        print("打开了文件")
        self.imageprocessing(1)
        # TODO: 可能打开的是2D图或3D图。即未来该功能可能会被迁移到其他地方

    # 文件/保存
    @pyqtSlot()
    def on_action_saveFile_triggered(self):
        print("保存了文件")
        self.imageprocessing(2)
        # TODO: 可能保存的是配置或日志文件，目前暂不能明确