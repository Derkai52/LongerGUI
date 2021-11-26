import logging
from struct import pack, unpack
import socket
import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "communication")))
from communication import commands as cmds
from event.messages import *


robot_vendor = "aaa"
endian = "<"
port = "50000"
is_ascii = True
auto_list = ["201", "1,-490.000,0,539.000,-90.000,90.000,180.000", "205", "1"]

a = [1, 2.5, 3.0]
b = float("1")
if b.is_integer():
    Number = int(b)
ccc = ""
print(2) if ccc and float(ccc) else print(1)


def unpack_ascii_params(*args, **kwargs):
    if isinstance(args[0], bytes):
        str_list = filter(None, args[0].decode().split(','))
        return [int(float(i)) if i and float(i).is_integer() else float(i) for i in str_list]
    return args


def pack_ascii_params(*args, **kwargs):
    return (','.join([str(i) for i in args]) + ',').encode(encoding='utf-8')


def unpack_hex_params(*args, **kwargs):
    return unpack('{}'.format(endian) + kwargs.get('fmt', ''), *args)


def pack_hex_params(*args, **kwargs):
    return pack('{}'.format(endian) + kwargs.get('fmt', ''), *args)


if is_ascii:
    pack_params = pack_ascii_params
    unpack_params = unpack_ascii_params
else:
    pack_params = pack_hex_params
    unpack_params = unpack_hex_params


# zzz = pack_ascii_params(*a)
# xxx, *ccc = unpack_ascii_params(zzz)
# xxx = unpack_ascii_params(*ccc)


def command_descs():
    """
    doc: 指令代码选择提升区
    :return:
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


def run_vision(params):
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
    params = params.split(",")
    if len(params) != 1:
        print("Params missing!")
        return
    return pack_params(int(params[0]), fmt="i")


def switch_model_set_branch_index(params):
    params = params.split(",")
    if len(params) != 2:
        print("Params missing!")
        return
    return pack_params(int(params[0]), int(params[1]), fmt="2i")



def run_viz(params):
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
    params = params.split(",")
    if len(params) != 4:
        print("Params missing!")
        return
    return pack_params(int(params[0]), *([float(i) for i in params[1:]]), fmt="i3f")


def set_outer_pose(params):
    params = params.split(",")
    if len(params) != 6:
        print("Params missing!")
        return
    return pack_params(*[float(i) for i in params], fmt="6f")


def pack_calibrate_params(params):
    params = params.split(",")
    if len(params) != 13:
        print("Params missing!")
        return
    return pack_params(int(params[0]), *([float(i) for i in params[1:]]), fmt="i12f")


def send_msg(client, msg):
    if not is_ascii:
        if robot_vendor and robot_vendor.startswith("KUKA"):
            msg += b"\x00" * (660 - len(msg))
        else:
            msg += b"\x00" * (56 - len(msg))
    client.send(msg)


def recv_test(send_cmd, client):
    print("Recving......")
    recv_cmds = client.recv(660)
    print(recv_cmds)
    recv_cmd, status_code = unpack_params(recv_cmds[:8], fmt="2i")
    print(recv_cmd, send_cmd)
    assert send_cmd == recv_cmd
    print("Status code={}, message: {}".format(status_code, adapter_message_dict()[status_code]))
    if recv_cmd in (cmds.GET_VISION_DATA, cmds.GET_VIZ_DATA) and status_code in (VISION_HAS_POSES, VIZ_FINISHED):
        recv_finished, point_count, *visual_move_position = unpack_params(recv_cmds[8:], fmt="3i")
        print("Recv not finish, you can continue to get data using same command" if recv_finished == 0 else "Recv finished")
        print("Point count={}".format(point_count))
        if recv_cmd == cmds.GET_VIZ_DATA:
            print("Visual move position is", visual_move_position)
        poses_labels_speeds = unpack_params(recv_cmds[20:], fmt="6fii" * point_count)
        print(poses_labels_speeds)
        for i in range(point_count):
            print("Pose", i+1, ":", poses_labels_speeds[i*8:i*8+6], "Label:", poses_labels_speeds[i*8+6], "Speed:", poses_labels_speeds[i*8+7])
    elif recv_cmd == cmds.GET_CALIBRATION_DATA and status_code == VISION_SEND_CALIBRATION_POINT_OK:
        points = unpack_params(recv_cmds[8:], fmt="i12f")
        print("Calibrate point: Pose=[{}], Jps=[{}]".format(points[1:7], points[7:]))
        if points[0] == 1:
            print("Calibration finished!")
    elif recv_cmd == cmds.GET_DO_LIST:
        do_list = unpack_params(recv_cmds[8:], fmt="64i")

        print("Available do:", do_list[0:64 - do_list.count(-1)])
        print("Do list={}".format(do_list))


def test_loop():
    # args = sys.argv
    # if len(args) < 2:
    #     print("Usage: \n  %s  port(server listen port)" % args[0])
    #     return
    # print("Ctrl+C to quit test\n")
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
    logging.info("port:{}".format(port))
    client = socket.create_connection(("127.0.0.1", port))
    print("Connect to server successfully.")
    auto_start = False
    while True:
        client.settimeout(None)
        print("Input below number to start test:")
        for desc in command_descs():
            print("\t" + desc)
        try:
            cmd = int(input("Input command:") if not auto_start else auto_list[auto_index])
            if cmd == 6:
                auto_start = True
                cmd = int(auto_list[0])
                auto_index = 0
            if auto_start:
                auto_index += 1
        except ValueError:
            print("Invalid command!")
            continue
        if cmd not in params_descs():
            print("Invalid command!")
            continue
        params = b""
        if cmd not in (cmds.STOP_VIZ, cmds.GET_DO_LIST, cmds.GET_STATUSES):
            while not params:
                print(params_descs()[cmd])
                params = input("Input params in order(comma separated):") if not auto_start else auto_list[auto_index]
                if auto_start:
                    auto_index += 1
                    if auto_index >= len(auto_list):
                        auto_start = False
                try:
                    params = command_func_dict[cmd](params)
                except Exception as e:
                    logging.exception(e)
                    print("Exception occurred. Check and input again...")
        if not is_ascii:
            params += bytearray([0x00] * (36 - len(params)))
        send_msg(client, pack_params(cmd, fmt="i") + params)
        
        recv_test(cmd, client)


def read_robot_vendor():
    global robot_vendor
    # robot_vendor = input("Input robot vendor(Case insensitive):").upper()
    print("Current robot vendor is:[", robot_vendor, "]")

def read_endian():
    global endian
    # endian = input("Input endian('>' or '<'):")
    print("Current robot vendor is:[", endian, "]")

def read_port():
    global port
    # port = input("Input port:")
    print("Current port: " + port)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")
    read_robot_vendor()
    read_endian()
    read_port()
    logging.info("is_ascii:{}".format(is_ascii))
    try:
        test_loop()
    except KeyboardInterrupt:
        print("\nQuit test.")
    except Exception as e:
        logging.exception(e)
