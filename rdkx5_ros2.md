# ROS2架构
- 系统架构	完全分布式（无中心节点，基于DDS）
- 底层通信	工业级标准DDS（数据分发服务）
- 实时行	强（支持QoS策略，适配RTOS）
- 多机通信	原生支持（自动发现，无缝多机协同）
- 跨平台	Linux,Windows,MacOS,RTOS
- 编程语言	C++14+/Python3
## DDS
```text
Data Distribution Service
专门为实时系统和分布式系统设计，采用发布-订阅的通信模型
```
# 搭建开发环境
- 安装Ubuntu 22.04 LTS Desktop
- 通常采用PC（开发/调试/仿真主机）+开发板（部署/运行/边缘计算节点）双机协同
- 进行一些ros2的配置
- 启动小海龟
另开一个终端
```bash
ros2 topic echo /turtle1/cmd_vel 
#可打印速度数据
```
- 三个终端之间存在DDS通信


# colcon构建系统
- collective construction(集体构建)
- 管理器而不是底层编译器
- 核心工作
1. 扫描各个源码目录，分析依赖拓扑图
2. 决定编译顺序，调度底层工具（CMake/Make/Ninja）干活
3. 将编译生成的目标文件存放到install 目录

## ROS2功能包（package）
- include/:	 	存放C++头文件(.h/.hpp)
- src/:			存放C++的源代码文件(.cpp)
- package.xml : 	ROS2功能包描述文件(xml格式的清单文件，定义了功能包的元数据和依赖关系)
- CMakeList.txt	:	定义colcon build 编译源代码的具体规则 		包括查找依赖库、指定C++标准、生成可执行文件或库文件、安装规则

## ROS2工作区workspace
- build/:		编译产生的临时文件、CMake缓存文件等(随时可删)
- install/:		安装目录，存储编译生成的可执行程序文件(存储Node)
- log/:			日志目录，用于存储日志文件
- package_1\2\3...		存放功能源码(git 版本控制目标) 当pkg过多时，也可以统一放入src目录

## ROS2工程创建
1. 创建工作目录
```bash
mkdir -p ~/ros2_ws
cd ~/ros2_ws
```
2. 创建ROS2工作区
```bash
colcon build
```
	
3. 创建ROS2 C++功能包(位于工作目录中)
```cpp
ros2 pkg create my_first_pkg --build-type ament_cmake --node-name hello_node			
# ros2 创建功能包 叫myfirstpackage 用cmake编译 最终形成可执行程序的名字为hello_node
```

# 如何编译构造系统
- package.xml 配置文件 定义了功能包的元数据和依赖关系
- 核心标签
1. 元数据-> 	<name>/<version>/<description>
2. 依赖关系->	<depend>rclcpp</depend> 	#very important!
- Remark: 如果代码里#include<rclcpp/rclcpp.hpp>,但package.xml里没写<depend>rclcpp</depend>，后续打包发布会报错

