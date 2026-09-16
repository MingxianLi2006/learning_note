#CMakeLists.txt
cmake_minimum_required(VERSION 3.12)
project(demo VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

add_executable(demo main.cpp)
target_link_libraries(demo PRIVATE ${OpenCV_LIBS})
