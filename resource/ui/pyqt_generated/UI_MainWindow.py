# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 750))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Horizontal_status = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Horizontal_status.sizePolicy().hasHeightForWidth())
        self.Horizontal_status.setSizePolicy(sizePolicy)
        self.Horizontal_status.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"\n"
"")
        self.Horizontal_status.setObjectName("Horizontal_status")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Horizontal_status)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_status = QtWidgets.QLabel(self.Horizontal_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        self.label_status.setMinimumSize(QtCore.QSize(30, 15))
        self.label_status.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_status.setFont(font)
        self.label_status.setMouseTracking(True)
        self.label_status.setTabletTracking(False)
        self.label_status.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setToolTipDuration(0)
        self.label_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_status.setAutoFillBackground(False)
        self.label_status.setStyleSheet("color: rgb(0, 255, 127);\n"
"font: 48pt \"Constantia\";\n"
"border-width: 0px;")
        self.label_status.setFrameShape(QtWidgets.QFrame.HLine)
        self.label_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_status.setLineWidth(0)
        self.label_status.setMidLineWidth(0)
        self.label_status.setTextFormat(QtCore.Qt.AutoText)
        self.label_status.setScaledContents(False)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setWordWrap(False)
        self.label_status.setIndent(0)
        self.label_status.setOpenExternalLinks(False)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_16.addWidget(self.label_status)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(0, 1, -1, 1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 9, 9, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_communiteStatus = QtWidgets.QHBoxLayout()
        self.horizontalLayout_communiteStatus.setObjectName("horizontalLayout_communiteStatus")
        self.label_text_communiteStatus = QtWidgets.QLabel(self.Horizontal_status)
        self.label_text_communiteStatus.setEnabled(False)
        self.label_text_communiteStatus.setStyleSheet("border-width: 0px;\n"
"")
        self.label_text_communiteStatus.setObjectName("label_text_communiteStatus")
        self.horizontalLayout_communiteStatus.addWidget(self.label_text_communiteStatus)
        self.label_communiteStatus = QtWidgets.QLabel(self.Horizontal_status)
        self.label_communiteStatus.setEnabled(False)
        self.label_communiteStatus.setStyleSheet("border-width: 0px;\n"
"color: rgb(0, 170, 0);")
        self.label_communiteStatus.setObjectName("label_communiteStatus")
        self.horizontalLayout_communiteStatus.addWidget(self.label_communiteStatus)
        self.verticalLayout_3.addLayout(self.horizontalLayout_communiteStatus)
        self.horizontalLayout_beatTime = QtWidgets.QHBoxLayout()
        self.horizontalLayout_beatTime.setObjectName("horizontalLayout_beatTime")
        self.label_text_communiteTime = QtWidgets.QLabel(self.Horizontal_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text_communiteTime.sizePolicy().hasHeightForWidth())
        self.label_text_communiteTime.setSizePolicy(sizePolicy)
        self.label_text_communiteTime.setStyleSheet("border-width: 0px;")
        self.label_text_communiteTime.setObjectName("label_text_communiteTime")
        self.horizontalLayout_beatTime.addWidget(self.label_text_communiteTime)
        self.label_beatTime = QtWidgets.QLabel(self.Horizontal_status)
        self.label_beatTime.setEnabled(False)
        self.label_beatTime.setStyleSheet("border-width: 0px;\n"
"font: 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_beatTime.setObjectName("label_beatTime")
        self.horizontalLayout_beatTime.addWidget(self.label_beatTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_beatTime)
        self.horizontalLayout_18.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(54, 19, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_runningNum = QtWidgets.QHBoxLayout()
        self.horizontalLayout_runningNum.setObjectName("horizontalLayout_runningNum")
        self.label_text_runningNum = QtWidgets.QLabel(self.Horizontal_status)
        self.label_text_runningNum.setEnabled(False)
        self.label_text_runningNum.setStyleSheet("border-width: 0px;\n"
"")
        self.label_text_runningNum.setObjectName("label_text_runningNum")
        self.horizontalLayout_runningNum.addWidget(self.label_text_runningNum)
        self.label_runningNum = QtWidgets.QLabel(self.Horizontal_status)
        self.label_runningNum.setEnabled(False)
        self.label_runningNum.setStyleSheet("border-width: 0px;\n"
"")
        self.label_runningNum.setObjectName("label_runningNum")
        self.horizontalLayout_runningNum.addWidget(self.label_runningNum)
        self.verticalLayout_12.addLayout(self.horizontalLayout_runningNum)
        self.horizontalLayout_poseNum = QtWidgets.QHBoxLayout()
        self.horizontalLayout_poseNum.setObjectName("horizontalLayout_poseNum")
        self.label_text_poseNum = QtWidgets.QLabel(self.Horizontal_status)
        self.label_text_poseNum.setEnabled(False)
        self.label_text_poseNum.setStyleSheet("border-width: 0px;\n"
"")
        self.label_text_poseNum.setObjectName("label_text_poseNum")
        self.horizontalLayout_poseNum.addWidget(self.label_text_poseNum)
        self.label_poseNum = QtWidgets.QLabel(self.Horizontal_status)
        self.label_poseNum.setEnabled(False)
        self.label_poseNum.setStyleSheet("border-width: 0px;\n"
"")
        self.label_poseNum.setObjectName("label_poseNum")
        self.horizontalLayout_poseNum.addWidget(self.label_poseNum)
        self.verticalLayout_12.addLayout(self.horizontalLayout_poseNum)
        self.horizontalLayout_18.addLayout(self.verticalLayout_12)
        spacerItem2 = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.horizontalLayout_runningTime = QtWidgets.QHBoxLayout()
        self.horizontalLayout_runningTime.setObjectName("horizontalLayout_runningTime")
        self.label_text_runningTime = QtWidgets.QLabel(self.Horizontal_status)
        self.label_text_runningTime.setEnabled(False)
        self.label_text_runningTime.setStyleSheet("border-width: 0px;\n"
"")
        self.label_text_runningTime.setObjectName("label_text_runningTime")
        self.horizontalLayout_runningTime.addWidget(self.label_text_runningTime)
        self.label_runningTime = QtWidgets.QLabel(self.Horizontal_status)
        self.label_runningTime.setEnabled(False)
        self.label_runningTime.setStyleSheet("border-width: 0px;\n"
"")
        self.label_runningTime.setObjectName("label_runningTime")
        self.horizontalLayout_runningTime.addWidget(self.label_runningTime)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_runningTime)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)
        self.pushButton_start = QtWidgets.QPushButton(self.Horizontal_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(14)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_17.addWidget(self.pushButton_start)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.verticalLayout_9.addWidget(self.Horizontal_status)
        self.horizontalLayout_display = QtWidgets.QHBoxLayout()
        self.horizontalLayout_display.setObjectName("horizontalLayout_display")
        self.verticalLayout_display_vision = QtWidgets.QVBoxLayout()
        self.verticalLayout_display_vision.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_display_vision.setObjectName("verticalLayout_display_vision")
        self.stackedWidget_display = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_display.setObjectName("stackedWidget_display")
        self.page_vision_2D = QtWidgets.QWidget()
        self.page_vision_2D.setObjectName("page_vision_2D")
        self.gridLayout = QtWidgets.QGridLayout(self.page_vision_2D)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_vision_2D = QtWidgets.QLabel(self.page_vision_2D)
        self.label_vision_2D.setObjectName("label_vision_2D")
        self.gridLayout_3.addWidget(self.label_vision_2D, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stackedWidget_display.addWidget(self.page_vision_2D)
        self.page_vision_3D = QtWidgets.QWidget()
        self.page_vision_3D.setObjectName("page_vision_3D")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_vision_3D)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.stackedWidget_display.addWidget(self.page_vision_3D)
        self.verticalLayout_display_vision.addWidget(self.stackedWidget_display)
        self.horizontalLayout_display_vision_chioce = QtWidgets.QHBoxLayout()
        self.horizontalLayout_display_vision_chioce.setObjectName("horizontalLayout_display_vision_chioce")


        from util.vision.cloud_process import cloudshow
        cloudshow(self)

        self.pushButton_2DImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2DImage.setObjectName("pushButton_2DImage")
        self.horizontalLayout_display_vision_chioce.addWidget(self.pushButton_2DImage)
        self.pushButton_3DCloud = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3DCloud.setObjectName("pushButton_3DCloud")
        self.horizontalLayout_display_vision_chioce.addWidget(self.pushButton_3DCloud)
        self.verticalLayout_display_vision.addLayout(self.horizontalLayout_display_vision_chioce)
        self.horizontalLayout_display.addLayout(self.verticalLayout_display_vision)
        self.verticalLayout_log_data_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_log_data_3.setObjectName("verticalLayout_log_data_3")
        self.label_text_displayData = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_text_displayData.sizePolicy().hasHeightForWidth())
        self.label_text_displayData.setSizePolicy(sizePolicy)
        self.label_text_displayData.setMinimumSize(QtCore.QSize(0, 0))
        self.label_text_displayData.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.label_text_displayData.setObjectName("label_text_displayData")
        self.verticalLayout_log_data_3.addWidget(self.label_text_displayData)
        self.widget_displayData = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_displayData.sizePolicy().hasHeightForWidth())
        self.widget_displayData.setSizePolicy(sizePolicy)
        self.widget_displayData.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"\n"
"")
        self.widget_displayData.setObjectName("widget_displayData")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.widget_displayData)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.PlainTextEdit_logText = QtWidgets.QPlainTextEdit(self.widget_displayData)
        self.PlainTextEdit_logText.setObjectName("PlainTextEdit_logText")
        self.verticalLayout_18.addWidget(self.PlainTextEdit_logText)
        self.horizontalLayout_32.addLayout(self.verticalLayout_18)
        self.verticalLayout_log_data_3.addWidget(self.widget_displayData)
        self.horizontalLayout_display.addLayout(self.verticalLayout_log_data_3)
        self.horizontalLayout_display.setStretch(0, 5)
        self.horizontalLayout_display.setStretch(1, 1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_display)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_setting = QtWidgets.QMenu(self.menubar)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_function = QtWidgets.QMenu(self.menubar)
        self.menu_function.setObjectName("menu_function")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_openFile = QtWidgets.QAction(MainWindow)
        self.action_openFile.setCheckable(True)
        self.action_openFile.setObjectName("action_openFile")
        self.action_saveFile = QtWidgets.QAction(MainWindow)
        self.action_saveFile.setObjectName("action_saveFile")
        self.action_systemSetting = QtWidgets.QAction(MainWindow)
        self.action_systemSetting.setObjectName("action_systemSetting")
        self.actionbanben = QtWidgets.QAction(MainWindow)
        self.actionbanben.setObjectName("actionbanben")
        self.action_switchScene = QtWidgets.QAction(MainWindow)
        self.action_switchScene.setObjectName("action_switchScene")
        self.action_switchLayout = QtWidgets.QAction(MainWindow)
        self.action_switchLayout.setObjectName("action_switchLayout")
        self.action_loginAuthority = QtWidgets.QAction(MainWindow)
        self.action_loginAuthority.setObjectName("action_loginAuthority")
        self.action_virtualKeyboard = QtWidgets.QAction(MainWindow)
        self.action_virtualKeyboard.setObjectName("action_virtualKeyboard")
        self.action_communicationTest = QtWidgets.QAction(MainWindow)
        self.action_communicationTest.setObjectName("action_communicationTest")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_docs = QtWidgets.QAction(MainWindow)
        self.action_docs.setObjectName("action_docs")
        self.menu_file.addAction(self.action_openFile)
        self.menu_file.addAction(self.action_saveFile)
        self.menu_setting.addAction(self.action_systemSetting)
        self.menu_setting.addAction(self.action_loginAuthority)
        self.menu_function.addAction(self.action_switchScene)
        self.menu_function.addAction(self.action_switchLayout)
        self.menu_tools.addAction(self.action_virtualKeyboard)
        self.menu_tools.addAction(self.action_communicationTest)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_docs)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_function.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_status.setText(_translate("MainWindow", "<html><head/><body><p>OK</p></body></html>"))
        self.label_text_communiteStatus.setText(_translate("MainWindow", "通信状态："))
        self.label_communiteStatus.setText(_translate("MainWindow", "通信连接成功"))
        self.label_text_communiteTime.setText(_translate("MainWindow", "单次执行时间："))
        self.label_beatTime.setText(_translate("MainWindow", "4132 ms"))
        self.label_text_runningNum.setText(_translate("MainWindow", "运行次数："))
        self.label_runningNum.setText(_translate("MainWindow", "0"))
        self.label_text_poseNum.setText(_translate("MainWindow", "位姿个数："))
        self.label_poseNum.setText(_translate("MainWindow", "0"))
        self.label_text_runningTime.setText(_translate("MainWindow", "累计运行时间："))
        self.label_runningTime.setText(_translate("MainWindow", "0ms"))
        self.pushButton_start.setText(_translate("MainWindow", "开始运行"))
        self.label_vision_2D.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">2D图像为空</span></p></body></html>"))
        self.pushButton_2DImage.setText(_translate("MainWindow", "2D图像"))
        self.pushButton_3DCloud.setText(_translate("MainWindow", "3D点云"))
        self.label_text_displayData.setText(_translate("MainWindow", "数据显示"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_setting.setTitle(_translate("MainWindow", "设置"))
        self.menu_function.setTitle(_translate("MainWindow", "功能"))
        self.menu_tools.setTitle(_translate("MainWindow", "工具"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助"))
        self.action_openFile.setText(_translate("MainWindow", "打开"))
        self.action_saveFile.setText(_translate("MainWindow", "保存"))
        self.action_systemSetting.setText(_translate("MainWindow", "系统设置 "))
        self.actionbanben.setText(_translate("MainWindow", "版本信息"))
        self.action_switchScene.setText(_translate("MainWindow", "切换场景"))
        self.action_switchLayout.setText(_translate("MainWindow", "切换布局"))
        self.action_loginAuthority.setText(_translate("MainWindow", "登录权限"))
        self.action_virtualKeyboard.setText(_translate("MainWindow", "虚拟键盘"))
        self.action_communicationTest.setText(_translate("MainWindow", "通信测试助手"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_docs.setText(_translate("MainWindow", "文档"))
