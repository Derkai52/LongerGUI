# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_LoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(300, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        LoginDialog.setMinimumSize(QtCore.QSize(300, 180))
        LoginDialog.setMaximumSize(QtCore.QSize(300, 180))
        self.pushButton_signIn = QtWidgets.QPushButton(LoginDialog)
        self.pushButton_signIn.setGeometry(QtCore.QRect(20, 110, 261, 61))
        self.pushButton_signIn.setObjectName("pushButton_signIn")
        self.pushButton_modifyPwd = QtWidgets.QPushButton(LoginDialog)
        self.pushButton_modifyPwd.setGeometry(QtCore.QRect(210, 10, 75, 23))
        self.pushButton_modifyPwd.setObjectName("pushButton_modifyPwd")
        self.layoutWidget = QtWidgets.QWidget(LoginDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 181, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_newpassword = QtWidgets.QLabel(self.layoutWidget)
        self.label_newpassword.setObjectName("label_newpassword")
        self.horizontalLayout_3.addWidget(self.label_newpassword)
        self.lineEdit_newpassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_newpassword.setMaxLength(20)
        self.lineEdit_newpassword.setObjectName("lineEdit_newpassword")
        self.horizontalLayout_3.addWidget(self.lineEdit_newpassword)
        self.layoutWidget1 = QtWidgets.QWidget(LoginDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 181, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_userType = QtWidgets.QLabel(self.layoutWidget1)
        self.label_userType.setObjectName("label_userType")
        self.horizontalLayout.addWidget(self.label_userType)
        self.comboBox_userType = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_userType.setObjectName("comboBox_userType")
        self.comboBox_userType.addItem("")
        self.comboBox_userType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_userType)
        self.horizontalLayout.setStretch(1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(LoginDialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 40, 181, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(self.layoutWidget2)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_password.setMaxLength(20)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.comboBox_userType, self.lineEdit_password)
        LoginDialog.setTabOrder(self.lineEdit_password, self.pushButton_signIn)
        LoginDialog.setTabOrder(self.pushButton_signIn, self.pushButton_modifyPwd)
        LoginDialog.setTabOrder(self.pushButton_modifyPwd, self.lineEdit_newpassword)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "用户登录"))
        self.pushButton_signIn.setText(_translate("LoginDialog", "登录"))
        self.pushButton_modifyPwd.setText(_translate("LoginDialog", "修改密码"))
        self.label_newpassword.setText(_translate("LoginDialog", "新密码"))
        self.label_userType.setText(_translate("LoginDialog", "用户类型"))
        self.comboBox_userType.setCurrentText(_translate("LoginDialog", "操作员"))
        self.comboBox_userType.setItemText(0, _translate("LoginDialog", "操作员"))
        self.comboBox_userType.setItemText(1, _translate("LoginDialog", "管理员"))
        self.label_password.setText(_translate("LoginDialog", "密码"))
