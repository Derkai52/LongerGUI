# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Settings.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(898, 648)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/机器人.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Setting.setWindowIcon(icon)
        Setting.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.gridLayout = QtWidgets.QGridLayout(Setting)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Setting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(204, 78))
        self.tabWidget.setMaximumSize(QtCore.QSize(854, 576))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setStyleSheet("font: 12pt \"Arial\";")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.software = QtWidgets.QWidget()
        self.software.setObjectName("software")
        self.layoutWidget = QtWidgets.QWidget(self.software)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ProjectName = QtWidgets.QLabel(self.layoutWidget)
        self.label_ProjectName.setObjectName("label_ProjectName")
        self.horizontalLayout.addWidget(self.label_ProjectName)
        self.lineEdit_ProjectName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ProjectName.setObjectName("lineEdit_ProjectName")
        self.horizontalLayout.addWidget(self.lineEdit_ProjectName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_version = QtWidgets.QLabel(self.layoutWidget)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_2.addWidget(self.label_version)
        self.lineEdit_version = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_version.setObjectName("lineEdit_version")
        self.horizontalLayout_2.addWidget(self.lineEdit_version)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ProjectPath = QtWidgets.QLabel(self.layoutWidget)
        self.label_ProjectPath.setObjectName("label_ProjectPath")
        self.horizontalLayout_3.addWidget(self.label_ProjectPath)
        self.lineEdit_ProjectPath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ProjectPath.setObjectName("lineEdit_ProjectPath")
        self.horizontalLayout_3.addWidget(self.lineEdit_ProjectPath)
        self.toolButton_ProjectPath = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_ProjectPath.setObjectName("toolButton_ProjectPath")
        self.horizontalLayout_3.addWidget(self.toolButton_ProjectPath)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.software, "")
        self.communication = QtWidgets.QWidget()
        self.communication.setObjectName("communication")
        self.layoutWidget1 = QtWidgets.QWidget(self.communication)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 741, 551))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_MechIP = QtWidgets.QLabel(self.layoutWidget1)
        self.label_MechIP.setObjectName("label_MechIP")
        self.horizontalLayout_4.addWidget(self.label_MechIP)
        self.lineEdit_MechIP = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_MechIP.setObjectName("lineEdit_MechIP")
        self.horizontalLayout_4.addWidget(self.lineEdit_MechIP)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_MechPort = QtWidgets.QLabel(self.layoutWidget1)
        self.label_MechPort.setObjectName("label_MechPort")
        self.horizontalLayout_5.addWidget(self.label_MechPort)
        self.lineEdit_MechPort = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_MechPort.setObjectName("lineEdit_MechPort")
        self.horizontalLayout_5.addWidget(self.lineEdit_MechPort)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_RobotIP = QtWidgets.QLabel(self.layoutWidget1)
        self.label_RobotIP.setObjectName("label_RobotIP")
        self.horizontalLayout_6.addWidget(self.label_RobotIP)
        self.lineEdit_RobotIP = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_RobotIP.setObjectName("lineEdit_RobotIP")
        self.horizontalLayout_6.addWidget(self.lineEdit_RobotIP)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_RobotPort = QtWidgets.QLabel(self.layoutWidget1)
        self.label_RobotPort.setObjectName("label_RobotPort")
        self.horizontalLayout_7.addWidget(self.label_RobotPort)
        self.lineEdit_RobotPort = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_RobotPort.setObjectName("lineEdit_RobotPort")
        self.horizontalLayout_7.addWidget(self.lineEdit_RobotPort)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_RobotVendor = QtWidgets.QLabel(self.layoutWidget1)
        self.label_RobotVendor.setObjectName("label_RobotVendor")
        self.horizontalLayout_8.addWidget(self.label_RobotVendor)
        self.lineEdit_RobotVendor = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_RobotVendor.setObjectName("lineEdit_RobotVendor")
        self.horizontalLayout_8.addWidget(self.lineEdit_RobotVendor)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_22.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(93, 4, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(self.layoutWidget1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_22.addWidget(self.line)
        spacerItem3 = QtWidgets.QSpacerItem(119, 0, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_ChooseASCIICode = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ChooseASCIICode.setObjectName("label_ChooseASCIICode")
        self.horizontalLayout_21.addWidget(self.label_ChooseASCIICode)
        self.comboBox_ChooseASCIICode = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_ChooseASCIICode.setObjectName("comboBox_ChooseASCIICode")
        self.comboBox_ChooseASCIICode.addItem("")
        self.comboBox_ChooseASCIICode.addItem("")
        self.horizontalLayout_21.addWidget(self.comboBox_ChooseASCIICode)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_ClientCommandLength = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ClientCommandLength.setObjectName("label_ClientCommandLength")
        self.horizontalLayout_19.addWidget(self.label_ClientCommandLength)
        self.spinBox_ClientCommandLength = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_ClientCommandLength.setObjectName("spinBox_ClientCommandLength")
        self.horizontalLayout_19.addWidget(self.spinBox_ClientCommandLength)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_MechCommandLength = QtWidgets.QLabel(self.layoutWidget1)
        self.label_MechCommandLength.setObjectName("label_MechCommandLength")
        self.horizontalLayout_18.addWidget(self.label_MechCommandLength)
        self.spinBox_MechCommandLength = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_MechCommandLength.setObjectName("spinBox_MechCommandLength")
        self.horizontalLayout_18.addWidget(self.spinBox_MechCommandLength)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_DataReceivingLength = QtWidgets.QLabel(self.layoutWidget1)
        self.label_DataReceivingLength.setObjectName("label_DataReceivingLength")
        self.horizontalLayout_17.addWidget(self.label_DataReceivingLength)
        self.spinBox_DataReceivingLength = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_DataReceivingLength.setObjectName("spinBox_DataReceivingLength")
        self.horizontalLayout_17.addWidget(self.spinBox_DataReceivingLength)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_HexSide = QtWidgets.QLabel(self.layoutWidget1)
        self.label_HexSide.setObjectName("label_HexSide")
        self.horizontalLayout_20.addWidget(self.label_HexSide)
        self.comboBox_HexSide = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_HexSide.setObjectName("comboBox_HexSide")
        self.comboBox_HexSide.addItem("")
        self.comboBox_HexSide.addItem("")
        self.horizontalLayout_20.addWidget(self.comboBox_HexSide)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_22.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.communication, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.layoutWidget2 = QtWidgets.QWidget(self.log)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 21, 829, 592))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem4 = QtWidgets.QSpacerItem(69, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem4)
        self.label_LogSavePath = QtWidgets.QLabel(self.layoutWidget2)
        self.label_LogSavePath.setObjectName("label_LogSavePath")
        self.horizontalLayout_26.addWidget(self.label_LogSavePath)
        self.lineEdit_LogSavePath = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_LogSavePath.setObjectName("lineEdit_LogSavePath")
        self.horizontalLayout_26.addWidget(self.lineEdit_LogSavePath)
        self.toolButton_LogSavePath = QtWidgets.QToolButton(self.layoutWidget2)
        self.toolButton_LogSavePath.setObjectName("toolButton_LogSavePath")
        self.horizontalLayout_26.addWidget(self.toolButton_LogSavePath)
        self.verticalLayout_5.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem5 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem5)
        self.label_LogLevel = QtWidgets.QLabel(self.layoutWidget2)
        self.label_LogLevel.setObjectName("label_LogLevel")
        self.horizontalLayout_25.addWidget(self.label_LogLevel)
        self.lineEdit_LogLevel = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_LogLevel.setObjectName("lineEdit_LogLevel")
        self.horizontalLayout_25.addWidget(self.lineEdit_LogLevel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem6 = QtWidgets.QSpacerItem(53, 22, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem6)
        self.label_BackupFileNumber = QtWidgets.QLabel(self.layoutWidget2)
        self.label_BackupFileNumber.setMaximumSize(QtCore.QSize(100, 16777211))
        self.label_BackupFileNumber.setObjectName("label_BackupFileNumber")
        self.horizontalLayout_24.addWidget(self.label_BackupFileNumber)
        self.spinBox_BackupFileNumber = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinBox_BackupFileNumber.setObjectName("spinBox_BackupFileNumber")
        self.horizontalLayout_24.addWidget(self.spinBox_BackupFileNumber)
        self.verticalLayout_5.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem7 = QtWidgets.QSpacerItem(81, 34, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem7)
        self.label_LogFormat = QtWidgets.QLabel(self.layoutWidget2)
        self.label_LogFormat.setMinimumSize(QtCore.QSize(60, 0))
        self.label_LogFormat.setObjectName("label_LogFormat")
        self.horizontalLayout_23.addWidget(self.label_LogFormat, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.textBrowser_LogFormat = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.textBrowser_LogFormat.setMinimumSize(QtCore.QSize(661, 0))
        self.textBrowser_LogFormat.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser_LogFormat.setObjectName("textBrowser_LogFormat")
        self.horizontalLayout_23.addWidget(self.textBrowser_LogFormat)
        self.verticalLayout_5.addLayout(self.horizontalLayout_23)
        spacerItem8 = QtWidgets.QSpacerItem(80, 379, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem8)
        self.tabWidget.addTab(self.log, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(Setting)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Form"))
        self.label_ProjectName.setText(_translate("Setting", "项目名称："))
        self.label_version.setText(_translate("Setting", "版    本："))
        self.label_ProjectPath.setText(_translate("Setting", "项目路径："))
        self.toolButton_ProjectPath.setText(_translate("Setting", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.software), _translate("Setting", "软件"))
        self.label_MechIP.setText(_translate("Setting", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">mech_interface Ip：</span></p></body></html>"))
        self.label_MechPort.setText(_translate("Setting", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">mech_interface Port：</span></p></body></html>"))
        self.label_RobotIP.setText(_translate("Setting", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">robot_server Ip：</span></p></body></html>"))
        self.label_RobotPort.setText(_translate("Setting", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">robot_server Port：</span></p></body></html>"))
        self.label_RobotVendor.setText(_translate("Setting", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">robot_vendor：</span></p></body></html>"))
        self.label_ChooseASCIICode.setText(_translate("Setting", "<html><head/><body><p align=\"right\">选择ASCII码：</p></body></html>"))
        self.comboBox_ChooseASCIICode.setItemText(0, _translate("Setting", "TRUE"))
        self.comboBox_ChooseASCIICode.setItemText(1, _translate("Setting", "FALSE"))
        self.label_ClientCommandLength.setText(_translate("Setting", "<html><head/><body><p align=\"right\">客户端命令长度：</p></body></html>"))
        self.label_MechCommandLength.setText(_translate("Setting", "<html><head/><body><p align=\"right\">Mech端命令长度：</p></body></html>"))
        self.label_DataReceivingLength.setText(_translate("Setting", "<html><head/><body><p align=\"right\">数据接收长度：</p></body></html>"))
        self.label_HexSide.setText(_translate("Setting", "<html><head/><body><p align=\"right\">HEX端：</p></body></html>"))
        self.comboBox_HexSide.setItemText(0, _translate("Setting", "大端"))
        self.comboBox_HexSide.setItemText(1, _translate("Setting", "小端"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.communication), _translate("Setting", "通信"))
        self.label_LogSavePath.setText(_translate("Setting", "<html><head/><body><p align=\"right\">日志保存路径：</p></body></html>"))
        self.toolButton_LogSavePath.setText(_translate("Setting", "..."))
        self.label_LogLevel.setText(_translate("Setting", "<html><head/><body><p align=\"right\">日志等级：</p></body></html>"))
        self.label_BackupFileNumber.setText(_translate("Setting", "<html><head/><body><p align=\"right\">备份文件个数：</p></body></html>"))
        self.label_LogFormat.setText(_translate("Setting", "日志格式："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("Setting", "日志"))
