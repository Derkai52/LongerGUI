from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal, QTranslator, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QAbstractItemView, QDialog, QAction, QMenu
from PyQt5.QtGui import QIcon, QFont, QPixmap, QCursor, QColor
from resource.ui.pyqt_generated.UI_Login_permission import Ui_LoginPermission




class LoginPermission(QDialog, Ui_LoginPermission): #这个窗口继承了用QtDesignner 绘制的窗口
    def __init__(self):
        super(LoginPermission,self).__init__()
        self.setupUi(self)