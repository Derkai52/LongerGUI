# LongerGUI 详细设计手册 ( V0.1.1-Alpha )



## 一、项目资料

**项目简介：** LongerGUI是一款 Mech-Mind 的小工具，可进行数据处理与分析，帮助客户更直观的获取所需的生产信息

**项目仓库地址：** https://gitee.com/Derkai52/longer-gui.git

**开发平台：** x86 64位 Windows平台

**开发环境：** Python3.6，详细环境包请参阅《requirements.txt》

**开发工具：** Pycharm、QtDesigner

**相关工具资料：**

> [PyCharm 中文指南(Win版) 2.0 documentation (iswbm.com)](https://pycharm.iswbm.com/preface.html)
>
> [Qt5 中文指南 (biancheng.net)](http://c.biancheng.net/view/3851.html)

**软件运行示例图：**

![image-20220111223454813](.\doc_img\image-20220111223454813.png)



## 二、设计模式

类之间是嵌套的，只有MainWindow类被外部实例化。其他类都被前一个类调用，实例化均在类里面进行。

![image-20211228160623026](.\doc_img\image-20211228160623026.png)

## 三、前端

### 1、前端文件生成

#### 1.1、文件目录树设计

按照《LongerGUI开发者快速手册》的文件目录树设计要求，资源类文件尽可能按分类放置在对应文件夹内；

这样做的好处是资源目录路径固定，方便后面在IDE上配置QtDesigner等外部工具。

如下图所示，ui文件和对应生成的py文件都在pyqt_generated 目录下：

![image-20220108122812749](.\doc_img\image-20220108122812749.png)



#### 1.2、配置Pycharm的QtDesigner外部工具

**PyUIC工具** ：pyqt的一种将ui文件自动转化为py文件的工具

Pycharm通过添加【外部工具】，可快速运行QtDesigner和PyUIC，这样能大大提高前后端调试的效率，即可以随时在Pycharm看到修改后生成的界面代码文件：

![image-20220108125220794](.\doc_img\image-20220108125220794.png)



我们需要进行如下设置，相关路径以实际情况为准：（本质就是自定义命令行，在Pycharm上点击对应按钮时执行）

[参考链接：Pycharm 添加QT Designer和pyuic外部工具，利用pyuic将ui文件转为py代码](https://www.cnblogs.com/caiya/p/12930389.html)







#### 1.3、UI界面制作与Py文件生成（使用QtDesigner提供的默认组件）

> UI界面制作请参考《QtDesigner手册》，相关规范请参考《LongerGUI二次开发手册》中前端设计部分。



我们使用QtDesigner修改ui文件后，可以直接在Pycharm对修改后的ui文件执行PyUIC工具，它将自动生成一个同名称的py文件。

![image-20220108130640056](.\doc_img\image-20220108130640056.png)



由于考虑到py文件经常需要被覆盖性生成(PyUIC工具的特性)，所以我们**尽可能避免手动修改该文件代码**。

毕竟PyUIC工具生成的py代码时已经提示：

![image-20220108131050632](.\doc_img\image-20220108131050632.png)





生成的py文件包含一个与UI窗口同名的类。如下图所示，UI窗口里的组件及属性会作为实例属性包含在类里。

![image-20220108141616007](.\doc_img\image-20220108141616007.png)





#### 1.4、UI界面制作与Py文件生成（添加自定义组件）

QtDesigner默认的组件总是有限的，不能完全满足实际开发的需求。有一些已支持pyqt的第三方库，可以在py代码里面导入它们作为界面组件。

注：本项目使用的第三方库请参阅《requirements.txt》



**例如使用pyqtgraph包添加一个点云显示组件：**

![image-20220107150823024](.\doc_img\image-20220107150823024.png)



**将添加的组件插入到生成的Py文件代码中合适的位置** （通常位于setUi函数大概末尾处）

![image-20220108142450513](.\doc_img\image-20220108142450513.png)



上面这种方法的弊端仍然在于在执行PyUIC工具时会被覆盖，只建议临时使用或前端界面稳定，变更较少时使用。

此时可以使用QtCreator设计组件，并将组件相关文件导入QtDesigner即可。详见资料如下：









### 2、前后端事件交互

[相关资料：PyQt5信号与槽（事件处理机制）](https://www.cnblogs.com/chenhaiming/p/9930628.html)



每一个UI窗口都至少由以下几个文件组成：

~~~python
# 以主窗口MainWindow为例：
UI_MainWindow.ui # 主窗口UI文件
UI_MainWindow.py # 由PyUIC工具从主窗口UI文件生成的Py文件
main_window.py   # 主窗口界面类的实例化，用于在程序中执行
~~~



我们设计UI相关的文件目录结构如下，保证对前端界面修改时，尽量减少对程序的修改操作。

![image-20220108150254751](.\doc_img\image-20220108150254751.png)





#### 2.1、使用PyQt内置信号-槽函数

**此示例通过讲解点击【开始程序】来引入前后端事件交互的设计。**

在QTDesigner我们可以看到每个组件的属性表，如下图所示：

![image-20211229214530880](.\doc_img\image-20211229214530880.png)



为避免重复点击，我们想要点击【开始程序】按钮后，按钮需要变更为不可点击状态。即修改属性【enabled】的值由True变更为False.





PyUIC工具执行时会自动生成如下代码，按钮点击事件作为PyQt内置信号，在实例化对象时，统一连接到实例化对象中。

![image-20220108145522330](.\doc_img\image-20220108145522330.png)



所以我们现在只需要在实例化对象的地方创建内置槽函数即可！

![image-20211229213107918](.\doc_img\image-20211229213107918.png)



内置槽函数格式如下所示：

~~~ python
    @pyqtSlot() # 装饰器：通常放在函数上面一行，用于表明该函数基于此装饰器生成的。此处表明为该函数是一个QT内置槽函数
    def on_action_about_triggered(self): # 内置槽函数(内置槽函数名不可任意修改，否则无法捕获到内置信号。格式:on_控件名_信号名(self,内置参数))
        """
        槽函数功能代码......
        """
~~~



此示例则为创建了一个【启动程序】的槽函数，槽函数的格式多数如此。由于UI事件过多，且通常的输入输出都面向UI界面，所以一般不写对应代码文档。只用保证槽函数名浅显易懂即可。

![image-20211229213915871](.\doc_img\image-20211229213915871.png)



此时，我们在UI界面上触发事件时，事件信号能自动发送到对应槽函数并调用槽函数。





#### 2.2、自定义信号-槽函数

除了pyqt默认提供的信号-槽函数外，我们还需要自定义信号-槽函数，以保证程序前后端事件交互有更多的灵活性。

**本示例通过自定义的信号-槽函数，实现在后端统计当前位姿，在前端显示【位姿个数】**



如下图所示，首先定义一个自定义信号-槽类，用于后端事件信号发送给前端。

![image-20220107124122787](.\doc_img\image-20220107124122787.png)



同时完成对【自定义信号-槽函数】类的实例化，该实例化对象 display_signal 作为全局变量，可被导入到其他py文件中使用

![image-20220107131756379](.\doc_img\image-20220107131756379.png)



导入主界面初始化函数 mainwindow.py 

![image-20220107135552959](.\doc_img\image-20220107135552959.png)



自定义槽函数 output_pose_num

![image-20220107135659140](.\doc_img\image-20220107135659140.png)



此时，我们可以在需要的地方调用即可发送信号数据给前端即可。

~~~python
display_signal.pose_emit("位姿数量")
~~~





### 3、事件可视化

为了方便用户及调试人员能看到软件运行的实时状态，我们将日志记录的事件信息按日志等级显示在窗口特定区域。如下图所示：

![image-20220101182604004](.\doc_img\image-20220101182604004.png)

同时为了方便记录生产运行状态用于追溯复盘，生产运行日志也通过HTML文本格式记录，优势是可以格式化显示信息，不同记录等级的日志信息用不同颜色表示:

![image-20220102125316993](.\doc_img\image-20220102125316993.png)

**实现流程**

该部分程序的实现位于log.py部分，这里实现了两个类，分别是【生成器和处理器类】，以及【格式类】。

会在log文件内实例化一个日志对象，名称为 longer_ui，该对象被全局调用，所有日志信息均被该日志对象记录。

hub.py初始化时，会通过该日志对象生成一条处理器，该处理器通过信号槽发送信号至主窗口显示组件上。

该日志对象默认日志记录等级受权限等级调控，当登录用户为【操作员】时，最低可使用INFO等级；当登录用户为【管理员】时，最低可使用DEBUG等级。同时在此基础上可以在【初始化配置】中设置实际日志记录等级。



**日志内容的生成**

详细可参阅 **第5部分---日志**





## 四、配置

最初config文件我只用了一个文件，后来考虑到功能的拓展性，我们不得不用不同的文件来书写不同的模块，于是最终我们将所有配置工具相关的都放入了config_tool中。由于此部分设计抽象程度相当，我决定用大量的篇幅讲解说明，方便开发者了解。

![image-20211229215730437](.\doc_img\image-20211229215730437.png)



### 1、配置文件生成与保存

软件中有大量的参数需要保存和修改，我们设计了一个配置表，按照类别将他们分为以下几大类：

![image-20211228160740857](.\doc_img\image-20211228160740857.png)



最开始尝试过Windows下的ini或cfg格式保存配置，但跨平台性和程序可拓展性逊于json等结构化格式，于是采用json格式

为保证配置文件的可迁移性和访问安全性，默认保存路径选择在Windows默认的软件数据目录下

> 示例：C:\Users\用户名\AppData\Roaming\Longer\LongerGUI\setting.json



**引导式配置生成器**

为了方便配置，设计了引导式配置生成器，用户可通过提示按步骤完成基本项的配置。界面如下：

![image-20220107153305292](.\doc_img\image-20220107153305292.png)



针对该功能，我们设计了一个Setting类(详见setting.py)，包含了如下细节：

首先会初始化窗口组件，读取配置文件内容并填充到组件中，作为初始值，用户可以对初始值进行修改；每当用户完成一页的配置后，点击下一步时会触发配置检查，主要检查用户输入是否正确。完成后会自动跳转到下一配置页；用户可通过点击左侧的高亮页面随时对已配置的页面进行修改。最后配置完成后，点击保存即可将配置内容写入到配置文件中。中途所有的信息提示都通过QMessage弹窗类实现。



**部分功能设计：**

**1、保存配置：**

![image-20220107153541564](.\doc_img\image-20220107153541564.png)



**2、配置文件目录生成：**

![image-20220107153624399](.\doc_img\image-20220107153624399.png)



**3、步骤检查和全局检查：**

![image-20220107153726232](.\doc_img\image-20220107153726232.png)



### 2、配置文件读写

配置文件的读写功能，直接使用了自定义的【文件读写工具库】，程序将在初始化时自动读取配置文件。为提供二次开发的便捷性，我们希望能提供一个易于外界访问的配置类实例，同时该配置类实例只能在系统中有一个，从而防止访问冲突并节约系统资源。

[相关资料：Python中的单例模式](https://www.cnblogs.com/shenbuer/p/7724091.html)

![image-20220112000722217](.\doc_img\image-20220112000722217.png)





我们希望通过一个单例模式设计的实例化对象就能访问配置项。所以我们将提前区分好的几大类别配置文件分别用类实现，然后让它们统一在【生成器类：Generator】内进行实例化。

![image-20211229223057671](.\doc_img\image-20211229223057671.png)





同时我们希望【生成器类：Generator】具备的基础功能点为：**读写配置文件**

于是拆分为该类为两个方法，一个用于读配置文件，一个用于写配置文件。此时我们正好用到工具库里面的读写函数，非常美妙简洁！

由于我们的配置文件类型是json格式，所以在读写之前我们需要对该格式进行一个转换，即变成我们能直接使用的，于是我们把读写配置文件的方法分别命名为【序列化】【反序列化】，听上去很酷，简而言之就是通过一种方式将配置信息序列化生成json格式，或将json格式反序列化解析为便于程序可用的信息。

![image-20211229224440958](.\doc_img\image-20211229224440958.png)

由于需要考虑大量配置的访问，且没有下标访问和配置项键值对唯一性的需求。基于哈希的无序且唯一以及访问性能高效，**我们选定配置表数据结构为字典** 。

由于存在大量键值对的访问，又为了便于程序的书写。所以专门用一个json_key.py文件来存放键值对的键。

这样设计的好处在于我在程序中访问变量，即可获得对应的键。而不影响程序的易读性和美观。当修改键名仅需修改json_key.py文件即可:

![image-20220112001236970](.\doc_img\image-20220112001236970.png)





### 3、 反序列化操作(读取配置文件)

这个部分较为抽象，我们用 **读取【软件名称】** 的示例来梳理工作流程，总结该部分程序结构设计

由于我们希望能在全局使用配置信息，所以我们用单例模式实例化了一个配置类对象 configObject，该对象由单例生成，通过import被各文件访问使用。

先说结果， **读取【软件名称】** 我们的代码是：

~~~python
configObject.software_config.software_name
# 配置类对象----> 软件配置大类 ----> 软件名称
~~~

如上表所示，这样的写法在代码中能让人清晰看到配置的层级关系。



为了实现这样的递进访问关系，程序的设计如下：

![image-20211229224713281](.\doc_img\image-20211229224713281.png)

首先通过工具库的 read_json_file函数获取json文本内容，由于json文本内容在python可以使用字典解析，于是使用字典的get方法获取对应键的值。为了在访问时能体现出层次分类递进的关系。此处我们仅仅获取了大类的配置。我们对每个大类的配置都定义了对象变量。



那么如何单独获取配置项的值呢？我们以 SoftWareConfig类为例：

![image-20211229230020602](.\doc_img\image-20211229230020602.png)





![image-20211229230317291](.\doc_img\image-20211229230317291.png)

此处传入的参数js即为配置大类的配置表（一个字典），通过对该字典的get函数，即可获得配置大类配置项的值。同时还可以利用get方法的第二个参数设置默认值，实现 ”无法正常读取参数时，使用默认值“。



自此，读取软件名称的流程就走完啦!





### 4、序列化操作(写入配置文件)

同上条【反序列化操作】相似，也利用了层级递进的关系进行生成和写入，详见代码。



### 5、引导式配置

**设置页面报错提示的设计思路：** 为了方便用户按步骤配置信息，又兼顾考虑到用户需要随时对已配置好的配置页重新修改，结合采用了”引导式“配置流程和灵活的跳转修改，在点击下一页的跳转时进行当前页的配置检查。同时在最后的保存设置重新对配置情况再进行全局检查。

**报错提示信息** ：不同配置页用":"作为间隔符，配置页内不同配置项用","作为间隔符。所以在设计报错提示信息请避免使用这两个字符







## 五、通讯

由于软件的最初定位为Mech与机器人的信息中转兼数据处理中心。

所以采用了端口转发的形式实现数据分发。



### 1、数据中转处理中心Hub设计

Longer-GUI在智能生产系统中的工作角色如下图所示：

![LongerGUI网络拓扑](.\doc_img\LongerGUI网络拓扑.png)



由于需要考虑和多方设备进行通讯，在通讯协议使用了应用广泛的Socket通讯，目前支持TCP协议，设计了数据处理和事件。

为减少维护难度和保证生产运行安全，Longer只负责和Mech建立完整的通讯，而机器人端的通讯状态(例如心跳检测、校验连接等通讯机制)，交由Mech处理，在此环节中Longer仅提供端口数据转发服务。

![Longer工作流图.drawio](.\doc_img\Longer工作流图.drawio.png)



### 2、与Mech的通讯

程序启动后，Hub类实例化，会初始化一个 Tcp客户端套接字，根据配置信息的Mech标准接口地址尝试连接。

由于在多方的通讯中，与Mech的通讯优先级是最高的，所以在最开始的启动代码(主线程)中采用周期循环检测，来判断Mech通讯的连接情况，并引入了断线重连机制。在重连期间，TCP客户端套接字会尝试访问Mech标准接口地址端口，周期默认为2秒(此时主线程处于阻塞状态)

![image-20220105095418542](.\doc_img\image-20220105095418542.png)





当连接成功后，都会自动进行一次对话校验，目前使用的校验码是Standard-Interface报文协议的 “901”指令码。完成校验检测才可继续对话，否则关闭对话。

详见《Standard-Interface协议报文》

**校验检测实现：**

![image-20220103182205315](.\doc_img\image-20220103182205315.png)



### 3、与Robot的通讯

为减少维护难度和保证生产运行安全，Longer只负责和Mech建立完整的通讯，而机器人端的通讯状态(例如心跳检测、校验连接等通讯机制)，交由Mech处理，Longer仅提供端口数据转发服务。所以连接Robot的前提是保证和Mech的通讯。与Mech建立连接后，Longer会开启一个Robot接口服务器，供机器人连接。

为了防止意外丢失连接导致不可预期情况，主循环会一直检测与Mech的通讯状态，若意外丢失连接，则会直接断开Robot连接。



### 4、与第三方设备的通讯

暂未开放



### 5、数据处理与事件

Mech 事件：直接引用Mech事件表

事件被设计收录日志，按日志等级表共分为4个等级。设计了一个函数event_logging用于获得事件日志等级和事件内容。并将其记录入日志中

使用：仅需调用event_logging(状态码)即可



设置了一个【指令生成处理表】，针对传入的不同指令码，调用不同【指令参数生成函数】。如下图所示

![image-20211231165604251](.\doc_img\image-20211231165604251.png)



使用：


```python
# 输入指令码和参数，返回打包好的信息
打包好的信息 = command_func_dict[指令码](参数)
```



## 六、日志

### 1、日志生成

使用Python自带的logging库实现日志管理，目前使用的事件表级别如下：

|  级别   | 级别数值 | 描述                                   |
| :-----: | :------: | -------------------------------------- |
|  DEBUG  |    10    | 详细信息，常用于调试                   |
|  INFO   |    20    | 程序正常运行过程中产生的一些信息       |
| WARNING |    30    | 虽然程序还在正常工作，但有可能发生错误 |
|  ERROR  |    40    | 程序出现错误                           |



**日志模块设计预期的需求:**

> 日志分级能应对不同场景：
>
> 1、对于操作员：要能在软件运行主界面上显示INFO级别及以上的信息实时查看运行状态；
>
> 2、对于管理员：在后台日志目录保存DEBUG级别及以上的信息便于管理员追溯和排查问题。
>
> 同时要求日志信息描述简洁直观、自动化日志管理



**实现设计：**

> 相关代码：log.py   main_window.py  format_adapter.py

日志模块在log.py实现，在这里初始化了两个日志对象，分别是log_record 和 logs，

其中logs面向用户界面日志事件可视化，log_record用于日志文件记录，他们的继承关系如下图：

关于logging对象间传递日志信息的实现原理可参阅资料：[Python logging继承关系](https://lisongmin.github.io/python-logging-inherit/)



![日志层级关系.drawio](.\doc_img\日志层级关系.drawio.png)







其中logging_handler作为logs的日志处理器，在hub.py中被实例化；当该处理器被使用时，能自动发送信号给界面组件，实现实时显示日志事件。

**logging_handler实例化类设计如下：**

![image-20220102224002447](.\doc_img\image-20220102224002447.png)



**在主窗口初始化时初始化：**

![image-20220102224610705](.\doc_img\image-20220102224610705.png)



**根据发送的信号内容输出到界面上：**

![image-20220102225004015](.\doc_img\image-20220102225004015.png)





同时，作为全局变量，logs可以被项目中任一文件调用并使用logging_handler记录器记录事件。

logs的propagate默认为True，即通过logs记录的事件会传送至它的父日志对象 log_record。   作为ROOT层级的日志对象，log_record接收事件后会使用file_handler记录日志信息至HTML文件。





**于是根据logging的继承关系，完成了如下的分级处理：**

1、当logs设置为INFO时，【界面事件可视化】和【写入文件】只能看到INFO等级及之上的；

![image-20220102212141018](.\doc_img\image-20220102212141018.png)



2、当logs设置为DEBUG时，【界面事件可视化】和【写入文件】能看到DEBUG等级及之上的；

![image-20220102212211427](.\doc_img\image-20220102212211427.png)







### 2、日志管理

由于不间断生产会产生海量日志信息，为方便排查信息，在记录格式设置上默认设置为：

> ```python
> '%(asctime)s.%(msecs)03d %(levelname)s %(message)s' # 格式
> ```



**示例：**![image-20220102170558266](.\doc_img\image-20220102170558266.png)

**特性：**

1、事件记录以提供了小数点后3位的毫秒数

2、使用HTML语法进行分级颜色区分

3、日志文件设置了自动清理机制，默认以天为文件分隔，当超过7天的日志信息会被自动覆盖



**注意：**

> 1、需要保证运行所在系统时钟正确。
>
> 2、日志记录时刻仅作为参考值，不代表事件真实发生时刻，可能存在40~800ms内的延时，主要原因由通讯IO导致。
>
> 3、备份日志信息请手动备份





**根据日志进行程序调试：**

根据logging继承机制，仅需对日志信息的入口调整记录等级即可修改日志记录的等级范围。（详见 log.py）

![image-20220102214139783](.\doc_img\image-20220102214139783.png)





## 七、其他

### 1、权限与安全

由于防止误操作诱发生产事故，我们设定了权限分级。让不同等级的用户有不同的操作权限范围。目前含有【操作员】【管理员】两个权限等级

可以通过点击主界面上的用户名切换用户。操作员可以直接登录。而管理员需要输入密码登录。同时管理员也可以修改密码。

密码作为配置文件信息，存储在本地。

> **管理员默认密码是**:
>
> longer

若要更改默认密码，修改 config_generator.py 中密码配置项的get方法参数即可



### 2、部署与兼容性

#### 2.1、程序打包

可以使用pyinstall库打包你的python项目。但这会不可避免的导致程序过大和运行性能进一步下降。

由于软件需要配合Mech软件使用，所以我们默认软件运行所在的环境是含有Mech的环境（包含pyqt等库），所以我们可以通过打部分的环境包，减少包的大小。



同时建议将核心类的算法模块，C++实现底层算法暴露接口通过打包成DLL库给python调用。这样能保证程序运行的性能，又保证了核心算法知识产权安全性。

> 推荐使用 Pybind11 工具来实现这一功能





#### 2.2、程序部署


目前程序预留了两种启动方式:

> 1、手动执行main.py文件启动程序；
>
> 2、通过外部传参调用的方式启动。将我们的程序作为Mech的子程序,实现在Mech-Center里面启动



这里详细说明一下在Mech-Center的实现原理：

> 利用Mech-Center的mainwindow.py中的app_start函数（程序启动器）完成对第三方程序的调用



首先来看一下Mech-Center是如何启动Viz和Vision，以及Center-Vision-Viz之间的通讯的，这样能帮助我们理解Center是如何调用和配合其他软件程序的。

实现代码在Mech-Center的mainwindow.py中，该部分设计如下：

![image-20220111153813645](.\doc_img\image-20220111153813645.png)



Center、Vision、Viz的通讯数据即可通过进程管道subprocess.Popen进行交互。

所以我们仅需在Mech-Center中写入外部调用软件的执行路径和相关参数，即可实现调用Longer或其他第三方程序。





#### 2.3、将LongerGUI嵌入到Mech-Center中

**下面通过两个示例展示了如何添加Longer软件入口至Mech软件中**



**1、将入口添加至Center工具栏中，让用户自主启动Longer：**

![image-20220111212527471](.\doc_img\image-20220111212527471.png)





首先找到Mech-Center该窗口的UI文件，工具栏所在的UI文件是UI_MainWindow.py

我们直接翻到最下面，将所示QT控件代码添加至setupUi函数靠近末尾处（UI文件通常代码很长，添加到该函数末尾主要是为了方便查找）

![image-20220111212436298](.\doc_img\image-20220111212436298.png)



然后转到mainwindow.py中，添加对应的QT内置槽函数（详见前章：前后端交互）

![image-20220111215540987](.\doc_img\image-20220111215540987.png)

此时即可实现点击控件按钮，启动LongerGUI



**2、启动Vision/Viz的同时，自动启动LongerGUI：**

进入Mech-Center的mainwindow.py中的app_start函数（程序启动器），添加LongerGUI入口启动代码：

![image-20220111214657053](.\doc_img\image-20220111214657053.png)





## 结语---留给开发者的话（2022.1.12）

开发者你好，由于技术储备和开发规划的种种问题，**现在它还不是一个稳定的产品**。很抱歉，阅读这份代码可能会给你带来一些不好的体验。

现在需要面临一次重构，我有一些建议项如下，已按照优先级梳理了相对顺序，作为你的参考：



### 开展重构工作前的TODO清单：

**1、学习Mech-Center 界面源码**: 界面的架构设计和部分核心模块是从Mech-Center借鉴过来的，学习它有助于你消化这份代码。

**2、变量名存在多种规范**：比给自己家孩子取名字还难。

**3、解决异常处理流、IO流不明确问题**：当前只有程序流程图，没有清晰的异常处理流图，这对于维护工作是致命的。

**4、最可能面临重构的模块：通讯模块Hub**: 如果要拓展第三方设备，需要重构，否则就是屎山拉屎。

**5、检查代码里面的TODO清单: **通常它们都是有缺陷的点

**6、标准化目录生成器**：由于没有办法直接从Mech拿到图像信息，只能通过读取文件的方式拿取，此时标准化目录显得尤为重要。我们可以依托这个先决条件开始建立自己的图像算法库。

**7、文档标准化：**目前文档字数已经达到3万字，插图也有快百张了。。。

自评一下，这三个手册的完善度我只能打50分，主要原因在于目前稳定的模块还不够多，大部分正在开发的模块BUG是无穷的，功能点还改吗？现在可以写了吗？这个度很难拿捏。

