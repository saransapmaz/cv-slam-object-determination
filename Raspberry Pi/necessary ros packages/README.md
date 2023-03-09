## Raspberry Pi Launch File

These ROS packages are required for "publishalldata" launch file.

1) LiDAR package can be different for each custom mobile robot, so ensure to have correct LiDAR ROS package version.
2) image_transport_plugins package is a plugin that enables publishing and subscribing to sensor_msgs/Image. See the link below:
       
      https://github.com/ros-perception/image_transport_plugins
3) raspicam_node package enables Pi camera to publish image ROS topics. See the link below:

      https://github.com/dganbold/raspicam_node.git
    
4) rosserial package is a tool for connecting Arduino to ROS. See the link below:
 
      https://github.com/ros-drivers/rosserial
   
 ### Prerequisites
 
 1) Raspbian Jessie, Stretch, Buster or Ubuntu 16.04 should be installed on RPi in order to use ROS Kinetic. (It may work on ROS Melodic, never has been tried.)
 
 To install ROS Kinetic in RPi, please see the official tutorial link:
 
   http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi
 
 2) After the installation, Raspberry Pi should be marked as ROS Master by editing .bashrc file.

 In a terminal, write this line: 
    
    nano .bashrc
 
 Add these two lines at the end:
 
    export ROS_MASTER_URI=http://IP of Raspberry Pi:11311
    export ROS_IP=IP of Raspberry Pi
    
 Save and exit pressing CTRL+X. All devices connected to same Wi-Fi now can communicate through ROS Master by publishing or subscribing.
