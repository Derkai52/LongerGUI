# 本文件通过维护一个消息事件表，用于解析消息事件

from struct import pack, unpack
from communication import commands as cmds
from event.messages import *
from util.log_tool.log import logs
from util.generator import configObject

# 读取配置表信息
is_ascii = configObject.mech_communication_config.is_ascii
endian = configObject.mech_communication_config.endian
len_mech_msg = configObject.mech_communication_config.len_mech_msg
len_client_msg = configObject.mech_communication_config.len_client_msg
robot_vendor = configObject.robot_communication_config.robot_vendor



###################### 格式解包与打包 #######################
def unpack_ascii_params(*args, **kwargs):
    """
    doc: ascii信息解包
    :param args: 传入数据
    :param kwargs: 预留位(暂未启用)
    :return: 由元素组成的列表
    """
    if isinstance(args[0], bytes):
        str_list = filter(None, args[0].decode().split(','))
        return [int(float(i)) if i and float(i).is_integer() else float(i) for i in str_list]
    return args


def pack_ascii_params(*args, **kwargs):
    """
    doc: ascii信息打包
    :param args: 传入数据
    :param kwargs: 预留位(暂未启用)
    :return: 字符串
    """
    return (','.join([str(i) for i in args]) + ',').encode(encoding='utf-8')


def unpack_hex_params(*args, **kwargs):
    """
    doc: hex信息解包
    :param args: 传入数据
    :param kwargs: 预留位(暂未启用)
    :return: 由元素组成的元组
    """
    return unpack('{}'.format(endian) + kwargs.get('fmt', ''), *args)


def pack_hex_params(*args, **kwargs):
    """
    doc: hex信息打包
    :param args: 传入数据
    :param kwargs: 预留位(暂未启用)
    :return: bytes容器
    """
    return pack('{}'.format(endian) + kwargs.get('fmt', ''), *args)


if is_ascii:
    pack_params = pack_ascii_params
    unpack_params = unpack_ascii_params
else:
    pack_params = pack_hex_params
    unpack_params = unpack_hex_params

######################## 可视化展示 #######################
# zzz = pack_ascii_params(*a)
# xxx, *ccc = unpack_ascii_params(zzz)
# xxx = unpack_ascii_params(*ccc)

# 用于UI界面提示用户进行功能选择
def command_descs():
    """
    doc: 指令代码描述提示
    """
    return ("{}: Run Mech-Vision(will not include poses in this command's ack)".format(cmds.RUN_VISION),
            "{}: Get Mech-Vision poses".format(cmds.GET_VISION_DATA),
            "{}: Switch match models in Mech-Vision".format(cmds.SWITCH_MODEL),
            "{}: Run Mech-Viz(will not include poses in this command's ack)".format(cmds.RUN_VIZ),
            "{}: Stop Mech-Viz".format(cmds.STOP_VIZ),
            "{}: Set branch".format(cmds.SET_BRANCH),
            "{}: Set index of Index-like Move in Mech-Viz".format(cmds.SET_INDEX),
            "{}: Get Mech-Viz poses".format(cmds.GET_VIZ_DATA),
            "{}: Get DO list(in sucker for multi pick)".format(cmds.GET_DO_LIST),
            "{}: Set object(e.g. box) sizes".format(cmds.SET_BOX_SIZE),
            "{}: Set pose to Outer Move in Mech-Viz".format(cmds.SET_OUTER_POSE),
            "{}: Calibrate the Mech-Eye camera".format(cmds.GET_CALIBRATION_DATA),
            "{}: Get the service statuses".format(cmds.GET_STATUSES),
            )


def params_descs():
    """
    doc: 指令代码描述提示
    """
    return {cmds.RUN_VISION: """Project number-a positive integer; Count of poses-a positive integer(0 is get all poses); Pose or jps by robot(None)-0, (Jps)-1, (Pose)-2;"""
                             """ Pose-xyzABC(unit is mm and degree), Jps-j1~j6(unit is degree)
                                    For example: 1,1,1,-490.000,0,539.000,-90.000,90.000,180.000""",
            cmds.GET_VISION_DATA: """Project number-a positive integer; 
                                    For example: 1""",
            cmds.SWITCH_MODEL: """Project number-a positive integer; Workpiece number-a positive integer
                                    For example: 2,1""",
            cmds.RUN_VIZ: """Pose or jps by robot(None)-0, (Jps)-1, (Pose)-2; Pose-xyzABC(unit is mm and degree), Jps-j1~j6(unit is degree)
                                    For example: 1,-490.000,0,539.000,-90.000,90.000,180.000""",
            cmds.STOP_VIZ: """None params""",
            cmds.SET_BRANCH: """Branch number-a positive integer; Out port number-a positive integer
                                    For example: 1,3""",
            cmds.SET_INDEX: """Index Move number-a positive integer; index number-a positive integer
                                    For example: 1,3""",
            cmds.GET_VIZ_DATA: """Point type want to get(JPS)-1, (Pose)-2
                                    For example: 1""",
            cmds.GET_DO_LIST: """None params""",
            cmds.SET_BOX_SIZE: """sizes-length/width/height(unit is mm)
                                    For example: 1,100.0,200.0,300.0""",
            cmds.SET_OUTER_POSE: """Pose-xyzABC(unit is mm and degree)
                                    For example: -490.000,0,539.000,-90.000,90.000,180.000""",
            cmds.GET_CALIBRATION_DATA: """Move finished-1, Move failed-2; Robot's current pose(unit is mm and degree); Robot's current jps(unit is degree)
                                    For example: 1,-490.000,0,539.000,-90.000,90.000,180.000,-85.000,-90.000,-66.000,-90.000,0,0""",
            cmds.GET_STATUSES: """None params""",}

