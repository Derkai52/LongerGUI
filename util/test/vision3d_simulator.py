from time import sleep
from unified_service.json_service import JsonService, start_server_and_wait
from unified_service.caller import HubCaller


# -------------------------------------------------配置区--------------------------------------------------
# 1. 工程名字
project_name = "vision_test"
# 2. 模拟poses
poses = [[-0.4, -0.6, 0.2, 0.71, 0, 0, 0.71],
         [-0.3, -0.6, 0.2, 1, 0, 0, 0],
         [-0.2, -0.6, 0.1, -0.71, 0, 0, 0.71],
         [-0.1, -0.6, 0, 0, 0, 0, -1],
         [0.0, -0.6, -0.2, 0.71, 0, 0, 0.71]] * 20
# 3. 模拟labels
labels = ["0", "1", "2", "0", "1"] * 20
# 4. 模拟速度参数
motion_params = [{"velocity": 0.2}, {"velocity": 0.6}, {"velocity": 0.5}, {"velocity": 0.8}, {"velocity": 0.1}] * 20
# 5. 模拟vision计算耗时
vision_cost = 5
# 6. 模拟有无点云
noCloudInRoi = False
# ---------------------------------------------------------------------------------------------------------


class Vision3dSimu(JsonService):
    service_type = "vision3d"
    
    def findPoses(self, *_):
        sleep(vision_cost)
        result = {"poses": poses,
                   "labels": labels,
                   "noCloudInRoi": noCloudInRoi,  
                   "motion_params": motion_params}
        result["function"] = "posesFound"
        HubCaller('127.0.0.1:5307').call("forward", {"type": "vision_watcher", "message": result})
        return result


if __name__ == '__main__':
    start_server_and_wait(HubCaller('127.0.0.1:5307'), Vision3dSimu(), project_name)
