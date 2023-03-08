#!/usr/bin/env python
import cv2
from cv_bridge import CvBridge, CvBridgeError
import rospy
import time
import geometry_msgs.msg as gm
from geometry_msgs.msg import PoseStamped
from sensor_msgs import msg
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import PointCloud2
import std_msgs.msg
from sensor_msgs.msg import Image
import sensor_msgs.point_cloud2 as pcl2
from visualization_msgs.msg import Marker
import subprocess
import pickle as pk
import message_filters
import math
import numpy as np


now = time.time()
bridge = CvBridge()
i = 0
msg = 0.0
msg2 = []
cv_image = []
sol20 = []
sag20 = []
c = []
x_coords = []
y_coords = []
dosya_adi = []
x = 0.0
y = 0.0
a= 0.0
b = 0.0
#distance5

def iteration():
    global i
    i = i+1
    return i
def foo():
    global now, rastgele
    now = time.time()
def listener():
    global new_msg, msg,msg2, msg3, cv_image, sol20, sag20
    rospy.init_node('navig')
    #move = Twist()
    laser = message_filters.Subscriber('/scan', LaserScan)
    pose = message_filters.Subscriber('/slam_out_pose', PoseStamped)
    image = message_filters.Subscriber('/raspicam_node/image_raw', Image)
    ts = message_filters.ApproximateTimeSynchronizer([laser, pose, image],1,1,1)
    ts.registerCallback(callback)
    

    r = rospy.Rate(100)
    while not rospy.is_shutdown():
        #rospy.loginfo(msg)
        r.sleep()

def callback(sensor, pozisyon, foto):
    global msg, msg2, cv_image, sol20, sag20, sol20_, sag20_

    
    for i in range(10):
        
        sag20.append(sensor.ranges[339+i])
        sol20.append(sensor.ranges[i])
        
    
    msg2 = [pozisyon.pose.position.x, pozisyon.pose.position.y, pozisyon.pose.position.z]
    try:
      global cv_image
      cv_image = bridge.imgmsg_to_cv2(foto, "bgr8")
      
    except CvBridgeError as e:
      print(e)
    kaydet()


      
    

def kaydet():
    #pozisyon = []
    filename = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen'+str(iteration())+'.jpg'
    
    
    global sol20, sag20, pozisyon,x_coords,y_coords, dosya_adi,x ,y,a, b

    c_time = time.time()
    e_time = c_time - now
    #cv2.imsho w("Image window", cv_image)
    cropped_image = cv_image[0:480, 250:390]
    cv2.imwrite(filename, cropped_image)
    
              
    #time.sleep(1)
   
    a = min(sol20)
    b = min(sag20)
    
    
    if a<b:
        for i in range(10):
            if sol20[i] == a:
                #print("sol? ",a)
                #print(i)
                Rotation = np.matrix([[math.cos(math.radians(i)), -math.sin(math.radians(i)), 0],
                                      [math.sin(math.radians(i)), math.cos(math.radians(i)), 0],
                                      [0, 0, 1]])
                #print(Rotation)
                Translation = np.matrix([[1, 0, a], [0,1,0],[0, 0, 1]])
                #print(Translation)
                slam_out = np.matrix([msg2[0],msg2[1],1])
                sonuc = np.dot(slam_out, Rotation)
                sonuc2 = sonuc + np.array([a,0,0])
                array_cevir = sonuc2.getA()
                x = array_cevir[0][0]
                y = array_cevir[0][1]
                print(y)
                #x_coords.append(x)
                #y_coords.append(y)
                
                #print(x_coords)
                
                
    if a>b:
        for i in range(10):
            if sag20[i] == b:
                #print("sag? ", b)
                #print(339+i)
                Rotation = np.matrix([[math.cos(math.radians(339+i)), -math.sin(math.radians(339+i)), 0],
                                      [math.sin(math.radians(339+i)), math.cos(math.radians(339+i)), 0],
                                      [0, 0, 1]])
                #print(Rotation)
                Translation = np.matrix([[1, 0, a], [0,1,0],[0, 0, 1]])
                #print(Translation)
                slam_out = np.matrix([msg2[0],msg2[1],1])
                sonuc = np.dot(slam_out, Rotation)
                sonuc2 = sonuc + np.array([a,0,0])
                array_cevir = sonuc2.getA()
                x = array_cevir[0][0]
                y = array_cevir[0][1]
                print(y)
                
                #print(x_coords)
                #print(y_coords)
                   
        print("x",x)            
        dosya_adi.append(filename)
        x_coords.append(x)
        y_coords.append(y)


    

if __name__ == '__main__':

    print("1")

    listener()
    my_dict = {
        'dosya_adi': dosya_adi,
        'x_koordinatlari': x_coords,
        'y_koordinatlari': y_coords
        }
    with open("/home/saran/catkin_ws/src/hadibklm/scripts/kullandigimkodlar/resimler_xy.pickle", "wb") as file:
        pk.dump(my_dict, file, pk.HIGHEST_PROTOCOL)

    #with open("resimler_xykoordinatlari.pickle", "rb") as file:
        #loaded_dict = pk.load(file)

    #print(type(loaded_dict))

    print("6")