- package.xml配置示例
骨干
```text
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<!-- 根标签：ROS 2 强烈建议使用 format="3" -->
<package format="3">

  <!-- ================ 第一段：我是谁？（包的身份信息） ================ -->
  <name>my_first_pkg</name>
  <version>0.0.1</version>
  <description>我的第一个 ROS 2 C++ 功能包</description>
  <maintainer email="student@robot.com">student</maintainer>
  <license>Apache-2.0</license>

  <!-- ================ 第二段：我需要啥？（依赖清单 BOM） ================ -->
  <!-- 1. 构建工具依赖（告诉 colcon 用什么编译工具） -->
  <buildtool_depend>ament_cmake</buildtool_depend>

  <!-- 2. 核心代码依赖（我的 C++ 代码里用到了哪些库？） -->
  <!-- 重点：format 3 的 <depend> 标签，一键搞定编译和运行依赖！ -->
  <depend>rclcpp</depend>

  <!-- ================ 第三段：我怎么构建？（构建类型声明） ================ -->
  <export>
    <build_type>ament_cmake</build_type>
  </export>

</package>
```
## cmake VS ament_cmake
- cmake独立且跨平台构建工具 适用于任何c cpp py 项目
- ament_cmake	专为ROS2设计、基于cmake 扩展的构建宏 封装了ROS2 特有的依赖解析、接口生成和包注册机制 
- 通过预定义宏自动处理
1. ROS2依赖传递
2. 头文件路径配置
3. 环境变量注册
```
	宏拓展		   colcon	
cmake   -----> ament_cmake -----> ROS2节点
```
## CMakeLists配置文件
```txt
cmake_minimum_required(VERSION 3.8)
project(my_first_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ================ 寻找依赖 ================
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)  # 对应 package.xml 中的 <depend>

# ================ 定义并链接目标 ================
# 1. 把源码变成可执行文件
add_executable(hello_node src/hello_node.cpp)

# 2. 使用 ament_cmake 提供的宏把关键组件(rclcpp)链接到程序中
ament_target_dependencies(hello_node rclcpp)

# ================ 安装到 install 目录 ================
install(TARGETS
  hello_node
  DESTINATION lib/${PROJECT_NAME}
)

# 告诉 ament 系统：这个包配置完毕
ament_package()
```
- 编写"Hello ROS2"代码
```cpp
#include <rclcpp/rclcpp.hpp>                             // ① 引入 ROS 2 C++ 客户端库的“总头文件”

int main(int argc, char **argv) {                        // ② 标准 C++ 程序入口
  rclcpp::init(argc, argv);                              // ③ 初始化 ROS 2 通信基础设施

  auto node = std::make_shared<rclcpp::Node>("hello_node"); // ④ 创建一个名为 "hello_node" 的节点
  RCLCPP_INFO(node->get_logger(), "Hello ROS 2 from %s!",  // ⑤ 通过日志系统输出信息
              node->get_name());

  rclcpp::shutdown();                                    // ⑥ 关闭 ROS 2，释放资源
  return 0;                                              // ⑦ 程序正常退出
}

```


- 编译工程&执行程序
```bash
# 告知机器 ros2的位置 开机自启
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
# 确认
echo $ROS_DISTRO
```


```bash
# 回到工作区根目录
cd ~/ros2_ws/

# 编译工作区中的功能包
colcon build

# 配置环境变量
source install/setup.bash

# 运行节点
ros2 run my_first_pkg hello_node
```
- 用Launch操作多个节点 通过话题和服务实现节点通信

- 话题（Topic）：像广播电台，一个人说，很多人听。单向、异步、持续不断。

- 服务（Service）：像打电话，你问一句，对方答一句。双向、同步、一次性的。

### ROS2工作空间的结构
```
ros2_ws/          ← 工作空间根目录
├── src/          ← 所有功能包的源码必须放在这里！
│   ├── my_first_pkg/
│   └── my_second_pkg/
├── build/        ← colcon 自动生成
├── install/      ← colcon 自动生成
└── log/          ← colcon 自动生成
```
### 实战
- 修改src
- 修改CMakeLists和package.xml的依赖关系
```text
# CMakeLists下
# find dependencies
find_package(rclcpp REQUIRED)

# add_executable(hello_node src/hello_node.cpp)后
ament_target_dependencies(hello_node rclcpp)
```

```text
# package.xml中
<depend>rclcpp</depend>
```
- colcon build	要在工作空间根目录下执行
- 配置环境变量
```bash
source install/setup.bash
```
- 运行
```bash
ros2 run my_first_pkg hello.node
#ros2 run 功能包 节点
```
- 编译位置错误时
```bash
rm -rf build install log
rm -rf src/my_first_pkg/build src/my_first_pkg/install src/my_first_pkg/log
```

- AI总结
```bash
# 1. 每次开新终端，确认 ROS 2 环境
echo $ROS_DISTRO           # 应该输出 humble，没有就先 source

# 2. 创建工作空间（只需一次）
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake my_pkg

# 3. 写代码（CMakeLists.txt 顺序：find_package → add_executable → ament_target_dependencies）

# 4. 编译（永远在根目录）
cd ~/ros2_ws
colcon build

# 5. source 工作空间环境
source install/setup.bash

# 6. 运行（任何目录下都行）
ros2 run my_pkg my_node
```

