#!/usr/bin/env python
import cv2
from cv_bridge import CvBridge, CvBridgeError
import rospy
import time
import geometry_msgs.msg as gm
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Transform
from tf2_msgs.msg import TFMessage
import tf2_ros
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
k = 0
msg = 0.0
msg2 = []
cv_image = []
sol20 = []
sag20 = []
c = []
x_coords = []
y_coords = []
dosya_adi = []
xnesne = 0.0
ynesne = 0.0
xt = 0.0
yt = 0.0
fi_degreex = 0.0
fi_degreey = 0.0
fi_degreez = 0.0
fi_degreew = 0.0
xuz = 0.0
a= 0.0
b = 0.0
def iteration():
    global k
    k = k+1
    return k

def listener():
    global new_msg, msg,msg2, msg3, cv_image, sol20, sag20, trans
    rospy.init_node('navig')
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    laser = message_filters.Subscriber('/scan', LaserScan)
    pose = message_filters.Subscriber('/slam_out_pose', PoseStamped)
    image = message_filters.Subscriber('/raspicam_node/image_raw', Image)
    ts = message_filters.ApproximateTimeSynchronizer([laser, pose, image],1,1,1)
    ts.registerCallback(callback)
    
    

    r = rospy.Rate(1000)
    while not rospy.is_shutdown():
         try:
            trans = tfBuffer.lookup_transform("map", "base_link", rospy.Time())
         except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            r.sleep()
            continue
    

def callback(sensor, pozisyon, foto):
    global msg, msg2, cv_image, sol20, sag20, sol20_, sag20_, xt, yt, fi_degreex, fi_degreey, fi_degreez, fi_degreew
    
    xt = trans.transform.translation.x
    yt = trans.transform.translation.y
    fi_degreex = trans.transform.rotation.x
    fi_degreey = trans.transform.rotation.y
    fi_degreez = trans.transform.rotation.z
    fi_degreew = trans.transform.rotation.w
    
    for i in range(10):
        if sensor.ranges[349+i]!=0:
            sag20.append(sensor.ranges[349+i])
        if sensor.ranges[i]!=0:
            sol20.append(sensor.ranges[i])

    msg2 = [pozisyon.pose.position.x, pozisyon.pose.position.y, pozisyon.pose.position.z]
            #pozisyon.pose.orientation.x,pozisyon.pose.orientation.y,pozisyon.pose.orientation.z,pozisyon.pose.orientation.w]
    try:
      global cv_image
      cv_image = bridge.imgmsg_to_cv2(foto, "bgr8")
      
    except CvBridgeError as e:
      print(e)
    kaydet()


def kaydet():
    
    global sol20, sag20, pozisyon,x_coords,y_coords, dosya_adi, a, b,xnesne, ynesne, xuz, filename, msg2
    #time.sleep(1)
    try:
        a = min(sol20)  #Find minimum distance left side of sensor
        b = min(sag20)  #Find minimum distance right side of sensor
        
        #print("x", x)
        siny = 2* (fi_degreew * fi_degreez + fi_degreey * fi_degreex)
        cosy = 1 - 2 * (fi_degreey*fi_degreey+fi_degreez*fi_degreez)
        angles = math.atan2(siny,cosy) #formuldeki fi degeri
        
        #print("**************",angles)
        
        if a<b and a!=0 and b!=0 and a<1.0 and a>0.4 :
           
            for i in range(len(sol20)):
                #a and b present minimum distance values of left and right front of the sensor. 
                #if the obstable is near to left side of the robot, this loop is triggered.
                
                if sol20[i] == a:
                    
                    #CHANGE THE FOLDER DIRECTORY
                    #filename = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen'+str(iteration())+'.jpg'
                    filename = filenamee + str(iteration())+'.jpg'
                    cropped_image = cv_image[0:480, 240:400] #Crop the original image
                    cv2.imwrite(filename, cropped_image)
                   
                    #ROTATION MATRIX
                    xrn = a*math.sin(math.radians(90-i))
                    yrn = a*math.sin(math.radians(i))
                    #TRANSLATION MATRIX
                    x1 = (xrn*math.cos(math.radians(math.degrees(angles)))) - (yrn*math.sin(math.radians(math.degrees(angles))))
                    y1 = (xrn*math.sin(math.radians(math.degrees(angles)))) + (yrn*math.cos(math.radians(math.degrees(angles))))

                    
                    xnesne = x1 + xt # x of the obstable
                    ynesne = y1 + yt # y of the obstable
                
                    #print("xnesne",xnesne)
                    #print("ynesne",ynesne)
                    print("yt",yt)
                    print("xt",xt)
                    
                    dosya_adi.append(filename)
                    x_coords.append(xnesne)
                    y_coords.append(ynesne)
                     
        if a>b and a!=0 and b!=0 and b<1.0 and b>0.4 :
            #a and b present minimum distance values of left and right front of the sensor. 
            #if the obstable is near to right side of the robot, this loop is triggered.
            
            for i in range(len(sag20)):
                if sag20[i] == b:
                       
                    # CHANGE THE FOLDER DIRECTORY
                    #filename = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen'+str(iteration())+'.jpg'
                    filename = filenamee + str(iteration())+'.jpg'
                    cropped_image = cv_image[0:480, 240:400] # Crop the original size photo
                    cv2.imwrite(filename, cropped_image) # Save it to file predetermined
                    dosya_adi.append(filename) # Append the matrix which contains file names
                    #print(filename)
                    
                    #ROTATION MATRIX
                    xrn = b*math.sin(math.radians(90-i))
                    yrn = -b*math.sin(math.radians(i))
                    #TRANSLATION MATRIX
                    x1 = (xrn*math.cos(math.radians(math.degrees(angles)))) - (yrn*math.sin(math.radians(math.degrees(angles))))
                    y1 = (xrn*math.sin(math.radians(math.degrees(angles)))) + (yrn*math.cos(math.radians(math.degrees(angles))))
            
                    xnesne = x1 + xt  # x of the obstable
                    ynesne = y1 + yt  # y of the obstable
                    
                    #print("xnesne_2",xnesne)
                    #print("ynesne_2",ynesne)
                   
                    x_coords.append(xnesne)
                    y_coords.append(ynesne)
                   
  
    except ValueError or NameError: 
        print("Dead Zone") # Dead zone
        pass
       
    sol20 = []
    sag20 = []
    msg2 = []
    xnesne=0.0
    ynesne=0.0
    #print("x=====", x)

if __name__ == '__main__':
    print("Where do you want to store the pictures? Please enter a full directory: ")
    filenamee = input()
    print("Pictures will be stored in "+filenamee)
    print("Data are being collected...") 

    listener() # ROS function
    print("Data are being saved...") 
    my_dict = {
        'dosya_adi': dosya_adi, #file name
        'x_koordinatlari': x_coords, #x_coordinates
        'y_koordinatlari': y_coords  #y_coordinates
        }
    
    #change the directory
    print("Where do you want to store the pictures.pickle file? Please enter a full directory including pictures.pickle: ")
    pics = input()
    with open(pics, "wb") as file:
        pk.dump(my_dict, file, pk.HIGHEST_PROTOCOL)
    
    print("Data saved.") 
