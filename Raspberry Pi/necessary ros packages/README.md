## Raspberry Pi Launch File

These ROS packages are required for "publishalldata" launch file.

1) LiDAR package can be different for each custom mobile robot, so ensure to have correct LiDAR ROS package version.
2) image_transport_plugins package is a plugin that enables publishing and subscribing to sensor_msgs/Image. See the link below:
   https://github.com/ros-perception/image_transport_plugins
3) raspicam_node package enables Pi camera to publish image ROS topics. See the link below:
   https://github.com/saransapmaz/cv-slam-object-determination/tree/main/Raspberry%20Pi/necessary%20ros%20packages/raspicam_node
4) rosserial package is a tool for connecting Arduino to ROS. See the link below:
   https://github.com/saransapmaz/cv-slam-object-determination/tree/main/Raspberry%20Pi/necessary%20ros%20packages/rosserial

