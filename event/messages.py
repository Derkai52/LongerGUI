# 本文件存放 Mech 返回指令代码列表
from util.log import logs


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
VIZ_COLLISION_CHECKED         = 2006  # Viz检查碰撞
VIZ_PLAN_FILED                = 2007  # Viz规划失败
VIZ_RUN_ERROR                 = 2008  # Viz运行错误
VIZ_NO_TCP_POSE               = 2009  # Viz没有TCP姿态
VIZ_NO_DO_LIST                = 2011  # Viz没有DO列表
VIZ_POINT_TYPE_ERROR          = 2012  # Viz点位类型错误
VIZ_POINT_ERROR               = 2013  # Viz点错误
VIZ_PROJECT_NOT_SET           = 2014  # Viz工程没有被设置
VIZ_POSE_NOT_SUPPORTED        = 2015  # Viz不支持的Pose位姿
VIZ_SET_PROPERTY_ERROR        = 2016  # Viz设置属性错误
VIZ_STOP_FAILED               = 2017  # Viz停止失败
VIZ_BRANCH_OUTPORT_ERROR      = 2018  # Viz分支输出错误
VIZ_SET_BRANCH_ERROR          = 2019  # Viz设置分支错误
VIZ_NOT_RUN_YET               = 2022  # Viz没有再次运行
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


