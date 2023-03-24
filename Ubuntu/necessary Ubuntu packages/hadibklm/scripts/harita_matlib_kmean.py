#In order to combine map and objects, and avoiding repeating values, k-mean approach is applied.

import matplotlib.pyplot as plt
import pickle as pk
import scipy.cluster.vq as vq
import collections
import numpy as np
import math
xmap = []
ymap = []
xnesne = []
ynesne = []
nesne_isimleri = []
carpim = []
count = 0
toplam=0
toplamy = 0
yeninesne = []
goster = []
kaydetbakalim = []
kaydetbakalimy = []
yeni_nesne = []
xnesne_ = []
ynesne_ = []
yenix = 0
yenix2 = 0
yeniy = 0
yeniy2 = 0
kalan_nesne = []
kalan_nesne1 = []
res = {}
yeniyd = []
yeniy2d = []
ynesne1_ = []
toplamy = 0.0
yeni_nesnelerx_ = []
yeni_nesnelery_ = []
yeninesneler_ = []

print('Full file directory to map.pickle: "/home/user..../map.pickle" ')
file_path_map_pickle = input()
print('Full file directory to objects_xy.pickle: /home/user..../objects_xy.pickle: ')
file_path_nesne_xy = input()
with open (file_path_map_pickle, "rb") as file:
        loaded_dict_map = pk.load(file, encoding="bytes")



with open (file_path_nesne_xy, "rb") as file:
        loaded_dict_nesneler = pk.load(file, encoding="bytes")


xmap = loaded_dict_map[b'x1']
ymap = loaded_dict_map[b'y1']

xnesne = loaded_dict_nesneler['x']
ynesne = loaded_dict_nesneler['y']
print("How many objects do you expect to see? (max 6): ")
howmuch = input()

group_number = int(howmuch)
for i in range(len(xnesne)):
    carpim.append(ynesne[i]*-1)

nesne_isimleri = loaded_dict_nesneler['nesne_isimleri']
for i in range(len(nesne_isimleri)):
    if nesne_isimleri[i] != "bed" and nesne_isimleri[i] != "chair"  and nesne_isimleri[i] != "toilet"  and nesne_isimleri[i] != "diningtable" and nesne_isimleri[i] != "refrigerator" and nesne_isimleri[i] != "sink":
        yeni_nesnelerx_.append(xnesne[i])
        yeni_nesnelery_.append(ynesne[i])
        yeninesneler_.append(nesne_isimleri[i])

def matplotlib_opt(ymap,xmap):
    yeni_nesnelerx, yeni_nesnelery = ymap,xmap 
    min_x = np.min(np.array(yeni_nesnelerx))
    max_x = np.max(np.array(yeni_nesnelerx))
    min_y = np.min(np.array(yeni_nesnelery))
    max_y = np.max(np.array(yeni_nesnelery))
    dx = abs(max_x - min_x)
    dy = abs(max_y - min_y)
    cons = dy/dx
    #print(cons)
    k = 1
    print(cons)
    plt.rcParams["svg.fonttype"] = "none" #fontlari editable yap: LaTex icin calismiyor.
    plt.rc('axes', linewidth=1.5)
    plt.figure(figsize=(5*k*1-cons, 5*k*cons) ) #Cizim alanini ayarla
    #plt.figure(figsize=(5, 5)) #Cizim alanini ayarla

    plt.tick_params(direction='in', top=True, right=True, left = True, bottom = True) # Sag ve ustteki tickleri goster

def auto_cluster(data,threshold=0.1,k=group_number):
    # There are more sophisticated ways of determining k
    # See http://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set
    data=np.asarray(data)
    distortion=1e20
    while distortion>threshold:
        codebook,distortion=vq.kmeans(data,k)
        k+=1   
    code,dist=vq.vq(data,codebook)    
    groups=collections.defaultdict(list)
    for index,datum in zip(code,data):
        groups[index].append(datum)
    return groups


