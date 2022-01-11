# 用于软件界面可视化

import logging
from PyQt5.QtGui import QColor, QTextCharFormat, QFont
from util.log_tool.log import logs

def ansiColor(code):
    r = 170 if code & 1 else 0
    g = 170 if code & 2 else 0
    b = 170 if code & 4 else 0
    return QColor(r, g, b)

ResetFormat = 0
BoldText = 1
TextColorStart = 30
TextColorEnd = 37
RgbTextColor = 38
DefaultTextColor = 39
BackgroundColorStart = 40
BackgroundColorEnd = 47
RgbBackgroundColor = 48
DefaultBackgroundColor = 49

LOG_CODE_DEBUG = 0
LOG_CODE_INFO = 36
LOG_CODE_WARNING = 33
LOG_CODE_ERROR = 31

logging_to_log_code = {
    logging.DEBUG: LOG_CODE_DEBUG,
    logging.INFO: LOG_CODE_INFO,
    logging.WARNING: LOG_CODE_WARNING,
    logging.ERROR: LOG_CODE_ERROR,
}

log_code_to_name = {
    LOG_CODE_DEBUG: "DEBUG",
    LOG_CODE_INFO: "INFO",
    LOG_CODE_WARNING: "WARNING",
    LOG_CODE_ERROR: "ERROR"
}


# log_color_code = {
#     logs.debug: LOG_CODE_DEBUG,
#     logs.info: LOG_CODE_INFO,
#     logs.warning: LOG_CODE_WARNING,
#     logs.error: LOG_CODE_ERROR,
# }

VALID_SEPARATORS = (",", ";", " ", ":", "|", "!", "/", "-", "+", "=", "%", "(", ")", "_")


# Hex转换器
def format_hex_bytes(src):
    text = ""
    for s in str(src).split("0x"):
        if s != "":
            s = s.zfill(2)
            text += (s + " ")
    return text

# Ascii码验证器
def check_ascii_character(chars) -> bool:
    for c in chars:
        if ord(c) > 255:
            return False
    return True