def adapter_message_dict(): # TODO: 事件反馈统一收录日志模块处理
    return {
        VISION_NOT_REGISTERED: output("Mech-Vision project is not registered"),
        VISION_NO_POSES: output("Mech-Vision No pose results"),
        VISION_NO_CLOUD: output("Mech-Vision No point cloud in ROI"),
        VISION_SET_PROPERTY_FAILED: output("Mech-Vision Set property failed"),
        VISION_POINT_TYPE_ERROR: output("Mech-Vision Pose type is invalid"),
        VISION_POINT_ERROR: output("Mech-Vision Pose value is invalid"),
        VISION_IN_CALCULATING: output("Mech-Vision is in calculating"),
        VISION_ALREADY_FINISHED: output("Mech-Vision The pose results had been sent"),
        VISION_POSES_MOTION_PARAMS_UNEQUAL: output("Mech-Vision The number of poses and motion params don't correspond"),
        VISION_POSES_LABELS_UNEQUAL: output("Mech-Vision The number of poses and labels don't correspond"),
        VISION_PROJECT_NOT_FOUND: output("Mech-Vision Project number does not exist"),
        VISION_RECIPE_NUM_OUT_RANGE: output("Mech-Vision parameter recipe number out of range. (CV-E0403)"),
        VISION_RECIPE_NOT_SET: output("Mech-Vision parameter recipe not set.(CV-E0401)"),
        VISION_SWITCH_MODEL_FAILED: output("Mech-Vision Switch recipe failed"),
        VISION_LABEL_MAPPING_ERROR: output("Mech-Vision Label Mapping number is invalid"),
        VISION_POSE_COUNT_ERROR: output("Mech-Vision Pose count error"),
        VISION_RUN_TIMEOUT: output("Mech-Vision Execution time timeout"),
        VISION_NOT_RUN_YET: output("Mech-Vision doesn't be executed"),
        VISION_HAS_POSES: output("Mech-Vision Get pose results successfully"),
        VISION_IS_READY: output("Mech-Vision is ready"),
        VISION_TRIGGERED_OK: output("Mech-Vision triggered successfully"),
        VISION_SET_MODEL_OK: output("Mech-Vision Recipe switched successfully"),
        VISION_SET_OUTER_BOX_SIZE_OK: output("Mech-Vision set external box size successfully"),

        VIZ_NOT_REGISTERED: output("Mech-Viz project is not registered"),
        VIZ_IS_RUNNING: output("Mech-Viz is in running"),
        VIZ_NO_VISION_POSE: output("Mech-Viz No pose results received from Mech-Vision"),
        VIZ_VISION_POSE_NOT_REACHABLE: output("Mech-Viz cannot reach the pose position from Mech-Vision"),
        VIZ_SELECT_JPS_ERROR: output("Mech-Viz Robot joints calculation failed"),
        VIZ_COLLISION_CHECKED: output("Mech-Viz Collision detected"),
        VIZ_PLAN_FILED: output("Mech-Viz motion planning failed"),
        VIZ_RUN_ERROR: output("Mech-Viz has running error"),
        VIZ_NO_TCP_POSE: output("Mech-Viz TCP pose is not provided"),
        VIZ_NO_DO_LIST: output("Mech-Viz DO list is not provided"),
        VIZ_POINT_TYPE_ERROR: output("Mech-Viz Pose type is invalid"),
        VIZ_POINT_ERROR: output("Mech-Viz Pose value is invalid"),
        VIZ_PROJECT_NOT_SET: output("Mech-Viz No project setup"),
        VIZ_POSE_NOT_SUPPORTED: output("Mech-Viz Tcp pose type is not supported"),
        VIZ_SET_PROPERTY_ERROR: output("Mech-Viz Set property failed"),
        VIZ_STOP_FAILED: output("Mech-Viz Stop execution failed"),
        VIZ_BRANCH_OUTPORT_ERROR: output("Mech-Viz Branch exitport is invalid"),
        VIZ_SET_BRANCH_ERROR: output("Mech-Viz Set branch failed, please check if it exists in project"),
        VIZ_NOT_RUN_YET: output("Mech-Viz doesn't be executed"),
        VIZ_PROJECT_IS_BROKEN: output("Mech-Viz project is abnormal"),
        VIZ_BRANCH_NAME_ERROR: output("Mech-Viz Branch name is invalid"),
        VIZ_RUN_TIMEOUT: output("Mech-Viz Execution time timeout"),
        VIZ_INDEX_NAME_ERROR: output("Mech-Viz Index-Skill name is invalid"),
        VIZ_INDEX_ORDER_ERROR: output("Mech-Viz Index number is invalid"),
        VIZ_SET_INDEX_ERROR: output("Mech-Viz Set index failed, please check if it exists in project"),
        VIZ_FINISHED: output("Mech-Viz execution completed successfully"),
        VIZ_COMMAND_STOP: output("Mech-Viz stopped successfully"),
        VIZ_SEND_DO_LIST_OK: output("Mech-Viz Send DO list successfully"),
        VIZ_RUN_OK: output("Mech-Viz start successfully"),
        VIZ_STOP_OK: output("Mech-Viz Stop successfully"),
        VIZ_SET_BRANCH_OK: output("Mech-Viz Set branch successfully"),
        VIZ_SET_INDEX_OK: output("Mech-Viz Set index successfully"),
        VIZ_SET_OUTER_POSE_OK: output("Mech-Viz Set external pose successfully"),

        CENTER_INVALID_COMMAND: output("Mech-Center Invalid command"),
        CENTER_ERROR_PACKAGE: output("Mech-Center interface message length or format error"),
        CENTER_CLIENT_DISCONNECTED: output("Mech-Center Client is disconnected"),
        CENTER_SERVER_DISCONNECTED: output("Mech-Center Server is disconnected"),
        CENTER_TIMEOUT_ERROR: output("Mech-Center Calling Mech-Vision timeout"),
        CENTER_OTHER_ERROR: output("Mech-Center Unknown error"),
        CENTER_CLIENT_CONNECTED: output("Mech-Center Client connect OK"),
        CENTER_CONNECT_TO_SERVER: output("Mech-Center Server connect OK"),
        CENTER_WAIT_FOR_CLIENT: output("Mech-Center Wait for client to connect"),

        ROBOT_INVALID_ROBOT_TYPE: output("Robot invalid robot type"),
        ROBOT_EULER_NOT_SUPPORTED: output("Robot Euler type isn't supported"),
        ROBOT_SERVICE_NOT_REGISTERED: output("Robot service isn't registered"),
        ROBOT_MISSING_PARAMS_ERROR: output("Robot server parameters are incomplete"),
        ROBOT_SERVICE_REGISTERED: output("Robot service registered OK"),
        CONNECT_ROBOT_SUCCESS: output("Robot server connect to the robot successfully"),
        CONNECT_ROBOT_FAIL: output("Robot server connect to the robot failed"),
        DISCONNECT_ROBOT_SUCCESS: output("Robot server get disconnected"),

        VISION_SET_OUTER_BOX_SIZE_FAIL: output("Mech-Vision set box size data is invalid"),

        CALIBRATION_PARAMS_ERROR: output("Calibration parameter error "),
        CALIBRATION_NO_POINT: output("Calibration no pose provided from Mech-Vision"),
        CALIBRATION_NOT_REACH_POINT: output("Calibration Robot failed to reach the calibration point"),
        CALIBRATION_MOVE_FINISHED: output("Calibration Robot moves to the calibration point successfully"),
        CALIBRATION_SEND_POINT_OK: output("Calibration pose received from Mech-Vision successfully"),

    }