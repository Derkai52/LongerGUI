# LongerGUI 二次开发手册 ( V0.1.1-Alpha )



## 一、设计模式

类之间是嵌套的，只有MainWindow类被外部实例化。其他类都被前一个类调用，实例化均在类里面进行，这样能维持一定的低耦合度。

![image-20211228160623026](C:/Users/tk/Desktop/LongerGUI项目相关资料/doc_img/image-20211228160623026.png)



## 二、日志

**1、py文件添加日志记录**

```python
from util.log_tool.log import logs # 导入日志对象
logs.debug("Debug消息") # 日志消息
```

**2、修改日志可视化等级颜色**

log.py修改COLORS字典映射关系





## 三、配置

**1、读取配置**

在文件开头导入：

~~~python
from util.generator import configObject # 导入配置类对象
~~~

在需要使用的地方：

~~~python
# 格式： configObject.配置大类.具体配置项
~~~



~~~python
# 示例：
configObject.software_config.software_name # 获取【软件名称】
configObject.mech_communication_config.mech_interface_ip # 获取【Mech标准接口IP地址】
configObject.robot_communication_config.robot_server_agent_ip # 获取【机器人接口服务端IP地址】
configObject.log_config.log_save_level # 获取【日志记录等级】
configObject.other_config.update_doc_name # 获取【更新文件】
~~~



**2、修改配置文件存放路径**：在 setting_file.py 修改有关路径即可

**3、修改配置文件内容：**

> **修改配置项名：**修改json_key.py 相关键名即可
>
> **修改配置项所属分类、修改配置项默认值**：修改 config_generator.py 所对应的类方法、get方法参数即可



## 四、权限

为保证生产与调试互不干扰，引入了权限分级机制。权限分级为

|  等级  |     权限说明     |
| :----: | :--------------: |
| 操作员 |  基础的功能操作  |
| 管理员 | 所有的配置项操作 |

> 管理员密码默认为：longer

若要更改默认密码，修改 config_generator.py 中密码配置项的get方法参数即可。





## 五、前端

### 1、前端设计规范

**1、UI工程目录规范：**

~~~shell
├── resource # 资源类
│   └── ui   # 存放UI文件及其pyqt资源
│       ├── pyqt_generated # 存放生成的pyqt资源
│       └── ... # 存放UI文件   
~~~



**2、UI文件命名规范：**

一个页面通常包含以下三个文件，这三个文件的命名格式示例：

|   文件名   |                             说明                             |
| :--------: | :----------------------------------------------------------: |
| UI\_Hub.ui |             UI 文件：可以使用QTDesigner直接编辑              |
| UI\_Hub.py |      界面类文件：由UI文件通过PyUIC工具转化生成的py文件       |
|   hub.py   | 界面类调用文件：通常用于程序进行页面初始化或进行调用交互的文件 |



**3、UI控件命名规范：**

> 控件名称：控件类\_控件名称\_控件序列
>
> 例如: horizontalLayout_display_bottom  (含义：展示区最底端的的横向布局)



**由于UI控件经常需要改动，所以有些控件命名规范不强制，但涉及到对接程序槽函数操作的控件，比如按钮，输入栏等。尽量按照规范命名，否则影响程序代码的可维护性。**



**4、一些示例：**

上图三个功能块的命名如下图所示：

![image-20220107212551036](C:/Users/tk/Desktop/LongerGUI项目相关资料/doc_img/image-20220107212551036.png)

上图展示了，一组命名方法

~~~python
label_text_poseNum # 提示文本：“位姿个数”
label_poseNum # 位姿数量值
~~~





### 2、信号与槽函数

**1、添加内置槽函数(点击事件)**

~~~python
    # 启动程序
    @pyqtSlot()
    def on_控件名_clicked(self): # on_控件名_信号(self)
        init_sys()  # 后端程序执行入口
~~~



**2、添加自定义信号与槽(事件关系)**

案例请参考《LongerGUI详细设计手册》的【自定义信号-槽函数】部分内容

> [PyQt5 信号与槽（PyQt5的事件处理机制)](https://www.cnblogs.com/chenhaiming/p/9930628.html)







## 六、常用工具

为了保证程序的易读性和低耦合性，提供了一个工具库，内含如下常用工具。只需要调用对应工具内已实现的功能即可。

![image-20211228163057123](C:/Users/tk/Desktop/LongerGUI项目相关资料/doc_img/image-20211228163057123.png)



|                    相关文件                     |       工具名       |                     说明                     |
| :---------------------------------------------: | :----------------: | :------------------------------------------: |
| config_tool、generator、json_keys、setting_file |      配置工具      |               读写修改配置文件               |
|                    log_tool                     |      日志工具      |        日志生成、清理、格式化、可视化        |
|                 dir_generation                  | 标准工程生成器工具 | 按格式标准化生成工程，用于快速标准化部署工程 |
|                 format_adapter                  |    软件格式工具    |              用于软件界面可视化              |
|                   message_box                   |    消息提示工具    |           用于软件运行窗口信息提示           |
|             translations(暂未启用)              |     国际化工具     |                用于多语言翻译                |
|                    util_file                    |    文件读写工具    |    支持常见文件读写（文本、json、二进制）    |
|                     vision                      |       视觉库       |               2D/3D图像算法库                |
|                                                 |                    |                                              |





## 七、相关资料参考

> Mech-Mind用户手册：https://docs.mech-mind.net/zh-CN/index.html
>
> PyCharm工具指南：[PyCharm 中文指南(Win版) 2.0 documentation (iswbm.com)](https://pycharm.iswbm.com/preface.html)
>
> PyQt5指南：[Qt5 中文指南 (biancheng.net)](http://c.biancheng.net/view/3851.html)
>
> Socket 通信：[Socket套接字及缓冲区详解](https://blog.csdn.net/daaikuaichuan/article/details/83061726)
>
> 信号与槽：[PyQt5 信号与槽（PyQt5的事件处理机制）](https://www.cnblogs.com/chenhaiming/p/9930628.html)
>
> 日志：[Python logging继承关系](https://lisongmin.github.io/python-logging-inherit/)

