cmake_minimum_required(VERSION 3.8)
project(ros2_cpp)

find_package(rclcpp REQUIRED)   # find the dependencies for the ROS2 C++ client library
message(STATUS $(rclcpp_INCLUDE_DIRS))# find the relevannt header and library
message(STATUS $(rclcpp_LIBRARIES))
#library file and the library file that rclcpp depends
add_executable(ros2_cpp_node ros2_cpp_node.cpp)

target_include_directories(ros2_cpp_node PUBLIC ${rclcpp_INCLUDE_DIRS}) # header link
target_link_libraries(ros2_cpp_node ${rclcpp_LIBRARIES})#library link
