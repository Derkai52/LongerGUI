# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Login_permission.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPermission(object):
    def setupUi(self, LoginPermission):
        LoginPermission.setObjectName("LoginPermission")
        LoginPermission.resize(524, 312)
        LoginPermission.setMaximumSize(QtCore.QSize(524, 312))
        LoginPermission.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.line = QtWidgets.QFrame(LoginPermission)
        self.line.setGeometry(QtCore.QRect(120, 90, 2, 91))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(LoginPermission)
        self.line_2.setGeometry(QtCore.QRect(430, 90, 2, 91))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(LoginPermission)
        self.line_3.setGeometry(QtCore.QRect(120, 180, 311, 2))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(LoginPermission)
        self.line_4.setGeometry(QtCore.QRect(120, 90, 311, 2))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layoutWidget = QtWidgets.QWidget(LoginPermission)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 100, 291, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_ChoosePeopleLogin = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_ChoosePeopleLogin.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.comboBox_ChoosePeopleLogin.setObjectName("comboBox_ChoosePeopleLogin")
        self.comboBox_ChoosePeopleLogin.addItem("")
        self.comboBox_ChoosePeopleLogin.addItem("")
        self.verticalLayout.addWidget(self.comboBox_ChoosePeopleLogin)
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_PleaseInputPassWord = QtWidgets.QLabel(self.layoutWidget)
        self.label_PleaseInputPassWord.setObjectName("label_PleaseInputPassWord")
        self.horizontalLayout.addWidget(self.label_PleaseInputPassWord)
        self.lineEdit_PleaseInputPassWord = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_PleaseInputPassWord.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_PleaseInputPassWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PleaseInputPassWord.setObjectName("lineEdit_PleaseInputPassWord")
        self.horizontalLayout.addWidget(self.lineEdit_PleaseInputPassWord)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LoginPermission)
        QtCore.QMetaObject.connectSlotsByName(LoginPermission)

    def retranslateUi(self, LoginPermission):
        _translate = QtCore.QCoreApplication.translate
        LoginPermission.setWindowTitle(_translate("LoginPermission", "登录权限"))
        self.comboBox_ChoosePeopleLogin.setItemText(0, _translate("LoginPermission", "用户"))
        self.comboBox_ChoosePeopleLogin.setItemText(1, _translate("LoginPermission", "管理员"))
        self.label_PleaseInputPassWord.setText(_translate("LoginPermission", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">请输入密码：</span></p></body></html>"))
