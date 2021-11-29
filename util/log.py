import logging
from logging import handlers
import os
from config import *
import time

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    } # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3, fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        filename = filename + "\\" + time.strftime("%Y-%m-%d") + "\\" # 以日期为单位分隔日志
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt) # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level)) # 设置日志级别
        sh = logging.StreamHandler() # 往屏幕上输出
        sh.setFormatter(format_str) # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str) # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)



# 获取当前目录
cur_path =  os.path.abspath(os.path.dirname(__file__))
# 获取项目根目录
root_path = cur_path[:cur_path.rindex(project_name)+len(project_name)] + "\\"
logs = Logger(filename=root_path + log_save_path, level=log_save_level) # TODO: 从配置文件读取设置，并添加自动路径功能


## 测试用
# if __name__ == "__main__":
#     logs = Logger('../logs/all.log',level='debug')
#     logs.logger.debug('debug')
#     logs.logger.info('info')
#     logs.logger.warning('警告')
#     logs.logger.error('报错')
#     logs.logger.critical('严重')
#     Logger('../logs/error.log', level='error').logger.error('error')