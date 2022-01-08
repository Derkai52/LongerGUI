import sys, os, threading, subprocess, logging
import open3d as o3d
import pyqtgraph.opengl as gl
import numpy as np

from util.log_tool.log import LoggingHandler, logs
from util.config_generator import configObject
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
from resource.ui.login_dialog import LoginDialog


_translate = QCoreApplication.translate




class MainWindow(QMainWindow, Ui_MainWindow): #这个窗口继承了用QtDesignner 绘制的窗口

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Setting_dialog = Setting() # 设置页面,读取配置信息

        # 加载主页面日志信息
        self.logging_handler = LoggingHandler()
        self.logging_handler.newLogging.connect(self.output_gui_logger)
        logs.addHandler(self.logging_handler)

        # 加载位姿数量信息
        from event.parse_event import display_signal
        display_signal.signal_pose.connect(self.output_pose_num)





    def init_sys(self):
        """
        doc: 初始化Hub程序
        """
        mech_interface_ip = configObject.mech_communication_config.mech_interface_ip
        mech_interface_port = configObject.mech_communication_config.mech_interface_port
        robot_server_agent_ip = configObject.robot_communication_config.robot_server_agent_ip
        robot_server_agent_port = configObject.robot_communication_config.robot_server_agent_port

        self.hubProcess = Hub(serverIP=mech_interface_ip, serverPort=mech_interface_port, \
                     connectIP=robot_server_agent_ip, connectPort=robot_server_agent_port)
        self.hubProcess.run()  # 主程序开始运行



    def start_app(self, app_name, args):
        """
        doc: 多线程应用程序启动器
        :param app_name: 应用程序名
        :param args: 应用程序参数
        """
        # if self.setting_dialog.background_setting.start_programs_to_sys_tray:
        #     args += ["--show-mode", "1"]
        print(args[0])
        if not os.path.exists(args[0]):
            critical_box(self, text=self.tr("请先设置应用程序 {} 路径.").format(app_name))
            return None
        os.popen(args[0])
        # self.sub_process_list[app_name] = subprocess.Popen(args, creationflags=subprocess.CREATE_NEW_CONSOLE,
        #                                                    stdout=subprocess.PIPE,
        #                                                    stderr=subprocess.STDOUT, shell=True)

        # threading.Thread(target=self.read_app_output,
        #                  args=[self.sub_process_list[app_name], app_name, args[0]]).start()

    def output_gui_logger(self, log_level, msg):
        """
        doc: 输出日志信息并显示到文本框
        :param log_level: 日志等级数值(int)
        :param msg: 日志信息(str)
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

    # 显示当前位姿数量
    def output_pose_num(self, pose_num):
        self.label_poseNum.setText(pose_num)


    # 启动程序
    @pyqtSlot()
    def on_pushButton_start_clicked(self): # TODO：应当变更为服务注册机制
        if not self.pushButton_start.isCheckable(): # 开启通讯程序
            thread_main = threading.Thread(target=self.init_sys)  # 开启一个线程启动主程序
            thread_main.setDaemon(True)  # 挂后台进程
            thread_main.start()
            logs.info("主程序启动成功")
            self.pushButton_login.setEnabled(False) # 用户登录不可选
            self.pushButton_start.setText("结束运行")
            self.pushButton_start.setCheckable(True)

        else: # 关闭通讯程序
            self.hubProcess.running_flag = False
            self.pushButton_login.setEnabled(True) # 恢复用户可登录状态
            self.pushButton_start.setText("开始运行")
            self.pushButton_start.setCheckable(False)





    def setImage(self, image): # 指定在 label 中显示
        self.label_vision_2D.setPixmap(QPixmap.fromImage(image))

    def imageprocessing(self):
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
        png = QtGui.QPixmap(imgName).scaled(self.label_vision_2D.width(), self.label_vision_2D.height())  # 适应设计label时的大小
        self.label_vision_2D.setPixmap(png)


    # 文件/打开2D图像文件
    @pyqtSlot()
    def on_action_open2DImageFile_triggered(self):
        self.imageprocessing()

    # 显示点云
    def show_cloud_image(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "请选择图像：", '.', "All Files(*);;")
        if fileName != '':
            # 读取点云
            pcd = o3d.io.read_point_cloud(fileName)
            # 获取 Numpy 数组
            np_points = np.asarray(pcd.points)
            # 创建显示对象
            plot = gl.GLScatterPlotItem()
            # 设置显示数据
            plot.setData(pos=np_points, color=(1, 1, 1, 1), size=0.001, pxMode=False)
            # 显示点云
            self.graphicsView.addItem(plot)

    # 文件/打开3D图像文件
    @pyqtSlot()
    def on_action_open3DCloudFile_triggered(self):
        self.show_cloud_image()
        # TODO: 可能保存的是配置或日志文件，目前暂不能明确

    # 设置/系统设置
    @pyqtSlot()
    def on_action_systemSetting_triggered(self):
        self.Setting_dialog.show()
        self.label_status.setStyleSheet("color: rgb(255, 0, 0);\n"
                                        "font: 48pt \"Constantia\";\n"
                                        "border-width: 0px;")
        self.label_status.setText(_translate("MainWindow", "NG")) # TODO:提示符通过标志变量获取


    # 用户登录
    @pyqtSlot()
    def on_pushButton_login_clicked(self):
        Login_Dialog = LoginDialog() # 权限切换页面
        Login_Dialog.exec() # 用户登录
        if Login_Dialog.user_type == 0:
            self.pushButton_login.setText("操作员") # TODO: 不同等级权限应当有不同功能
            pass
        elif Login_Dialog.user_type == 1:
            self.pushButton_login.setText("管理员")
            pass





    # 工具/通信测试助手
    @pyqtSlot()
    def on_action_communicationTest_triggered(self):
        # bg_setting = self.setting_dialog.background_setting
        # if bg_setting.is_viz_needed:
        self.start_app("communication_assistant", [os.path.join(os.path.dirname(__file__), "..","..", "util","test", "NetAssist.exe")])


    # 菜单栏/帮助/关于
    @pyqtSlot()
    def on_action_about_triggered(self):
        information_box(self, "关于软件", "LongerGUI {}\n\nCopyright 1999-2022 BLonger Ltd. All rights reserved.".\
                        format(configObject.software_config.software_version))



    # 菜单栏/帮助/文档
    @pyqtSlot()
    def on_action_docs_triggered(self):
        # is_english = self.setting_dialog.current_language_name() == QLocale(QLocale.English).name() # 若不考虑做国际化语言，可忽略
        # change_log_file = "change_log.html" if is_english else "change_log_zh.html"
        change_log_file = configObject.other_config.update_doc_name
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),"..","update_logs", change_log_file)))
        print(os.path.join(os.path.dirname(__file__),"..", "update_logs", change_log_file))

####################################################
    # 2D图像
    @pyqtSlot()
    def on_pushButton_2DImage_clicked(self):

        self.pushButton_2DImage.setEnabled(False) # TODO: 【差前端的东西】默认只有两种图像，当一个按下另一个必然亮起。推荐方案是用QSS前端渲染出不同状态即可。
        self.pushButton_3DCloud.setEnabled(True)
        self.stackedWidget_display.setCurrentIndex(0)

    # 3D图像
    @pyqtSlot()
    def on_pushButton_3DCloud_clicked(self):
        self.pushButton_2DImage.setEnabled(True) # TODO: 【差前端的东西】默认只有两种图像，当一个按下另一个必然亮起。推荐方案是用QSS前端渲染出不同状态即可。
        self.pushButton_3DCloud.setEnabled(False)
        self.stackedWidget_display.setCurrentIndex(1)
