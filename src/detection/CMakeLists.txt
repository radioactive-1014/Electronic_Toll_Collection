cmake_minimum_required(VERSION 2.8.3)
project(detection)

## Add support for C++11, supported in ROS Kinetic and newer
# add_definitions(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  roscpp
  rospy
  sensor_msgs
  std_msgs
image_transport
)
find_package( OpenCV  REQUIRED )

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})
add_executable(talker src/image_pub.cpp)
add_executable(listner src/image_sub.cpp)

target_link_libraries(talker ${catkin_LIBRARIES})
target_link_libraries(talker ${OpenCV_LIBRARIES})

target_link_libraries(listner ${catkin_LIBRARIES})
target_link_libraries(listner ${OpenCV_LIBRARIES})
