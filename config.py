################# 软件设置 ############################
project_name = "LongerGUI"
project_version = "1.0"

################# 通信设置 ############################
is_ascii = True # 是否为 ASCII 码
endian = "<" # Hex 格式用大端还是小端
len_client_msg = 56 # 客户端发送给 Mech-Interface 的命令长度(bytes)
len_mech_msg = 660 #  Mech-Interface 发送给客户端的命令长度(bytes)
robot_vendor = "ABB" # 机器人设备商名称

################# 日志设置 #############################
log_save_path = "logs" # 日志保存文件夹(路径相对于项目根目录)
log_save_level = "info" # 日志采集最低等级
log_backCount = 3 # 备份文件的最大个数
# log_when = "D" # 时间记录间隔
log_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' # 日志记录格式