########################## 指令参数生成 #######################
def run_vision(params):
    """
    doc: 运行Vision
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) not in (3, 9):
        print("指令参数长度错误！Params missing!")
        return
    if params[2] == "0":
        params = list(params)[:3] + [0] * 6
    else:
        if len(params) != 9:
            print("Pose or JPS missing!")
            return
    return pack_params(int(params[0]), int(params[1]), int(params[2]), *([float(i) for i in params[3:]]), fmt="3i6f")


def get_viz_vision_data(params):
    """
    doc: 获得Viz或Vision的结果
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) != 1:
        print("Params missing!")
        return
    return pack_params(int(params[0]), fmt="i")


def switch_model_set_branch_index(params):
    """
    doc: 切换Vision配方/Viz设置Branch分支/Viz设置Index
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) != 2:
        print("Params missing!")
        return
    return pack_params(int(params[0]), int(params[1]), fmt="2i")


def run_viz(params):
    """
    doc: 运行Viz
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) not in (1, 7):
        print("Params missing!")
        return
    if params[0] == "0":
        params = [params[0]] + [0] * 6
    else:
        if len(params) != 7:
            print("Pose or JPS missing!")
            return
    return pack_params(int(params[0]), *([float(i) for i in params[1:]]), fmt="{}i6f")


def set_box_size(params):
    """
    doc: 外部传入箱子尺寸
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) != 4:
        print("Params missing!")
        return
    return pack_params(int(params[0]), *([float(i) for i in params[1:]]), fmt="i3f")


def set_outer_pose(params):
    """
    doc: 外部传入位姿(用于Out Move)
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) != 6:
        print("Params missing!")
        return
    return pack_params(*[float(i) for i in params], fmt="6f")


def pack_calibrate_params(params):
    """
    doc: 打包相机标定参数
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) != 13:
        print("Params missing!")
        return
    return pack_params(int(params[0]), *([float(i) for i in params[1:]]), fmt="i12f")


########################## 指令生成处理表 #####################
command_func_dict = {cmds.RUN_VISION: run_vision,
                     cmds.GET_VISION_DATA: get_viz_vision_data,
                     cmds.SWITCH_MODEL: switch_model_set_branch_index,
                     cmds.RUN_VIZ: run_viz,
                     cmds.SET_BRANCH: switch_model_set_branch_index,
                     cmds.SET_INDEX: switch_model_set_branch_index,
                     cmds.GET_VIZ_DATA: get_viz_vision_data,
                     cmds.SET_BOX_SIZE: set_box_size,
                     cmds.SET_OUTER_POSE: set_outer_pose,
                     cmds.GET_CALIBRATION_DATA: pack_calibrate_params}


def send_msg(client, msg):
    """
    doc: 发送消息(支持 ASCII 和 Hex)
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    if not is_ascii:
        if robot_vendor and robot_vendor.startswith("KUKA"):
            msg += b"\x00" * (len_mech_msg - len(msg))
        else:
            msg += b"\x00" * (len_client_msg - len(msg))
    client.send(msg)



from PyQt5.QtCore import QObject, pyqtSignal
class DisplayMainWindow(QObject):
    """
    用于窗口数据可视化的类
    """
    signal_pose = pyqtSignal(str)
    signal_runningTime = pyqtSignal(str)
    signal_runningNum = pyqtSignal(str)
    signal_beatTime = pyqtSignal(str)
    signal_communiteStatus = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)

        try:
            pass
            # self.newLogging.connect(calls)
        except IndexError:
            pass

    # 发送位姿点信息
    def pose_emit(self, pose_num):
        self.signal_pose.emit(pose_num)

    # 发送累计运行时间信息
    def runningtime_emit(self, runningtime):
        self.signal_runningTime.emit(runningtime)

    # 发送单词执行时间信息
    def beattime_emit(self, beattime):
        self.signal_beatTime.emit(beattime)

    # 发送运行次数信息
    def runningnum_emit(self, runningnum):
        self.signal_runningNum.emit(runningnum)

    # 发送通讯状态信息
    def communitestatus_emit(self, communitestatus):
        self.signal_communiteStatus.emit(communitestatus)


display_signal = DisplayMainWindow() # 自定义信号-槽函数类实例化