```bash
source /opt/ros/humble/setup.bash       # 加载系统 ROS 2
source ~/ros2_ws/install/setup.bash     # 加载你的工作空间
```

```text
source 是 Linux 里的一个命令，它的作用用一句话说就是：

    在当前终端里“执行”一个脚本文件，让脚本里设置的环境变量、函数、别名，全部留在当前终端里生效。
```

# C++Node 和 rclcpp 基础
## rclcpp在c++中是什么？
1. library
- ROS Client Library for C++
- ROS2提供给C++开发者的工具箱，封装了C语言的rcl接口和DDS中间件
2. 命名空间Namespace
- 在C++代码中rclcpp是一个顶层命名空间
- eg1. rclcpp::Node, rclcpp::Publisher, Node和Publisher是rclcpp中的类
- eg2. rclcpp::init(), rclcpp::spin(), init()和spin()是定义在rclcpp中的全局函数
## ROS2中的Node详解
- Node 对象可以作为发布者 订阅者 服务端 客户端
- Node 对象作为发布者和服务端使用时，以回调的方式获取消息
```cpp
rclcpp::Node::SharedPtr node;
//  ^^^^^^  ^^^^  ^^^^^^^^^
//    (1)    (2)     (3)
```
- (1) `rclcpp::Node` 左边rclcpp是命名空间 Node是命名空间中的一个类
- (2) `Node::SharePtr` SharePtr是Node类内部定义的一个类型别名
```cpp
//SharePtr为何物
class Node {
public:
    using SharedPtr = std::shared_ptr<Node>;  //指向Node类的shared_ptr
    // ...
};
```

### 快速判断
- 看 :: 左边那个名字：
- 如果是小写、像包名/模块名的（rclcpp、std、std_msgs、msg）→ 通常是命名空间。
- 如果是大写开头、像类型名的（Node、Publisher、String）→ 通常是类。
- 这只是命名习惯，不是语法规则，但 ROS 2 和标准库基本都遵守。
```cpp
rclcpp::Node                    // 节点类
rclcpp::Publisher<T>            // 发布者模板类
rclcpp::Subscription<T>         // 订阅者模板类
rclcpp::Service<T>              // 服务端类
rclcpp::Client<T>               // 客户端类
rclcpp::TimerBase               // 定时器基类
rclcpp::Executor                // 执行器基类
rclcpp::SingleThreadedExecutor  // 单线程执行器
rclcpp::MultiThreadedExecutor   // 多线程执行器
rclcpp::Logger                  // 日志器类
rclcpp::Parameter               // 参数类
rclcpp::CallbackGroup           // 回调组类
rclcpp::Context                 // 上下文类
...
//rclcpp中的类和模板类
```

```cpp
//Node类常用的成员函数
class Node_ {
public:
    // 构造函数：指定节点名称，可选指定命名空间
    explicit Node(const std::string & node_name,
                  const std::string & namespace_ = "");

    // 创建发布者 (Publisher)
    template <typename MessageT>
    typename Publisher<MessageT>::SharedPtr
    create_publisher(const std::string & topic_name, size_t qos_depth);

    // 创建订阅者 (Subscription)
    template <typename MessageT, typename CallbackT>
    typename Subscription<MessageT>::SharedPtr
    create_subscription(const std::string & topic_name,
                        size_t qos_depth, CallbackT && callback);

    // 创建定时器 (Timer) - 基于系统时钟
    TimerBase::SharedPtr
    create_wall_timer(std::chrono::nanoseconds period,
                      std::function<void()> callback);

    // 创建服务端 (Service Server)
    template <typename ServiceT, typename CallbackT>
    typename Service<ServiceT>::SharedPtr
    create_service(const std::string & service_name, CallbackT && callback);

    // 创建客户端 (Service Client)
    template <typename ServiceT>
    typename Client<ServiceT>::SharedPtr
    create_client(const std::string & service_name);

    // 获取节点专属的日志记录器 (Logger)
    rclcpp::Logger get_logger() const;

    // 获取节点名称
    const char * get_name() const;

    // 获取节点的时钟 (用于时间同步)
    rclcpp::Clock::SharedPtr get_clock();
};
```
# Spin函数原理
### Node为什么能收发消息？是否自动？

