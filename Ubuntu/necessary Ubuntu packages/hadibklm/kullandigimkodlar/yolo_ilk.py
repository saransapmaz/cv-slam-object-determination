import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2 as cv
import time
import numpy as np
import os
import pickle as pk




WHITE = (255, 255, 255)
img = None
img0 = None
outputs = None
nesne_isimleri = []
path = []
x_ = []
y_ = []
dosya_yolu = ""
xs = []
ys = []
xkor = 0.0
ykor = 0.0

with open ("/home/saran/catkin_ws/src/hadibklm/scripts/kullandigimkodlar/resimler_xy.pickle", "rb") as file:
        loaded_dict2 = pk.load(file, encoding="bytes")

xs = loaded_dict2[b'x_koordinatlari']
ys = loaded_dict2[b'y_koordinatlari']



classes = open('/home/saran/catkin_ws/src/hadibklm/darknet/data/coco.names').read().strip().split('\n')
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')
#img = cv.imread('/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen1.jpg')

#cv.imshow('window',  img)
#cv.waitKey(1)
net = cv.dnn.readNetFromDarknet('/home/saran/catkin_ws/src/hadibklm/darknet/cfg/yolov3.cfg', '/home/saran/catkin_ws/src/hadibklm/yolo/yolov3.weights')


ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# construct a blob from the image


def load_image(path, xkor, ykor):
    global img, img0, outputs, ln

    img0 = cv.imread(path)
    img = img0.copy()
    
    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)
    t0 = time.time()
    outputs = net.forward(ln)
    t = time.time() - t0

    # combine the 3 output groups into 1 (10647, 85)
    # large objects (507, 85)
    # medium objects (2028, 85)
    # small objects (8112, 85)
    outputs = np.vstack(outputs)
    xdeneme = xkor
    ydeneme = ykor
    post_process(img, outputs, 0.75, xdeneme, ydeneme)
    cv.imshow('window',  img)
    cv.displayOverlay('window', f'forward propagation time={t:.3}')
    cv.waitKey(0)


def post_process(img, outputs, conf, xdeneme, ydeneme):
    global nesne_isimleri, x_, y_
    H, W = img.shape[:2] #img shape[0] height, img shape[1] width
    
    #print((W/180)*70)
    boxes = []
    confidences = []
    classIDs = []

    for output in outputs:
        scores = output[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > conf:
            x, y, w, h = output[:4] * np.array([W, H, W, H])
            
            p0 = int(x - w//2), int(y - h//2)
            p1 = int(x + w//2), int(y + h//2)
            boxes.append([*p0, int(w), int(h)])
            confidences.append(float(confidence))
            classIDs.append(classID)
            # cv.rectangle(img, p0, p1, WHITE, 1)

    indices = cv.dnn.NMSBoxes(boxes, confidences, conf, conf-0.1)
    if len(indices) > 0:
        for i in indices.flatten():
            
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in colors[classIDs[i]]]
            cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
            #a = check_class_id(classes[classIDs[i]])
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            print(classes[classIDs[i]])
            if classes[classIDs[i]]!= "sofa" or classes[classIDs[i]]!= "bed" or classes[classIDs[i]]!= "person" or classes[classIDs[i]]!= "book":
                path.append(dosya_yolu)
                x_.append(xdeneme)
                y_.append(ydeneme)
                nesne_isimleri.append(classes[classIDs[i]])
            
            cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    #else:
        #os.remove(dosya_yolu)

def check_class_id(x): 
    if x == "bottle":
        yeni_isim = "sise"
    if x == "sofa":
        yeni_isim = "koltuk"
    if x == "book":
        yeni_isim = "kitap"
    if x == "chair":
        yeni_isim = "sandalye"
    if x == "person":
        yeni_isim = "insan"
    if x == "pottedplant":
        yeni_isim = "saksı"
    if x == "laptop":
        yeni_isim = "laptop"
        
    
    return yeni_isim
        

def trackbar(x):
    global img, xkor, ykor
    conf = x/100
    img = img0.copy()
    post_process(img, outputs, conf)
    cv.displayOverlay('window', f'confidence level={conf}')
    cv.imshow('window', img)

cv.namedWindow('window')
cv.createTrackbar('confidence', 'window', 50, 100, trackbar)


for i in range(len(xs)):
   
    dosya_yolu = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen'+str(i+1)+'.jpg'
    xkor = xs[i]
    ykor = ys[i]
    load_image(dosya_yolu,xkor,ykor)
        
        
    

#dosya_yolu = '/home/saran/catkin_ws/src/hadibklm/resimler/kaydedilen37.jpg'
#load_image(dosya_yolu)
print(x_)

my_dict3 = {
    #'dosya_adi': path,
    'nesne_isimleri': nesne_isimleri,
    'x' : x_,
    'y' : y_
    }
with open("/home/saran/catkin_ws/src/hadibklm/scripts/kullandigimkodlar/nesne_xy.pickle", "wb") as file:
        pk.dump(my_dict3, file, pk.HIGHEST_PROTOCOL)


cv.destroyAllWindows()


