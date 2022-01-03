# 本文件存放 Mech 返回指令代码列表
from util.log_tool.log import logs


"""
    Mech 返回值状态号表
    1***: Mech-Vision
    2***: Mech-Viz
    3***: Mech-Center
    4***: Robot
    5***: Dynamic Data
    6***: Custom message
    7***: Calibration

    001~099: error code
    100~999: normal code
"""

VISION_NOT_REGISTERED         = 1001  # 视觉服务未注册
VISION_NO_POSES               = 1002  # 没有视觉点位
VISION_NO_CLOUD               = 1003  # 没有视觉3D点云
VISION_SET_PROPERTY_FAILED    = 1004  # 视觉服务属性设置失败
VISION_POINT_TYPE_ERROR       = 1005  # 视觉点类型错误
VISION_POINT_ERROR            = 1006  # 视觉点错误
VISION_IN_CALCULATING         = 1007  # 视觉计算中
VISION_ALREADY_FINISHED       = 1008  # 视觉计算完成
VISION_POSES_MOTION_PARAMS_UNEQUAL = 1009 # 视觉姿态运动参数不相等
VISION_POSES_LABELS_UNEQUAL   = 1010  # 视觉点位标签不对等
VISION_PROJECT_NOT_FOUND      = 1011  # 视觉工程未发现
VISION_RECIPE_NUM_OUT_RANGE   = 1012  # 视觉配方数量超出限制
VISION_RECIPE_NOT_SET         = 1013  # 视觉配方未设置
VISION_SWITCH_MODEL_FAILED    = 1014  # 视觉模型切换失败
VISION_LABEL_MAPPING_ERROR    = 1017  # 视觉标签映射错误
VISION_POSE_COUNT_ERROR       = 1018  # 视觉pose统计错误
VISION_RUN_TIMEOUT            = 1019  # 视觉运行超时
VISION_NOT_RUN_YET            = 1020  # 视觉未再次运行
VISION_SET_OUTER_BOX_SIZE_FAIL= 1021  # 视觉外部设置箱子尺寸失败

VISION_HAS_POSES              = 1100  # 视觉有pose点
VISION_IS_READY               = 1101  # 视觉已就绪
VISION_TRIGGERED_OK           = 1102  # 视觉已正常触发
VISION_SET_MODEL_OK           = 1107  # 视觉模型正常设置
VISION_SET_OUTER_BOX_SIZE_OK  = 1108  # 视觉外部设置箱子尺寸成功

VIZ_NOT_REGISTERED            = 2001  # Viz没有注册
VIZ_IS_RUNNING                = 2002  # Viz正在运行
VIZ_NO_VISION_POSE            = 2003  # Viz没有视觉pose点
VIZ_VISION_POSE_NOT_REACHABLE = 2004  # 视觉pose点不可到达
VIZ_SELECT_JPS_ERROR          = 2005  # Viz选择JPS错误
VIZ_COLLISION_CHECKED         = 2006  # Viz检查到碰撞
VIZ_PLAN_FILED                = 2007  # Viz规划失败
VIZ_RUN_ERROR                 = 2008  # Viz运行错误
VIZ_NO_TCP_POSE               = 2009  # Viz没有TCP姿态
VIZ_NO_DO_LIST                = 2011  # Viz没有DO列表
VIZ_POINT_TYPE_ERROR          = 2012  # Viz点位类型错误
VIZ_POINT_ERROR               = 2013  # Viz位姿错误
VIZ_PROJECT_NOT_SET           = 2014  # Viz工程没有被设置
VIZ_POSE_NOT_SUPPORTED        = 2015  # Viz不支持的Pose位姿
VIZ_SET_PROPERTY_ERROR        = 2016  # Viz设置属性错误
VIZ_STOP_FAILED               = 2017  # Viz停止失败
VIZ_BRANCH_OUTPORT_ERROR      = 2018  # Viz分支输出错误
VIZ_SET_BRANCH_ERROR          = 2019  # Viz设置分支错误
VIZ_NOT_RUN_YET               = 2022  # Viz没有被执行
VIZ_PROJECT_IS_BROKEN         = 2023  # Viz工程已损坏
VIZ_BRANCH_NAME_ERROR         = 2024  # Viz分支名称错误
VIZ_RUN_TIMEOUT               = 2025  # Viz运行超时
VIZ_INDEX_NAME_ERROR          = 2026  # Viz索引名称错误
VIZ_INDEX_ORDER_ERROR         = 2027  # Viz索引顺序错误
VIZ_SET_INDEX_ERROR           = 2028  # Viz工程设置顺序错误
VIZ_FINISHED                  = 2100  # Viz完成
VIZ_COMMAND_STOP              = 2101  # Viz命令停止
VIZ_SEND_DO_LIST_OK           = 2102  # Viz发送DO列表成功
VIZ_RUN_OK                    = 2103  # Viz运行成功
VIZ_STOP_OK                   = 2104  # Viz停止成功
VIZ_SET_BRANCH_OK             = 2105  # Viz设置分支成功
VIZ_SET_INDEX_OK              = 2106  # Viz设置序号成功
VIZ_SET_OUTER_POSE_OK         = 2107  # Viz外部传入位姿(用于Out Move)成功