def parse_mech_msg(recv_cmds):
    """
    doc: 对Mech发送过来的信息进行事件处理
    :param recv_cmds: 待处理的Mech信息
    :return: Mech发送过来的信息
    """

    # 解析通讯消息
    try:
        recv_cmd, status_code = unpack_params(recv_cmds[:8], fmt="2i")
        print("\n从Mech接收的状态码={}, 事件: {}".format(status_code, event_logging(status_code)))
    except Exception:
        logs.error("接收消息解析错误:{}".format(recv_cmds))
        return

    # 获取Vision/Viz结果
    if recv_cmd in (cmds.GET_VISION_DATA, cmds.GET_VIZ_DATA) and status_code in (VISION_HAS_POSES, VIZ_FINISHED):
        recv_finished, point_count, *visual_move_position = unpack_params(recv_cmds[8:], fmt="3i")
        print("Recv not finish, you can continue to get data using same command" if recv_finished == 0 else "Recv finished")
        print("Point count={}".format(point_count))
        # 获取Viz结果
        if recv_cmd == cmds.GET_VIZ_DATA:
            print("Visual move position is", visual_move_position)
        poses_labels_speeds = unpack_params(recv_cmds[20:], fmt="6fii" * point_count)
        print(poses_labels_speeds)

        display_signal.pose_emit(str(point_count)) # 发送


        for i in range(point_count):
            print("Pose", i+1, ":", poses_labels_speeds[i*8:i*8+6], "Label:", poses_labels_speeds[i*8+6], "Speed:", poses_labels_speeds[i*8+7])

    # 获取相机标定点
    elif recv_cmd == cmds.GET_CALIBRATION_DATA and status_code == VISION_SEND_CALIBRATION_POINT_OK:
        points = unpack_params(recv_cmds[8:], fmt="i12f")
        print("Calibrate point: Pose=[{}], Jps=[{}]".format(points[1:7], points[7:]))
        if points[0] == 1:
            print("Calibration finished!")

    # 获取DO列表(吸盘分区多抓)
    elif recv_cmd == cmds.GET_DO_LIST:
        do_list = unpack_params(recv_cmds[8:], fmt="64i")
        print("Available do:", do_list[0:64 - do_list.count(-1)])
        print("Do list={}".format(do_list))

    return recv_cmds


def parsing_send_msg(sendmsg):
    """
    doc: 拆解待发送消息获得 指令代码和参数
    eg:拆解消息: '101,1,1,1,-490.000,0,539.000,-90.000,90.000,180.000'
    指令代码: '101'         参数: '1,1,1,-490.000,0,539.000,-90.000,90.000,180.000'
    :param sendmsg:
    :return: cmd: 指令代码  params:参数
    """
    # TODO:Warning 此处分解可能因为格式更改导致解法失效，可以考虑改为正则解析
    msg_temp = list(map(lambda x: int(float(x)), list(sendmsg.split(","))))  # 将传入的字符串转化为元素为数字的列表  eg. "101,1,1.23" -> [101,1,1.23]
    cmd = msg_temp[0]  # 获取指令代码
    indexnum = sendmsg.find(str(cmd)) + len(str(cmd)) + len(",")  # 字符串匹配获取第一个匹配项的第一个下标，加上匹配项长度，再加上分隔符"," 的长度，此时才可以获得后面的下标
    params = sendmsg[indexnum:]  # 获取参数
    return cmd, params






def msg_process(socket_object, msg, funcFlag):
    """
    doc: 对输入的信息进行处理，转化为可用的信息(注意，此函数已被多线程调用，请勿在未加锁下使用全局变量，)
    :param socket_object: socket套接字对象
    :param msg: 待处理的信息
    :param funcFlag: 1:信息处理并发送 2:信息处理并接受
    :return: funcFlag=1:None  funcFlag=2:接收的消息
    """



    if funcFlag == 1: # 发送信息
        # 1、消息解析 -> 指令码 + 参数
        try:
            cmd, params = parsing_send_msg(msg)
        except Exception as e:
            logs.error("信息解析错误:{}".format(msg))
            return

        # 2、指令表验证
        if cmd not in params_descs():
            logs.error("指令表未查找到此指令:{}".format(cmd))
            return

        # 3、信息打包与参数格式检查
        if cmd not in (cmds.STOP_VIZ, cmds.GET_DO_LIST, cmds.GET_STATUSES):  # 需要额外输入参数的情况
            try:
                params = command_func_dict[cmd](params) # 打包传入命令转化为可发送信息

            except Exception as e:
                logs.error("待发送信息打包失败:{}".format(e))
                return
        else:  # 不需要额外输入参数的情况
            params = bytes(params, encoding='utf-8')


        if not is_ascii: # 如果是Hex格式
            params += bytearray([0x00] * (36 - len(params)))  # 自动补齐

        if params == None: # TODO:建议做好所有消息的暴力测试，防止有错误处理遗漏的
            logs.error("待发送信息解析失败:{}".format(msg))
            return

        # 4、信息发送
        send_msg(socket_object, pack_params(cmd, fmt="i") + params)  # 发送信息
        return


    elif funcFlag == 2: # 接受信息
        recvmsg = parse_mech_msg(msg)
        return recvmsg

    else:
        logs.error("未收录的处理标识符{}".format(funcFlag))
        return