import sys, cv2, time, os

from resource.ui.pyqt_generated.UI_MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog,QTabWidget, QMessageBox

from PyQt5.QtCore import pyqtSlot, QTimer, QThread, pyqtSignal, Qt, QUrl

from PyQt5.QtGui import QPixmap, QImage, QDesktopServices

from resource.ui.main_window import MainWindow




if __name__ == "__main__":

    # 数据初始化完成，载入界面
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())







# 预留接口，直接使用参数启动程序(已停止维护)
# print(sys.argv[1])
#     if len(sys.argv) == 2: # 从文件读取
#         config_path = sys.argv[1]
#         client = Hub(configPath=config_path)
#         client.run()
#     elif len(sys.argv) == 5: # 输入外参
#         client = Hub(serverIP=sys.argv[1], serverPort=sys.argv[2], connectIP=sys.argv[3], connectPort=sys.argv[4])
#         client.run()
#     else:
#         print("Please input config_tool.cfg path or connect information")
#         print("Client configPath")
#         print("Client serverIP serverPort connectIP connectPort")
