#ROS2机器人开发
##Chapter1 启程
###ROS是什么？


    大脑	<-------皮肤（传感器）
（决策系统）	
		神经网络ROS
		
		------->肌肉（执行器）

本质上是用于快速搭建机器人的软件库（核心是通信）和工具集 追求稳定安全实时的通信能力

###ROS2系统架构
ROS 2 架构（分层并列）

应用层           │  ROS 2 客户端层    │  rcl客户端库   │  DDS接口层   │  DDS实现层          │  操作系统层
─────────────────┼────────────────────┼──────────────—─┼─────────────—┼─────────────────────┼───────────────
用户代码         │  rclcpp (C++)      │  rcl           │  RMW         │  Fast DDS           │  Linux
(ROS 2 节点)     │  rclpy (Python)    │  (C语言实现)   │  (ROS中间件  │  Eclipse Cyclone DDS│  Windows
                 │  其他语言API       │                │   接口)      │  RTI Connext DDS    │  macOS
四大核心通信机制

话题（Topic）：  
基于发布-订阅模式的通信方式，允许节点之间异步交换数据。

服务（Service）：  
同步通信方式，客户端发送请求，服务端处理并返回结果。

参数（Parameter）：  
用于机器人参数的设置和读取。

动作（Action）： 
支持复杂行为的通信方式，服务端可以反馈处理进度，客户端可以取消请求。

缺点：
受操作系统限制
本身做不到实时性 硬实时依赖操作系统
通信速度受内存速度 网速等物理层限制

Ubuntu安装ros2

###运行你的第一个机器人
ros2 run turtlesim_node turtlesim_node  功能包 可知性文件
打开小海龟
在第二个终端输入
ros2 run turtlesim turtle_teleop_key
点击第二个终端
用上下左右控制前后运动和方向
使用键盘移动海龟 

小海龟例子的简单分析
终端输入rqt
工具栏选择plugins/introspection/Node Graph
单击右上角刷新 获取当前系统最新的节点关系
/turtlesim ──发布──> /turtle1/cmd_vel ──订阅──> /teleop_turtle

/turtlesim ──提供──> /turtle1/rotate_absolute_action/feedback ──监听──> /teleop_turtle

/turtlesim ──提供──> /turtle1/rotate_absolute_action/status  ──监听──> /teleop_turtle

###掌握Linux基础命令
ros2 run --help
usage: ros2 run [-h] [--prefix PREFIX] package_name executable_name ...

安装vscode git 
下载.deb
sudo dpkg -i 

在linux中编写python、cpp代码
cmake

###Linux环境变量
echo $ROS_VERSION
找到ros版本号

echo $ROS_DISTRO
找到ros版本发行名字

printenv
打印所有环境变量
printenv | grep AMENT 过滤得到含有AMENT的内容

ros2 run turtlesim turtlesim_node在执行什么？
1.找到环境变量AMENT_PREFIX_PATH
=opt/ros/humble
2.其下找到lib/package_name/executable_name

环境变量谁设的
~/.bashrc隐藏文件
中有一行
source /opt/ros/humble/setup.bash
脚本文件功能之一为添加环境变量

#Chapter2 节点
##编写你的第一个节点

#Chapter3 话题
#Chapter4 服务
#Chapter5 工具
#Chapter6 仿真
#Chapter7 导航
#Chapter8 导航进阶
#Chapter9 真机实战
#Chapter10 进阶
