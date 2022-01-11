"""
######################################################################

        __                                    ___        _____
       / /  ___  _ __   __ _  ___ _ __       / _ \/\ /\  \_   \
      / /  / _ \| '_ \ / _` |/ _ \ '__|____ / /_\/ / \ \  / /\/
     / /__| (_) | | | | (_| |  __/ | |_____/ /_\\\ \_/ /\/ /_
     \____/\___/|_| |_|\__, |\___|_|       \____/ \___/\____/
                       |___/

############ < Designed by Longer-developer in 2022 > ################

"""

import sys, cv2, time, os

from resource.ui.pyqt_generated.UI_MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog,QTabWidget, QMessageBox

from PyQt5.QtCore import pyqtSlot, QTimer, QThread, pyqtSignal, Qt, QUrl

from PyQt5.QtGui import QPixmap, QImage, QDesktopServices

from resource.ui.main_window import MainWindow



# 手动启动程序
if __name__ == "__main__":

    # 数据初始化完成，载入界面
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



# 预留接口，使用外部调用参数启动程序(暂未启用，预留程序外部调用接口)
# 请根据实际情况修改下面程序，因为这是配合好几个版本前的代码了
# if len(sys.argv) == 2: # 从文件读取
#     config_path = sys.argv[1]
#     client = Hub(configPath=config_path)
#     client.run()
# elif len(sys.argv) == 5: # 输入外参
#     client = Hub(serverIP=sys.argv[1], serverPort=sys.argv[2], connectIP=sys.argv[3], connectPort=sys.argv[4])
#     client.run()
# else:
#     print("Please input config_tool.cfg path or connect information")
#     print("Client configPath")
#     print("Client serverIP serverPort connectIP connectPort")
