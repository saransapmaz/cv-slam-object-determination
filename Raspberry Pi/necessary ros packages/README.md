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
 
 *Raspbian Jessie, Stretch, Buster or Ubuntu 16.04 should be installed on RPi in order to use ROS Kinetic. (It may work on ROS Melodic, never has been tried.)
 
 To install ROS Kinetic in RPi, please see the official tutorial link:
 
   http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi
 
 *After the installation, Raspberry Pi should be marked as ROS Master by editing .bashrc file.

 In a terminal, write this line: 
    
    nano .bashrc
 
 Add these two lines with correct IP at the end:
 
    export ROS_MASTER_URI=http://IP of Raspberry Pi:11311
    export ROS_IP=IP of Raspberry Pi
    
 Save and exit pressing CTRL+X. In onder to make the script work, write this line in terminal and press ENTER.
 
    source .bashrc
 
 Check if ROS is working typing in terminal "roscore". 
 
 The ".launch" file can be executed if ROS is working. Before the exucation, some lines may be updated regarding to your system. Open ".launch" file, and make necessary changes.
