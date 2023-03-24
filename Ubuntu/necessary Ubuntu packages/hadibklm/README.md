### PREREQUESTS

In order to use the algorithm the requirements should be satisfied:

1. ROS Kinetic should be installed on both Linux-dependent machines (laptop and RPi).

***Desktop-full install are recommended. 

Installation ROs Kinetic on Ubuntu 16.04 laptop:
http://wiki.ros.org/kinetic/Installation/Ubuntu

Installation ROs Kinetic on RPi strecth :
http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi

2. Both machines should be connected to same Wi-Fi network.
3. IPs of both machines should be declared.
4. Raspberry Pi is to be set as master.
5. On ROS master machine the following steps should be followed:

   5.1. On a new terminal write and ENTER:
        nano .bashrc
   5.2. Edit and add these two lines at the end of the file:
        export ROS_MASTER_URI=http://IP of ROS master:11311
        export ROS_IP=IP of ROS master

6. On other ROS machine the following steps should be followed:

   6.1. On a new terminal write and ENTER:
        gedit .bashrc
   6.2. Edit and add these two lines at the end of the file:
        export ROS_MASTER_URI=http://IP of ROS master:11311
        export ROS_IP=IP of ROS machine

7. Create a catkin workspace properly on both machines.
8. On Raspberry Pi, please download all these packages in /home/user/your catkin ws in RPi/src, then build with "catkin_make -j1" command in terminal.

https://github.com/saransapmaz/cv-slam-object-determination/tree/main/Raspberry%20Pi/necessary%20ros%20packages

9. On Ubuntu, please download all these packages in "/home/user/your catkin ws in Ubuntu/src", then build with "catkin_make" command in terminal.

https://github.com/saransapmaz/cv-slam-object-determination/tree/main/Ubuntu/necessary%20Ubuntu%20packages

10. Before launching any codes, it is required that you chance some lines regarding to your own system. 

   10.1. Change footprint to regarding to your robot at line 3 on Ubuntu.
   
         https://github.com/saransapmaz/cv-slam-object-determination/blob/main/Ubuntu/necessary%20Ubuntu%20packages/hadibklm/config/costmap_common_params.yaml
         
   10.2. Change port name of Arduino according to your own system on Raspberry Pi.
   
         Number of line: 10.
         https://github.com/saransapmaz/cv-slam-object-determination/blob/main/Raspberry%20Pi/necessary%20ros%20packages/publishalldata.launch
     
   10.3. Finally make sure to have the Arduino code below:
   
         https://github.com/saransapmaz/cv-slam-object-determination/blob/main/rosdeneme.ino
         
       
11. You can consider following these steps to install side by Python 3.7 with OpenCV. This is very important because ROS Kinetic is only dependent to Python 2.7, and YOLO v3 Python code can not be executed. 

https://towardsdatascience.com/building-python-source-with-opencv-and-opencv-contrib-ba95d709eb

### STEP BY STEP 
         
1. Through ssh reach Raspberry Pi's terminal and start roscore.
2. In another terminal ssh to Pi, and roslaunch the file.

       https://github.com/saransapmaz/cv-slam-object-determination/blob/main/Raspberry%20Pi/necessary%20ros%20packages/publishalldata.launch
       
3. On Ubuntu, roslaunch the file.

       https://github.com/saransapmaz/cv-slam-object-determination/blob/main/Ubuntu/necessary%20Ubuntu%20packages/hadibklm/launch/harita_navigasyon.launch
       
4. On Ubuntu, write at terminal, and ENTER. At this point, RViz application should appear with some coordinate systems. Don't interrupt the code until the robot stops moving. Once the robot stop, you are free to use RViz 2D Nav Tool on the upper side of the application, and point the robot any destination within map.
       
       rosrun hadibklm collecter.py
         
5. THIS IS IMPORTANT: As you are done exploring the environment, please stop the code by typing CTRL + C in terminal where "collecter.py" is working. You should see "Veriler kaydediliyor..."
6. Do NOT close RViz application, in another terminal please type below command and ENTER. Until a picture appears, do NOT interrupt. Once you see a map, in same terminal type CTRL + C, and close.

        rosrun hadibklm map_reading2.py
        
7. Activate virtual environment in another terminal, and cd to scripts (example):
        
        cd /home/username/workspacename/src/hadibklm/scripts
     
8. Then type this command in same terminal:

        python yolo_.py

9. As pictures appear on screen, hold any key until any pictures left.
10. Last step, type this command in terminal:

        python harita_matlib_kmean.py
       