1. Node类是一个"通信实体的载体"
- rclcpp::init()使得底层DDS自动接管网络发现和数据路由
2. Node对象调用API创建通信对象
- 发送`auto pub=node->create_publisher<MSgType>("topic_name",10);`  
在代码中显式调用pub->publish(msg) 将msg代表的消息发送出去
- 接收：`auto sub=node->create_subscription<MsgType>("topic_name",10,callback);`  
当消息到达时，DDS会自动把他放到结点的接收队列  
结点通过回调函数callback接收订阅的消息（回调函数可以是全局/成员/Lambda函数）  
Executor执行器通过rclcpp::spin(node)来不断轮询队列，取出消息msg并触发回调callback

## rclcpp::spin(node) 函数调用
- spin()是ROS2节点的事件循环驱动器，没有它，节点不执行回调
- spin()默认情况下是无限阻塞的，满足特定条件时会返回

| 触发方式 | 具体场景 | 底层原理 |
| :--- | :--- | :--- |
| 外部信号 | 用户在终端按下 Ctrl+C | ROS 2 底层注册了信号处理函数，捕获 SIGINT 后自动调用 rclcpp::shutdown()，导致 spin() 退出。 |
| 内部主动关闭 | 在节点的某个回调函数中，或者在另一个线程里调用了 rclcpp::shutdown() | 全局上下文被销毁，Executor 发现上下文无效，主动结束 spin 循环。 |
| 节点被取消/销毁 | 节点从 Executor 中被移除，或节点的智能指针引用计数归零被销毁 | Executor 发现没有需要管理的节点了，循环自然结束。 |

### 原理解析
### Node 应用代码
*   `create_wall_timer(...)`
    *   注册回调 + 绑定函数
*   `create_subscription(...)`
    *   注册回调 + 绑定函数
*   `create_service(...)`
    *   注册回调 + 绑定函数

⬇️ (注册到 ROS 2 运行时)

### ROS 2 运行时
*   **定时器队列**
    *   `callback_1, [500ms]`
*   **订阅队列**
    *   `callback_2, [msg1, msg2]`
*   **服务队列**
    *   `callback_2, [req1, req2]`

⬇️

### 事件循环
`rclcpp::spin(node);` ➔ Executor 事件循环

```cpp
while (rclcpp::ok())
{
    1. 检查所有队列，找到“就绪”的回调
    2. 取出回调，执行对应的函数
    3. 继续循环...
}
```

- `rclcpp::spin(node)`的本质就是一个不停轮询各个节点队列的循环，当发现队列不为空时，调用对应的回调函数
- 本质：创建一个SingleThreadedExecutor 然后把node交给他，开始无限循环执行回调
```cpp
rclcpp::spin(node);
//等价于
auto executor=std::make_shared<rclcpp::executors::SingleThreadedExecutor>();
//创建一个执行器
executor->add_node(node);

executor->spin(); //内部就是一个while循环，不断调度回调
```
### rclcpp::spin(node)家族成员
| 函数变体 | 阻塞特性 | 核心应用场景 |
| :--- | :--- | :--- |
| `spin(node)` | **无限阻塞** | 90% 的常规节点（如纯话题通信、定时器节点），直接托管给 ROS 2。 |
| `spin_some(node)` | **非阻塞（瞬时返回）** |观察消息队列里是否有消息，有则一次性取出并执行，如有新消息则不理会。 需要与外部事件循环（如 UI 框架、自定义 while 循环）融合的场景。 |
| `spin_all(node, time)` | **限时阻塞** |只循环time指定的时间，没处理完也返回。 需要在一个时间窗口内尽可能多地处理积压回调。 |

# 日志打印与智能指针应用