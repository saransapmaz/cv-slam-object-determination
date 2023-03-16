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


#distance5

def iteration():
    global k
    k = k+1
    return k
def foo():
    global now, rastgele
    now = time.time()
def listener():
    global new_msg, msg,msg2, msg3, cv_image, sol20, sag20, trans
    rospy.init_node('navig')
    #move = Twist()
    #koordinat = TransformListener
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    laser = message_filters.Subscriber('/scan', LaserScan)
    pose = message_filters.Subscriber('/slam_out_pose', PoseStamped)
    image = message_filters.Subscriber('/raspicam_node/image_raw', Image)
    #transform = message_filters.Subscriber('/tf', TFMessage)
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
    
    #print("MAP",trf.transforms[0].header.frame_id) # == /map
    #print("CHILD",trf.transforms[0].child_frame_id) # == /base_link
    #print(trf.transforms[0].transform.translation.x) # xtranslation
    #print(trf.transforms[0].transform.translation.x) # ytranslation

    xt = trans.transform.translation.x
    yt = trans.transform.translation.y
    fi_degreex = trans.transform.rotation.x
    fi_degreey = trans.transform.rotation.y
    fi_degreez = trans.transform.rotation.z
    fi_degreew = trans.transform.rotation.w
    #print("*yt*__,",yt)
    
        
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
    #pozisyon = []
    #print("BIRR")
    
    
    global sol20, sag20, pozisyon,x_coords,y_coords, dosya_adi, a, b,xnesne, ynesne, xuz, filename, msg2
    #time.sleep(1)
    try:
        a = min(sol20)
        b = min(sag20)
        
        #print("x", x)
        siny = 2* (fi_degreew * fi_degreez + fi_degreey * fi_degreex)
        cosy = 1 - 2 * (fi_degreey*fi_degreey+fi_degreez*fi_degreez)
        angles = math.atan2(siny,cosy) #formuldeki fi degeri
        
        print("**************",angles)
        #time.sleep(0.25)
        if a<b and a!=0 and b!=0 and a<1.0 and a>0.4 :
            #print("IKIII")
            for i in range(len(sol20)):
                #print(a)
                #print(i)
                if sol20[i] == a:
                    #print("sol? ",a)
                    #print(i)
                    print("burada miyim? ------ 1")
                    print("**************",angles)
                    filename = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen'+str(iteration())+'.jpg'
                    cropped_image = cv_image[0:480, 240:400]
                    cv2.imwrite(filename, cropped_image)
                    print(i)

                    xrn = a*math.sin(math.radians(90-i))
                    yrn = a*math.sin(math.radians(i))
                    

                    x1 = (xrn*math.cos(math.radians(math.degrees(angles)))) - (yrn*math.sin(math.radians(math.degrees(angles))))
                    y1 = (xrn*math.sin(math.radians(math.degrees(angles)))) + (yrn*math.cos(math.radians(math.degrees(angles))))

                    
                    xnesne = x1 + xt
                    ynesne = y1 + yt
                    
                    #y = msg2[1]+(a)*math.sin(math.radians(i))
                    #print("uzunluk",a)
                    print("xrn",xrn)
                    print("yrn",yrn)
                    print("x1", x1)
                    print("y1", y1)
                    print("xnesne",xnesne)
                    print("ynesne",ynesne)
                    print("yt",yt)
                    print("xt",xt)
                    
                    dosya_adi.append(filename)
                    x_coords.append(xnesne)
                    y_coords.append(ynesne)
                    #print(a)
                    #time.sleep(0.25)
                    #print(x_coords)
                    
                    
        if a>b and a!=0 and b!=0 and b<1.0 and b>0.4 :
            #print("UCCC")
            
            for i in range(len(sag20)):
                #print(i)
                #print(b)
                if sag20[i] == b:
                    print("burada miyim? ------ 2")
                    print("**************",angles)
                    #print("sag? ", b)
                    #print(339+i)
                    filename = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen'+str(iteration())+'.jpg'
                    cropped_image = cv_image[0:480, 240:400]
                    cv2.imwrite(filename, cropped_image)
                    
                    #Rotation = np.matrix([[math.cos(math.radians(349+i)), -math.sin(math.radians(349+i)), 0],
                    #                      [math.sin(math.radians(349+i)), math.cos(math.radians(349+i)), 0],
                    #                      [0, 0, 1]])
                    #print(Rotation)
                    #Translation = np.matrix([[1, 0, a], [0,1,0],[0, 0, 1]])
                    #print(Translation)
                    #slam_out = np.matrix([msg2[0],msg2[1],1])
                    #sonuc = np.dot(slam_out, Rotation)
                    #sonuc2 = sonuc + np.array([a,0,0])
                    #array_cevir = sonuc2.getA()
                    dosya_adi.append(filename)
                    print(filename)
                    
                    xrn = b*math.sin(math.radians(90-i))
                    yrn = -b*math.sin(math.radians(i))

                    x1 = (xrn*math.cos(math.radians(math.degrees(angles)))) - (yrn*math.sin(math.radians(math.degrees(angles))))
                    y1 = (xrn*math.sin(math.radians(math.degrees(angles)))) + (yrn*math.cos(math.radians(math.degrees(angles))))
            
                    xnesne = x1 + xt
                    ynesne = y1 + yt
                    print("xrn",xrn)
                    print("yrn",yrn)
                    print("x1", x1)
                    print("y1", y1)
                    print("xnesne_2",xnesne)
                    print("ynesne_2",ynesne)
                    print("yt",yt)
                    print("xt",xt)
                    x_coords.append(xnesne)
                    y_coords.append(ynesne)
                    #print(a)
                    #time.sleep(0.25)
                    #print(x_coords)
                    #print(y_coords)
        if a==0 or b==0:
            a = a+10
            b = b+10
            print("aslinda ben yogum")
            #time.sleep(0.25)
                        
            #print(x)             
            #dosya_adi.append(filename)
            #x_coords.append(x)
            #y_coords.append(y)
    except ValueError or NameError:
        print("OLU BOLGE")
        pass
       
    sol20 = []
    sag20 = []
    msg2 = []
    xnesne=0.0
    ynesne=0.0
    #print("x=====", x)
          
    

if __name__ == '__main__':

    print("Veriler toplaniyor...")

    listener()
    print("Veriler kaydediliyor...")
    my_dict = {
        'dosya_adi': dosya_adi,
        'x_koordinatlari': x_coords,
        'y_koordinatlari': y_coords
        }
    with open("/home/saran/catkin_ws/src/hadibklm/scripts/kullandigimkodlar/resimler_xy.pickle", "wb") as file:
        pk.dump(my_dict, file, pk.HIGHEST_PROTOCOL)

    with open("/home/saran/catkin_ws/src/hadibklm/scripts/kullandigimkodlar/resimler_xy.pickle", "rb") as file:
        loaded_dict = pk.load(file)

    #print(loaded_dict)
    
    print("Veriler kaydedildi.")
