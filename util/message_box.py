from PyQt5.QtWidgets import QMessageBox
from util.translations import _translate


def information_box(parent, title="", text=""):
    """
    doc: 提示框(普通信息)
    :param parent: 父类(通常填self)
    :param title: 弹窗标题
    :param text: 弹窗内容
    :return: None
    """
    title = _translate("Logger", "Hint") if title == "" else title
    return QMessageBox.information(parent, title, text)


def warning_box(parent, title="", text=""):
    """
    doc: 提示框(警告)
    :param parent: 父类(通常填self)
    :param title: 弹窗标题
    :param text: 弹窗内容
    :return: None
    """
    title = _translate("Logger", "Warning") if title == "" else title
    return QMessageBox.warning(parent, title, text)


def warning_box_yes_no(parent, title="", text=""):
    """
    doc: 提示框(警告[是否选择型])
    :param parent: 父类(通常填self)
    :param title: 弹窗标题
    :param text: 弹窗内容
    :return: None
    """
    title = _translate("Logger", "Warning") if title == "" else title
    return QMessageBox.warning(parent, title, text, QMessageBox.Yes | QMessageBox.No)


def critical_box(parent, title="", text=""):
    """
    doc: 提示框(错误)
    :param parent: 父类(通常填self)
    :param title: 弹窗标题
    :param text: 弹窗内容
    :return: None
    """
    title = _translate("Logger", "Error") if title == "" else title
    return QMessageBox.critical(parent, title, text)
