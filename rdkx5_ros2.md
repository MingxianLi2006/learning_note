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

