#!/usr/bin/python

import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from nav_msgs.msg import OccupancyGrid
from sensor_msgs.msg import LaserScan
import numpy as np
from nav_msgs.msg import MapMetaData
import matplotlib.pyplot as plt
import pickle as pk
x1 = []
y1 = []
dx = []
dy = []
ayy = []
width = 0.0
height = 0.0
resolution = 0.0
def getCoords(msg1):
    global x1
    global y1
    global x1_max
    global y1_max
    global ayy
    global width
    global height
    global resolution
    x1 = []
    y1 = []
    width = msg1.info.width #pixel
    height = msg1.info.height
    resolution = msg1.info.resolution
    orijin = msg1.info.origin
    print(orijin)
    ayy = msg1
    
    #cell_x = x / resolution
    #print(len(msg1.data[:]))
    for i in range(width):
        for j in range(height):
            if msg1.data[i*width+j]==100:

                x1.append(((i*resolution + (resolution/2)-25.6249980927)))
                y1.append(((j*resolution + (resolution/2)-25.6249980927)))


rospy.init_node("yesyes")

sub_map = rospy.Subscriber('/map', OccupancyGrid, getCoords)


rospy.sleep(2)
r = rospy.Rate(10)

for i in range(len(x1)):
    dx.append(-1*x1[i])
    dy.append(-1*y1[i])
    
if ayy != []:
    #print(ayy)
    my_dict3 = {
        "x1": x1,
        "y1": y1
        }
    
    #CHANGE THE FOLDER NAME
    with open("/home/saran/catkin_ws/src/hadibklm/scripts/pickle/map.pickle", "wb") as file:
        pk.dump(my_dict3, file, pk.HIGHEST_PROTOCOL)
    plt.plot(y1,x1,".")
    plt.show()
        
        

r.sleep()