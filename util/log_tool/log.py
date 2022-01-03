import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time

from PyQt5.QtCore import QObject, pyqtSlot, Qt, pyqtSignal, QTranslator, QCoreApplication, QUrl
from util.generator import configObject

# 默认日志存储位置
default_log_dir = os.path.join(os.path.dirname(__file__), "..", "..", "logs")


# 颜色用于区分日志等级
COLORS = {
    'WARNING':  'aaaa00',
    'INFO':     '0000ff',
    'DEBUG':    '0000aa',
    'CRITICAL': 'aa00aa',
    'ERROR':    'aa0000'
}

class ColoredFormatter(logging.Formatter):
    """
    日志格式生成(可带颜色)
    颜色详情参阅COLORS字典
    """
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, fmt=msg, datefmt='%H:%M:%S')
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            record.levelname = '['+ levelname[0] + ']'
            record.color = COLORS[levelname] + ';">'
        return logging.Formatter.format(self, record)


class LoggingHandler(QObject, logging.Handler):
    """
    日志处理器生成
    """
    newLogging = pyqtSignal(int, str)

    def __init__(self, level=logging.NOTSET):
        QObject.__init__(self)
        logging.Handler.__init__(self, level=level)
        try:
            formatter = ColoredFormatter('%(asctime)s.%(msecs)03d %(levelname)s %(message)s') # 日志格式
            self.setFormatter(formatter)
        except IndexError:
            pass

    def emit(self, record):
        msg = self.format(record)
        self.newLogging.emit(record.levelno, msg)


def create_file_logger(log_dir=default_log_dir, log_level = logging.DEBUG, file_name_prefix="longer_", name=None):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    filename = os.path.join(log_dir, file_name_prefix) + time.strftime("%Y-%m-%d") + ".html" # 以日期为单位分隔日志

    file_handler = TimedRotatingFileHandler(filename, when='D', interval=1,
                                   encoding="utf-8", backupCount=7)
    file_handler.file_name_prefix = file_name_prefix
    color_format = '<p style="margin-top:0px; margin-bottom:0px;font-family:serif;font-weight:bold;">' \
                   ' %(asctime)s.%(msecs)03d <span style=" color:#%(color)s%(levelname)s %(threadName)s %(filename)s' \
                   ' %(lineno)d: %(message)s</span></p>'
    color_formatter = ColoredFormatter(color_format)

    file_handler.setFormatter(color_formatter)

    logger.addHandler(file_handler)
    return logger



log_record = create_file_logger() # 用于写入文本
logs = logging.getLogger("longer_ui")

logs.setLevel(logging.INFO) # 生产模式默认使用这行
logs.setLevel(logging.DEBUG) # 管理员调试模式可使用这一行




# 获取项目根目录(已弃用)
# cur_path =  os.path.abspath(os.path.dirname(__file__)) # 获取当前目录
# root_path = cur_path[:cur_path.rindex(configObject.software_config.software_name)+len(configObject.software_config.software_name)] + "\\"
# logs = Logger(filename=root_path + configObject.log_config.log_save_path, level=configObject.log_config.log_save_level, fmt=configObject.log_config.log_format)

## 已弃用的日志类
# class Logger(object):
#     level_relations = {
#         'debug':logging.DEBUG,
#         'info':logging.INFO,
#         'warning':logging.WARNING,
#         'error':logging.ERROR,
#         'crit':logging.CRITICAL
#     } # 日志级别关系映射
#
#     def __init__(self, filename, logname='root', level='info', when='D', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
#         filename = filename + "\\" + time.strftime("%Y-%m-%d") + "\\" # 以日期为单位分隔日志
#         self.logger = logging.getLogger(logname)
#         format_str = logging.Formatter(fmt) # 设置日志格式
#         self.logger.setLevel(self.level_relations.get(level)) # 设置日志级别
#         sh = logging.StreamHandler() # 往屏幕上输出
#         sh.setFormatter(format_str) # 设置屏幕上显示的格式
#         th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
#         # 实例化TimedRotatingFileHandler
#         # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
#         # S 秒
#         # M 分
#         # H 小时、
#         # D 天、
#         # W 每星期（interval==0时代表星期一）
#         # midnight 每天凌晨
#         th.setFormatter(format_str) # 设置文件里写入的格式
#         self.logger.addHandler(sh)  # 把对象加到logger里
#         self.logger.addHandler(th)

## 已弃用的测试用例
# if __name__ == "__main__":
#     logs = Logger('../logs/all.log_tool',level='debug')
#     logs.logger.debug('debug')
#     logs.logger.info('info')
#     logs.logger.warning('警告')
#     logs.logger.error('报错')
#     logs.logger.critical('严重')
#     Logger('../logs/error.log_tool', level='error').logger.error('error')