CENTER_INVALID_COMMAND        = 3001  # Center命令无效
CENTER_ERROR_PACKAGE          = 3002  # Center信息解包错误
CENTER_CLIENT_DISCONNECTED    = 3003  # Center已断开连接(客户端)
CENTER_SERVER_DISCONNECTED    = 3004  # Center已断开连接(服务端)
CENTER_TIMEOUT_ERROR          = 3005  # Center超时错误
CENTER_OTHER_ERROR            = 3006  # Center其他错误
CENTER_CLIENT_CONNECTED       = 3100  # Center已连接(客户端)
CENTER_CONNECT_TO_SERVER      = 3101  # Center已连接至服务端
CENTER_WAIT_FOR_CLIENT        = 3102  # Center等待客户端

ROBOT_INVALID_ROBOT_TYPE      = 4001  # Robot类型无效
ROBOT_EULER_NOT_SUPPORTED     = 4002  # Robot不支持的欧拉角
ROBOT_SERVICE_NOT_REGISTERED  = 4003  # Robot服务端未注册
ROBOT_MISSING_PARAMS_ERROR    = 4004  # Robot缺少参数错误
CONNECT_ROBOT_FAIL            = 4005  # 连接Robot失败
ROBOT_SERVICE_REGISTERED      = 4100  # Robot服务端已注册
CONNECT_ROBOT_SUCCESS         = 4101  # 连接Robot成功
DISCONNECT_ROBOT_SUCCESS      = 4102  # 成功断开与Robot的连接

CALIBRATION_PARAMS_ERROR      = 7001  # 校准参数错误
CALIBRATION_NO_POINT          = 7002  # 没有校准点
CALIBRATION_NOT_REACH_POINT   = 7003  # 校准点没有到达
CALIBRATION_MOVE_FINISHED     = 7100  # 已移动至校准点
CALIBRATION_SEND_POINT_OK     = 7101  # 成功发送校准点信息


