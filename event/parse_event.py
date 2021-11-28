# 本文件通过维护一个消息事件表，用于解析消息事件
import logging
from struct import pack, unpack
import socket
import sys
import os
from communication import commands as cmds
from event.messages import *
from config import *

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

########################## 指令处理 #######################
def run_vision(params):
    """
    doc: 运行Vision
    :param params: 传入对应指令参数
    :return: 打包后的信息
    """
    params = params.split(",")
    if len(params) not in (3, 9):
        print("Params missing!")
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


########################## 指令处理表 #####################
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

def recv_test(send_cmd, client): # TODO: 设置返回值
    print("Recving......")
    recv_cmds = client.recv(len_mech_msg)
    print(recv_cmds)
    recv_cmd, status_code = unpack_params(recv_cmds[:8], fmt="2i")
    print(recv_cmd, send_cmd)
    assert send_cmd == recv_cmd
    print("Status code={}, message: {}".format(status_code, adapter_message_dict()[status_code]))
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

def msg_process(msg, funcFlag):
    """
    doc: 对输入的信息进行处理，转化为可发送的信息
    :param cmd: 指令代码
    :param params: 指令代码参数
    :return:
    """
    cmd = msg[0]  # 获取指令代码
    params = msg[1]  # 获取指令参数 params = b""

    if cmd not in params_descs():
        print("Invalid command!")
        return # TODO: 返回一个 continue
        #continue


    if cmd not in (cmds.STOP_VIZ, cmds.GET_DO_LIST, cmds.GET_STATUSES):  # 需要额外输入参数的情况
        while not params:
            print(params_descs()[cmd]) # TODO: 可视化信息
            try:
                params = command_func_dict[cmd](params) # 打包传入命令转化为可发送信息
            except Exception as e:
                logging.exception(e)
                print("信息转化失败...")
    if not is_ascii: # 如果是Hex格式
        params += bytearray([0x00] * (36 - len(params)))  # 自动补齐

    if funcFlag == 1:
        send_msg(client, pack_params(cmd, fmt="i") + params)  # 发送信息
    elif funcFlag == 2:
        recv_test(cmd, client) # 接受信息