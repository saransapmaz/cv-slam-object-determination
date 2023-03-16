## Raspberry Pi Launch Dosyası (TR)

Bu ROS paketleri "publishalldata" launch dosyası için gereklidir.

1) LiDAR paketi farklı olabilir, doğru LiDAR ROS paketini yüklediğinize emin olun.
2) image_transport_plugins paketi sensor_msgs/Image ROS konusuna (topic) abone olmayı ya da sensor_msgs/Image ROS konusunu yayınlamayı etkinleştiren bir eklentidir. Ayrıntı için aşağıdaki linke tıklayınız: 
       
      https://github.com/ros-perception/image_transport_plugins

3) raspicam_node paketi Pi kamerasını kullanarak fotoğrafları ROS konusu (topic) şeklinde göndermeyi sağlar. Ayrıntı için aşağıdaki linke tıklayınız: 

      https://github.com/dganbold/raspicam_node.git
4) rosserial paketi Arduino ve ROS arasındaki bağlantının kurulmasını sağlar. Ayrıntı için aşağıdaki linke tıklayınız: 
 
      https://github.com/ros-drivers/rosserial

### Dosyanın çalıştırılması için gerekli olan ön aşamalar

 1) ROS Kinetic kullanımı için Raspbian Jessie, Stretch, Buster ya da Ubuntu 16.04 RPi üzerinde kurulu olmalıdır. (Teorik olarak ROS Melodic ile de çalışabilmektedir fakat hiç test edilmedi.)
    
    Raspberry Pi üzerine ROS Kinetic kurmak için lütfen siteden yardım alınız:

    http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi
 2) Kurulumdan sonra Raspberry Pi .bashrc dosyası düzenlenerek ROS Master olarak seçilmelidir.

    Terminal üzerine, alttaki satırı yazıp ENTER tuşuna basın.
    
        nano .bashrc
 
    Şu iki satırı dosyanın en sonuna doğru IP değerlerini girerek ekleyin.
 
        export ROS_MASTER_URI=http://IP of Raspberry Pi:11311
        export ROS_IP=IP of Raspberry Pi
    
    CTRL+X'e basarak kayddedin ve çıkın. Bu dosyayı aktifleştirmek için terminale aşağıdaki satırı yazın ve ENTER tuşuna basın.
 
        source .bashrc
 
    ROS'un doğru bir şekilde çalışıp çalışmadığını terminale "roscore" yazıp ENTER'a basarak kontrol edin. 
 
    Launch dosyası ROS ile ilgili bir problem yoksa terminal üzerinde çalıştırılabilir. Dosyayı çalıştırmadan önce launch dosyası içerisindeki gerekli düzenlemeleri yapın. 

## Raspberry Pi Launch File (EN)

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
 
    Add these two lines with correct IP at the end:
 
        export ROS_MASTER_URI=http://IP of Raspberry Pi:11311
        export ROS_IP=IP of Raspberry Pi
    
    Save and exit pressing CTRL+X. In onder to make the script work, write this line in terminal and press ENTER.
 
        source .bashrc
 
    Check if ROS is working typing in terminal "roscore". 
 
    The ".launch" file can be executed if ROS is working. Before the exucation, some lines may be updated regarding to your system. Open ".launch" file, and make necessary changes.
