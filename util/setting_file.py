import os
from logging.handlers import SocketHandler
from PyQt5.QtCore import QSettings

# 可运行此文件通过print查看路径
monitor_settings_address = "127.0.0.1:45454"
logger_handler_address = SocketHandler('127.0.0.1', 19996)

longer_path = os.path.join(os.path.expanduser("~"), r"AppData\Roaming\Longer")
# print(longer_path)
longer_gui_path = os.path.join(longer_path, "LongerGUI")
# print(longer_gui_path)
try:
    if os.path.exists(longer_path):
        if not os.path.exists(longer_gui_path):
            os.mkdir(longer_gui_path)
    else:
        os.mkdir(longer_path)
        os.mkdir(longer_gui_path)
except FileNotFoundError:
    pass
setting_file_path = os.path.join(longer_gui_path, "setting.json")
print(setting_file_path)
sys_settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "Longer/LongerGUI")
# print(sys_settings)
generator_config_file = os.path.join(longer_gui_path, "generate_adapter_config.json")
# adapter code path
# adapter_dir = os.path.join(os.path.dirname(__file__), "..", "adapter")
# print(adapter_dir)

