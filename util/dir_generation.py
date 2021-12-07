import os
def mkdirs(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)


def Splicing():

    return project_path





if is_custom: # 是否为自定义模式
    pass
else:
    task_name = input("请输入工件任务或功能场景")
    project_type = input("请输入工程类型\n1、单个工件任务/功能场景\n2、")
    camera_type = input("请输入相机数")
    if project_type == 1: # 单个工件任务,单相机
        pass
