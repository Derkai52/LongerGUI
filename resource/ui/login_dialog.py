from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, Qt

from resource.ui.pyqt_generated.UI_LoginDialog import Ui_LoginDialog
from util.message_box import critical_box, information_box
from util.setting_file import sys_settings
from util import json_keys as jk
import re


class UserType(object):
    Operator = 0
    Admin = 1


class LoginDialog(QDialog):
    def __init__(self, in_modifying):
        super().__init__()
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.setWindowFlags((self.windowFlags() & ~Qt.WindowContextHelpButtonHint))
        self.admin_pwd = sys_settings.value(jk.pwd, "longer") # 设置默认管理员密码
        self.user_type = int(sys_settings.value(jk.user_type, 0))
        self.in_modifying = in_modifying
        self.modify_flag = False # 是否修改
        self.set_modifying(in_modifying)


    @pyqtSlot(int)
    def on_comboBox_userType_currentIndexChanged(self, index): # 此处对两种页面的组件状态做了强制初始化
        if index == 0:
            self.ui.pushButton_modifyPwd.setVisible(False)
            self.ui.label_password.setVisible(False)
            self.ui.lineEdit_password.setVisible(False)
            self.ui.label_newpassword.setVisible(False)
            self.ui.lineEdit_newpassword.setVisible(False)
            self.ui.pushButton_signIn.setText("登录")
            self.ui.lineEdit_password.clear()
            self.ui.lineEdit_newpassword.clear()
        if index == 1:
            self.ui.label_password.setVisible(True)
            self.ui.lineEdit_password.setVisible(True)
            self.ui.pushButton_modifyPwd.setVisible(True)
            self.ui.label_newpassword.setVisible(False)
            self.ui.lineEdit_newpassword.setVisible(False)
            self.ui.pushButton_signIn.setText("登录")
            self.ui.lineEdit_password.clear()
            self.ui.lineEdit_newpassword.clear()
            self.modify_flag = False  # 是否修改

        # self.ui.pushButton_signIn

    @pyqtSlot()
    def on_pushButton_signIn_clicked(self):
        if self.is_operator():
            self.sign_in()
            self.accept()
            return

        if not self.modify_flag: # 不修改
            print("不修改")
            if self.ui.lineEdit_password.text() and self.ui.lineEdit_password.text() == self.admin_pwd:
                self.sign_in()
                self.accept()
            elif not self.ui.lineEdit_password.text():
                information_box(self, text=self.tr("请输入密码"))
            else:
                if self.modify_flag:
                    information_box(self, text=self.tr("请先输入初始密码"))
                else:
                    critical_box(self, text=self.tr("密码错误"))
        else: # 修改
            if not self.ui.lineEdit_password.text():
                critical_box(self, text=self.tr("请先输入旧密码"))
                return
            if self.ui.lineEdit_password.text() != self.admin_pwd:
                critical_box(self, text=self.tr("旧密码错误"))
                return
            if not self.ui.lineEdit_newpassword.text():
                information_box(self, text=self.tr("请输入新密码"))
                return

            if self.update_pwd():
                self.accept()


    @pyqtSlot()
    def on_pushButton_modifyPwd_clicked(self):
        self.modify_flag = True
        self.ui.label_password.setText("旧密码:")
        self.ui.label_newpassword.setVisible(True)
        self.ui.lineEdit_newpassword.setVisible(True)
        self.ui.pushButton_signIn.setText("修改密码")
        self.ui.pushButton_modifyPwd.setVisible(False)
        self.ui.lineEdit_password.clear()





    def sign_in(self):
        self.user_type = self.ui.comboBox_userType.currentIndex()
        sys_settings.setValue(jk.user_type, self.user_type)

    def update_pwd(self):
        self.temp_pwd = self.ui.lineEdit_newpassword.text() # 使用一个临时变量去存储当前键入的值
        for i in self.temp_pwd:
            if (u'\u4e00' <= i <= u'\u9fff') or i == " " : # 检查字符串是否包含中文和空格
                critical_box(self, text=self.tr("密码不能包含中文字符或空格！"))
                self.ui.lineEdit_newpassword.clear() # 输入错误后清空输入栏
                return False
        sys_settings.setValue(jk.pwd, self.temp_pwd)
        information_box(self, text=self.tr("密码修改成功！"))
        return True

    def is_operator(self):
        return not self.is_admin()

    def is_admin(self):
        return self.ui.comboBox_userType.currentIndex() == UserType.Admin

    def set_modifying(self, in_modifying):
        self.in_modifying = in_modifying
        self.ui.lineEdit_password.setVisible(not in_modifying)
        self.ui.label_password.setVisible(not in_modifying)
        self.ui.lineEdit_newpassword.setVisible(not in_modifying)
        self.ui.label_newpassword.setVisible(not in_modifying)
        self.ui.pushButton_modifyPwd.setVisible(not in_modifying)
        # self.ui.pushButton_signIn.setVisible(not in_modifying)
        self.ui.comboBox_userType.setEnabled(in_modifying)
        self.ui.comboBox_userType.setCurrentIndex(UserType.Operator)
        self.setWindowTitle(self.tr("用户登录"))