#include "rclcpp/rclcpp.hpp"
#include<iostream>
int main(int argc,char** argv)
{
    rclcpp::init(argc,argv);   
    //also a namespace
    auto node=std::make_shared<rclcpp::Node>("cpp_node");
    RCLCPP_INFO(node->get_logger(),"Hello cpp node! ");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}