kaydetbakalim = [yeni_nesnelerx_, yeni_nesnelery_, yeninesneler_]
groupsx=auto_cluster(yeni_nesnelerx_,threshold=0.05,k=group_number)
#groupsy=auto_cluster(ynesne,threshold=0.1,k=4)
for index,data in enumerate(sorted(groupsx.values(),key=lambda d: np.mean(d))):
    #print('{i}: {d}'.format(i=index,d=data))
    try:
        if index == 0:
            for k in range(len(data)):
                toplam = toplam + data[k]
            yenix = toplam/len(data)
            #print(yenix)
            xnesne_.append(yenix)
            #print(kaydetbakalim)
            k = 0
            for k in range(len(kaydetbakalim[0])):
                
                if kaydetbakalim[0][k]<= yenix+0.1 and kaydetbakalim[0][k]>= yenix-0.1:
                    yeni_nesne.append(kaydetbakalim[2][k])
                    toplamy = toplamy + kaydetbakalim[1][k]
                    ynesne1_.append(kaydetbakalim[1][k])
                
            
            ynesne_.append(toplamy / len(ynesne1_))
            #print("yeni_nesne", yeni_nesne)
            kalan_nesne = [*set(yeni_nesne)]
            
            #print(len(kalan_nesne))
            if len(kalan_nesne)>1:
                print("_________________________________________________________")
                #print("Aynı konum için birden fazla nesne tespit edildi.")
                print("Multiple objects are detected for the same location.")
                for k in yeni_nesne:
                    res[k] = yeni_nesne.count(k)
                A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
                #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
                print("Objects detected and number of the detection: \n",A)
                sira = len(A) - 1
                gondergitsin = A[sira][0]
                #b = turkce_isimler(gondergitsin)
                #kalan_nesne1.append(b)
                kalan_nesne1.append(gondergitsin)
                #print("En çok tespit edilen nesne:\n ",gondergitsin)
                print("The most detected object:\n ",gondergitsin)
                #print(len())
            else:
                print("_________________________________________________________")
                #print("Sadece bir nesne tespit edildi.")
                print("Only one object is detected.")
                for k in yeni_nesne:
                    res[k] = yeni_nesne.count(k)
                A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
                
                gondergitsin = kalan_nesne[0]
                #b = turkce_isimler(gondergitsin)
                #kalan_nesne1.append(b)
                kalan_nesne1.append(gondergitsin)
                #print("Tespit edilen nesne: ", b)
                #print("Tespit edilme miktarı: ", A[0][1])
                print("The detected object: ", gondergitsin)
                print("Amount of detection: \n", A[0][1])
            toplam = 0
    except ZeroDivisionError:
        xnesne_.pop()
        pass
    if index == 1:
        yenix = 0
        toplam = 0
        toplamy = 0
        ynesne1_ = []
        yeni_nesne = []
        for k in range(len(data)):
            toplam = toplam + data[k]
        yenix = toplam/len(data)
        xnesne_.append(yenix)
        k = 0
        for k in range(len(kaydetbakalim[0])):
            
            if kaydetbakalim[0][k]<= yenix+0.1 and kaydetbakalim[0][k]>= yenix-0.1 :

                yeni_nesne.append(kaydetbakalim[2][k])
                toplamy = toplamy + kaydetbakalim[1][k]
                ynesne1_.append(kaydetbakalim[1][k])
        ynesne_.append(toplamy/len(ynesne1_))
        #print("yeni_nesne", yeni_nesne)
        kalan_nesne = [*set(yeni_nesne)]
        #print(len(kalan_nesne))
        if len(kalan_nesne)>1:
            print("_________________________________________________________")
            #print("Aynı konum için birden fazla nesne tespit edildi.")
            print("Multiple objects are detected for the same location.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
            print("Objects detected and number of the detection: \n",A)
            sira = len(A) - 1
            gondergitsin = A[sira][0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print(ynesne_)
            #print("En çok tespit edilen nesne:\n ",b)
            print("The most detected object:\n ",gondergitsin)

            #print(len())
        else:
            print("_________________________________________________________")
            #print("Sadece bir nesne tespit edildi.")
            print("Only one object is detected.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            
            gondergitsin = kalan_nesne[0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print("Tespit edilen nesne: ", b)
            print("The detected object: ", gondergitsin)
            #print("Tespit edilme miktarı: ", A[0][1])
            print("Amount of detection: \n", A[0][1])
        toplam = 0
    if index == 2:
        yenix = 0
        toplam = 0
        toplamy = 0
        ynesne1_ = []
        yeni_nesne = []
        for k in range(len(data)):
            toplam = toplam + data[k]
        yenix = toplam/len(data)
        xnesne_.append(yenix)
        k = 0
        for k in range(len(kaydetbakalim[0])):
            
            if kaydetbakalim[0][k]<= yenix+0.2  and kaydetbakalim[0][k]>= yenix-0.2 :

                yeni_nesne.append(kaydetbakalim[2][k])
                toplamy = toplamy + kaydetbakalim[1][k]
                ynesne1_.append(kaydetbakalim[1][k])
        ynesne_.append(toplamy/len(ynesne1_))
        #print("yeni_nesne", yeni_nesne)
        kalan_nesne = [*set(yeni_nesne)]
        #print(len(kalan_nesne))
        if len(kalan_nesne)>1:
            print("_________________________________________________________")
            print("Multiple objects are detected for the same location.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
            print("Objects detected and number of the detection: \n",A)
            sira = len(A) - 1
            gondergitsin = A[sira][0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print(ynesne_)
            #print("En çok tespit edilen nesne:\n ",b)
            print("The most detected object:\n ",gondergitsin)
            
        else:
            print("_________________________________________________________")
            #print("Sadece bir nesne tespit edildi.")
            print("Only one object is detected.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            
            gondergitsin = kalan_nesne[0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print("Tespit edilen nesne: ", b)
            print("The detected object: ", gondergitsin)
            #print("Tespit edilme miktarı: ", A[0][1])
            print("Amount of detection: \n", A[0][1])
        toplam = 0
    if index == 3:
        yenix = 0
        toplam = 0
        toplamy = 0
        ynesne1_ = []
        yeni_nesne = []
        for k in range(len(data)):
            toplam = toplam + data[k]
        yenix = toplam/len(data)
        xnesne_.append(yenix)
        k = 0
        for k in range(len(kaydetbakalim[0])):
            
            if kaydetbakalim[0][k]<= yenix+0.05  and kaydetbakalim[0][k]>= yenix-0.05 :

                yeni_nesne.append(kaydetbakalim[2][k])
                toplamy = toplamy + kaydetbakalim[1][k]
                ynesne1_.append(kaydetbakalim[1][k])
        ynesne_.append(toplamy/len(ynesne1_))
        #print("yeni_nesne", yeni_nesne)
        kalan_nesne = [*set(yeni_nesne)]
        #print(len(kalan_nesne))
        if len(kalan_nesne)>1:
            print("_________________________________________________________")
            print("Multiple objects are detected for the same location.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
            print("Objects detected and number of the detection: \n",A)
            sira = len(A) - 1
            gondergitsin = A[sira][0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print(ynesne_)
            #print("En çok tespit edilen nesne:\n ",b)
            print("The most detected object:\n ",gondergitsin)

            #print(len())
        else:
            print("_________________________________________________________")
            #print("Sadece bir nesne tespit edildi.")
            print("Only one object is detected.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            
            gondergitsin = kalan_nesne[0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print("Tespit edilen nesne: ", b)
            print("The detected object: ", gondergitsin)
            #print("Tespit edilme miktarı: ", A[0][1])
            print("Amount of detection: \n", A[0][1])
        toplam = 0
    if index == 4:
        yenix = 0
        toplam = 0
        toplamy = 0
        ynesne1_ = []
        yeni_nesne = []
        for k in range(len(data)):
            toplam = toplam + data[k]
        yenix = toplam/len(data)
        xnesne_.append(yenix)
        k = 0
        for k in range(len(kaydetbakalim[0])):
            
            if kaydetbakalim[0][k]<= yenix+0.2  and kaydetbakalim[0][k]>= yenix-0.2 :

                yeni_nesne.append(kaydetbakalim[2][k])
                toplamy = toplamy + kaydetbakalim[1][k]
                ynesne1_.append(kaydetbakalim[1][k])
        ynesne_.append(toplamy/len(ynesne1_))
        #print("yeni_nesne", yeni_nesne)
        kalan_nesne = [*set(yeni_nesne)]
        #print(len(kalan_nesne))
        if len(kalan_nesne)>1:
            print("_________________________________________________________")
            print("Multiple objects are detected for the same location.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
            print("Objects detected and number of the detection: \n",A)
            sira = len(A) - 1
            gondergitsin = A[sira][0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print(ynesne_)
            #print("En çok tespit edilen nesne:\n ",b)
            print("The most detected object:\n ",gondergitsin)
        else:
            print("_________________________________________________________")
            #print("Sadece bir nesne tespit edildi.")
            print("Only one object is detected.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            
            gondergitsin = kalan_nesne[0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print("Tespit edilen nesne: ", b)
            print("The detected object: ", gondergitsin)
            #print("Tespit edilme miktarı: ", A[0][1])
            print("Amount of detection: \n", A[0][1])
        toplam = 0
    if index == 5:
        yenix = 0
        toplam = 0
        toplamy = 0
        ynesne1_ = []
        yeni_nesne = []
        for k in range(len(data)):
            toplam = toplam + data[k]
        yenix = toplam/len(data)
        xnesne_.append(yenix)
        k = 0
        for k in range(len(kaydetbakalim[0])):
            
            if kaydetbakalim[0][k]<= yenix+0.2 and kaydetbakalim[0][k]>= yenix-0.2:

                yeni_nesne.append(kaydetbakalim[2][k])
                toplamy = toplamy + kaydetbakalim[1][k]
                ynesne1_.append(kaydetbakalim[1][k])
        ynesne_.append(toplamy/len(ynesne1_))
        #print("yeni_nesne", yeni_nesne)
        kalan_nesne = [*set(yeni_nesne)]
        #print(len(kalan_nesne))
        if len(kalan_nesne)>1:
            print("_________________________________________________________")
            print("Multiple objects are detected for the same location.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
            print("Objects detected and number of the detection: \n",A)
            sira = len(A) - 1
            gondergitsin = A[sira][0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print(ynesne_)
            #print("En çok tespit edilen nesne:\n ",b)
            print("The most detected object:\n ",gondergitsin)

            #print(len())
        else:
            print("_________________________________________________________")
            #print("Sadece bir nesne tespit edildi.")
            print("Only one object is detected.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            
            gondergitsin = kalan_nesne[0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print("Tespit edilen nesne: ", b)
            print("The detected object: ", gondergitsin)
            #print("Tespit edilme miktarı: ", A[0][1])
            print("Amount of detection: \n", A[0][1])
        toplam = 0
    if index == 6:
        yenix = 0
        toplam = 0
        toplamy = 0
        ynesne1_ = []
        yeni_nesne = []
        for k in range(len(data)):
            toplam = toplam + data[k]
        yenix = toplam/len(data)
        xnesne_.append(yenix)
        k = 0
        for k in range(len(kaydetbakalim[0])):
            
            if kaydetbakalim[0][k]<= yenix+0.2 and kaydetbakalim[0][k]>= yenix-0.2:

                yeni_nesne.append(kaydetbakalim[2][k])
                toplamy = toplamy + kaydetbakalim[1][k]
                ynesne1_.append(kaydetbakalim[1][k])
        ynesne_.append(toplamy/len(ynesne1_))
        #print("yeni_nesne", yeni_nesne)
        kalan_nesne = [*set(yeni_nesne)]
        #print(len(kalan_nesne))
        if len(kalan_nesne)>1:
            print("_________________________________________________________")
            print("Multiple objects are detected for the same location.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            #print("Tespit edilen nesneler ve tespit edilme miktarları: \n",A)
            print("Objects detected and number of the detection: \n",A)
            sira = len(A) - 1
            gondergitsin = A[sira][0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print(ynesne_)
            #print("En çok tespit edilen nesne:\n ",b)
            print("The most detected object:\n ",gondergitsin)


            #print(len())
        else:
            print("_________________________________________________________")
            #print("Sadece bir nesne tespit edildi.")
            print("Only one object is detected.")
            for k in yeni_nesne:
                res[k] = yeni_nesne.count(k)
            A = sorted(res.items(), key=lambda item: item[1]) #degere gore siraladim
            
            gondergitsin = kalan_nesne[0]
            #b = turkce_isimler(gondergitsin)
            kalan_nesne1.append(gondergitsin)
            #print("Tespit edilen nesne: ", b)
            print("The detected object: ", gondergitsin)
            #print("Tespit edilme miktarı: ", A[0][1])
            print("Amount of detection: \n", A[0][1])
        toplam = 0

matplotlib_opt(ymap, xmap)
plt.plot(ymap,xmap,".")
plt.xlabel('x-axis (m)')
plt.ylabel('y-axis (m)')
plt.plot(0,0, "ro")
#plt.plot(0.17, -0.6, "g*")
#plt.plot(0.6, 0.01, "g*")
plt.xticks(np.arange(-10, 10, 0.5), rotation=90)

plt.yticks(np.arange(-10, 10, 0.5))

plt.plot(xnesne_, ynesne_, "m*")
#plt.plot(xnesne_,ynesne_,"g*")
#for i in range(len(goster)):
    #yeni_nesne.append(goster[i][2])
    #xnesne_.append(goster[i][0])
    #ynesne_.append(goster[i][1])

print("*****************************************************************")
#print("1. nesnenin gercek konumu (x, y): ", (0.17, -0.6 ))
#print("2. nesnenin gercek konumu (x, y): ", (0.6, 0.01 ))
for i, label in enumerate(kalan_nesne1):
    plt.annotate(label, (xnesne_[i],ynesne_[i]), fontsize=14)
    #print(str(i+1)+". nesnenin algoritma ile bulunan konumu (x, y) metre: ({:.3f}".format(xnesne_[i]),"{:.3f}".format(ynesne_[i]),")")
    print(str(i+1)+". coordinates (x, y) m: ({:.3f}".format(xnesne_[i]),"{:.3f}".format(ynesne_[i]),")")
#print("*****************************************************************")
#s1x = abs(xnesne_[0]-0.17)
#s1y = abs(ynesne_[0]+0.6)
#s2x = abs(xnesne_[1]-0.6)
#s2y = abs(ynesne_[1]-0.01)

#print("1. nesnenin sapma oranı (x, y) metre: ({:.3f}".format(s1x), "{:.3f}".format(s1y),")")
#print("2. nesnenin sapma oranı (x, y) metre: ({:.3f}".format(s2x), "{:.3f}".format(s2y),")")
#plt.plot(xnesne_, ynesne_, "r*")
print("*****************************************************************")
plt.show()
