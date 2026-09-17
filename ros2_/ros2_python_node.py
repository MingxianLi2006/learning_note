#!/usr/bin/env python3
#第一个节点python示例
import rclpy
from rclpy.node import Node

def main():
	rclpy.init()
	node=Node("Python_node")
	node.get_logger().info('你好Python节点！')
	#日志打印
	rclpy.spin(node)
	rclpy.shutdown()

if __name__=="__main__":
	main()