# TODO: 审查是否还有遗漏或者不合适的日志记录等级
def adapter_message_dict(): # TODO: 事件反馈统一收录日志模块处理
    return {
        VISION_NOT_REGISTERED: ["ERROR", "Mech-Vision 视觉工程未注册"],
        VISION_NO_POSES: ["ERROR", "Mech-Vision 没有结果点"],
        VISION_NO_CLOUD: ["ERROR", "Mech-Vision ROI区域无点云"],
        VISION_SET_PROPERTY_FAILED: ["ERROR", "Mech-Vision 设置属性失败"],
        VISION_POINT_TYPE_ERROR: ["ERROR", "Mech-Vision 位姿点类型无效"],
        VISION_POINT_ERROR: ["ERROR", "Mech-Vision 位姿点无效"],
        VISION_IN_CALCULATING: ["WARNING", "Mech-Vision 正在计算"],
        VISION_ALREADY_FINISHED: ["WARNING", "Mech-Vision 结果已发送"],
        VISION_POSES_MOTION_PARAMS_UNEQUAL: ["ERROR", "Mech-Vision 位姿数和运动参数的数量不对应"],
        VISION_POSES_LABELS_UNEQUAL: ["ERROR", "Mech-Vision 位姿和标签的数量不对应"],
        VISION_PROJECT_NOT_FOUND: ["ERROR", "Mech-Vision 项目不存在"],
        VISION_RECIPE_NUM_OUT_RANGE: ["ERROR", "Mech-Vision 配方编号超出范围. (CV-E0403)"],
        VISION_RECIPE_NOT_SET: ["ERROR", "Mech-Vision 未设置参数配方.(CV-E0401)"],
        VISION_SWITCH_MODEL_FAILED: ["ERROR", "Mech-Vision 切换配方失败"],
        VISION_LABEL_MAPPING_ERROR: ["ERROR", "Mech-Vision 标签映射编号无效"],
        VISION_POSE_COUNT_ERROR: ["ERROR", "Mech-Vision 位姿计数错误"],
        VISION_RUN_TIMEOUT: ["ERROR", "Mech-Vision 运行超时"],
        VISION_NOT_RUN_YET: ["ERROR", "Mech-Vision 没有被执行"],
        VISION_HAS_POSES: ["INFO", "Mech-Vision 成功获取位姿结果"],
        VISION_IS_READY: ["INFO", "Mech-Vision 当前可执行"],
        VISION_TRIGGERED_OK: ["INFO", "Mech-Vision 成功触发"],
        VISION_SET_MODEL_OK: ["INFO", "Mech-Vision 配方切换成功"],
        VISION_SET_OUTER_BOX_SIZE_OK: ["INFO", "Mech-Vision 外部输入box尺寸成功"],

        VIZ_NOT_REGISTERED: ["ERROR", "Mech-Viz 没有注册"],
        VIZ_IS_RUNNING: ["WARNING", "Mech-Viz 正在运行"],
        VIZ_NO_VISION_POSE: ["ERROR", "Mech-Viz 没有视觉pose点"],
        VIZ_VISION_POSE_NOT_REACHABLE: ["ERROR", "视觉pose点不可到达"],
        VIZ_SELECT_JPS_ERROR: ["ERROR", "Mech-Viz 选择JPS错误"],
        VIZ_COLLISION_CHECKED: ["ERROR", "Mech-Viz 检查到碰撞"],
        VIZ_PLAN_FILED: ["ERROR", "Mech-Viz 规划失败"],
        VIZ_RUN_ERROR: ["ERROR", "Mech-Viz 运行错误"],
        VIZ_NO_TCP_POSE: ["ERROR", "Mech-Viz 没有TCP姿态"],
        VIZ_NO_DO_LIST: ["ERROR", "Mech-Viz 没有DO列表"],
        VIZ_POINT_TYPE_ERROR: ["ERROR", "Mech-Viz 点位类型错误"],
        VIZ_POINT_ERROR: ["ERROR", "Mech-Viz 位姿错误"],
        VIZ_PROJECT_NOT_SET: ["ERROR", "Mech-Viz 工程没有被设置"],
        VIZ_POSE_NOT_SUPPORTED: ["ERROR", "Mech-Viz 不支持的Pose位姿"],
        VIZ_SET_PROPERTY_ERROR: ["ERROR", "Mech-Viz 设置属性错误"],
        VIZ_STOP_FAILED: ["ERROR", "Mech-Viz 停止失败"],
        VIZ_BRANCH_OUTPORT_ERROR: ["ERROR", "Mech-Viz 分支输出错误"],
        VIZ_SET_BRANCH_ERROR: ["ERROR", "Mech-Viz 设置分支错误,请检查项目中是否存在该工程"],
        VIZ_NOT_RUN_YET: ["ERROR", "Mech-Viz 没有被执行"],
        VIZ_PROJECT_IS_BROKEN: ["ERROR", "Mech-Viz 工程已损坏"],
        VIZ_BRANCH_NAME_ERROR: ["ERROR", "Mech-Viz 分支名称错误"],
        VIZ_RUN_TIMEOUT: ["ERROR", "Mech-Viz 运行超时"],
        VIZ_INDEX_NAME_ERROR: ["ERROR", "Mech-Viz 索引名称错误"],
        VIZ_INDEX_ORDER_ERROR: ["ERROR", "Mech-Viz 索引顺序错误"],
        VIZ_SET_INDEX_ERROR: ["ERROR", "Mech-Viz 工程设置顺序错误, 请检查项目中是否存在该工程"],
        VIZ_FINISHED: ["INFO", "Mech-Viz 执行完成成功"],
        VIZ_COMMAND_STOP: ["INFO", "Mech-Viz 停止成功"],
        VIZ_SEND_DO_LIST_OK: ["INFO", "Mech-Viz 发送DO列表成功"],
        VIZ_RUN_OK: ["INFO", "Mech-Viz 运行成功"],
        VIZ_STOP_OK: ["INFO", "Mech-Viz 停止成功"],
        VIZ_SET_BRANCH_OK: ["INFO", "Mech-Viz 设置分支成功"],
        VIZ_SET_INDEX_OK: ["INFO", "Mech-Viz 设置序号成功"],
        VIZ_SET_OUTER_POSE_OK: ["INFO", "Mech-Viz 外部传入位姿(用于Out Move)成功"],

        CENTER_INVALID_COMMAND: ["ERROR", "Mech-Center 命令无效"],
        CENTER_ERROR_PACKAGE: ["ERROR", "Mech-Center 信息长度或格式错误"],
        CENTER_CLIENT_DISCONNECTED: ["ERROR", "Mech-Center 已断开连接(客户端)"],
        CENTER_SERVER_DISCONNECTED: ["ERROR", "Mech-Center 已断开连接(服务端)"],
        CENTER_TIMEOUT_ERROR: ["ERROR", "Mech-Center 超时错误"],
        CENTER_OTHER_ERROR: ["ERROR", "Mech-Center 未知错误"],
        CENTER_CLIENT_CONNECTED: ["INFO", "Mech-Center 已连接(客户端)"],
        CENTER_CONNECT_TO_SERVER: ["INFO", "Mech-Center 已连接至服务端"],
        CENTER_WAIT_FOR_CLIENT: ["INFO", "Mech-Center 等待客户端连接"],

        ROBOT_INVALID_ROBOT_TYPE: ["ERROR", "Robot 类型无效"],
        ROBOT_EULER_NOT_SUPPORTED: ["ERROR", "Robot 不支持的欧拉角"],
        ROBOT_SERVICE_NOT_REGISTERED: ["ERROR", "Robot 服务端未注册"],
            ROBOT_MISSING_PARAMS_ERROR: ["ERROR", "Robot 缺少参数错误"],
        ROBOT_SERVICE_REGISTERED: ["INFO", "Robot 服务端已注册"],
        CONNECT_ROBOT_SUCCESS: ["INFO", "连接Robot成功"],
        CONNECT_ROBOT_FAIL: ["ERROR", "连接Robot失败"],
        DISCONNECT_ROBOT_SUCCESS: ["INFO", "成功断开与Robot的连接"],

        VISION_SET_OUTER_BOX_SIZE_FAIL: ["ERROR", "Mech-Vision 视觉外部设置箱子尺寸失败"],

        CALIBRATION_PARAMS_ERROR: ["ERROR", "校准参数错误"],
        CALIBRATION_NO_POINT: ["ERROR", "没有校准点"],
        CALIBRATION_NOT_REACH_POINT: ["ERROR", "校准点没有到达"],
        CALIBRATION_MOVE_FINISHED: ["INFO", "已移动至校准点"],
        CALIBRATION_SEND_POINT_OK: ["INFO", "成功发送校准点信息"],

    }


def event_logging(event_code):
    """
    doc: 日志事件记录
    :param event: 事件码
    :return: 事件解析内容
    """
    try:
        log_content = adapter_message_dict()[event_code]
    except Exception as e: # 解析错误或事件码未收录
        logs.error("未收录的事件类型:{}".format(event_code))
    level, content = log_content[0], log_content[1]
    if level == "DEBUG":
        logs.debug(content)
    elif level == "INFO":
        logs.info(content)
    elif level == "WARNING":
        logs.warning(content)
    elif level == "ERROR":
        logs.error(content)
    else:
        logs.error("未收录的日志记录等级！")

    return content
