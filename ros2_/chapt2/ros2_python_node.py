import rclpy    #import a library
from rclpy.node import Node

def main():
    rclpy.init()  #initialize the ROS2 communication
    node = Node('python_node')  #create a ROS2 node
    node.get_logger().info('Hello Python Node!')
    node.get_logger().warn('Hello Python Node! This is a warning message.')
    rclpy.spin(node)  #keep the node running
    rclpy.shutdown()  #shutdown the ROS2 communication

if __name__ == '__main__':
    main()  #call the main function
