In order to use the algorithm the requirements should be satisfied:

1) ROs Kinetic should be installed on both Linux-dependent machines (laptop and RPi).

***Desktop-full install are recommended. 

Installation ROs Kinetic on Ubuntu 16.04 laptop:
http://wiki.ros.org/kinetic/Installation/Ubuntu

Installation ROs Kinetic on RPi strecth :
http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi



2. Both machines should be connected to same Wi-Fi network.
3. IPs of both machines should be declared.
4. Only one of the machines can be chosen as ROs master.
5. On ROs master machine the following steps should be followed:

   5.1. On a new terminal write and ENTER:
        gedit .bashrc (or nano .bashrc)
   5.2. Edit and add these two lines at the end of the file:
        export ROS_MASTER_URI=http://IP of ROs master:11311
        export ROS_IP=IP of ROs master

6. On other ROs machine the following steps should be followed:

   6.1. On a new terminal write and ENTER:
        gedit .bashrc (or nano .bashrc)
   6.2. Edit and add these two lines at the end of the file:
        export ROS_MASTER_URI=http://IP of ROs master:11311
        export ROS_IP=IP of ROs machine

7. Install the code for ROs master





