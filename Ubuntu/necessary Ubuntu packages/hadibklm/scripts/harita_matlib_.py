import matplotlib.pyplot as plt
import pickle as pk
import numpy as np
import scipy.cluster.vq as vq
import collections

xmap = []
ymap = []
xnesne = []
ynesne = []
nesne_isimleri = []
carpim = []
yeni_nesnelerx =[]
yeni_nesnelery =[]
yeninesneler = []
with open ("/home/saran/catkin_ws/src/hadibklm/scripts/kullandigimkodlar/mekan1.pickle", "rb") as file:
        loaded_dict_map = pk.load(file, encoding="bytes")
def matplotlib_opt(ymap,xmap):
    yeni_nesnelerx, yeni_nesnelery = ymap,xmap 
    min_x = np.min(np.array(yeni_nesnelerx))
    max_x = np.max(np.array(yeni_nesnelerx))
    min_y = np.min(np.array(yeni_nesnelery))
    max_y = np.max(np.array(yeni_nesnelery))
    dx = abs(max_x - min_x)
    dy = abs(max_y - min_y)
    cons = dx / dy
    k = 0.5
    plt.rcParams["svg.fonttype"] = "none" #fontlari editable yap: LaTex icin calismiyor.
    plt.rc('axes', linewidth=1.5)
    plt.figure(figsize=(5 * abs(cons) * k, 5  * abs(cons) * k) ) #Cizim alanini ayarla
    #plt.figure(figsize=(5, 5)) #Cizim alanini ayarla

    plt.tick_params(direction='in', top=True, right=True, left = True, bottom = True) # Sag ve ustteki tickleri goster



with open ("/home/saran/catkin_ws/src/hadibklm/scripts/pickle/nesne_xy.pickle", "rb") as file:
        loaded_dict_nesneler = pk.load(file, encoding="bytes")

xmap = loaded_dict_map[b'x1']
ymap = loaded_dict_map[b'y1']

xnesne = loaded_dict_nesneler['x']
ynesne = loaded_dict_nesneler['y']

def matplotlib_opt(ymap,xmap):
    yeni_nesnelerx, yeni_nesnelery = ymap,xmap 
    min_x = np.min(np.array(yeni_nesnelerx))
    max_x = np.max(np.array(yeni_nesnelerx))
    min_y = np.min(np.array(yeni_nesnelery))
    max_y = np.max(np.array(yeni_nesnelery))
    dx = abs(max_x - min_x)
    dy = abs(max_y - min_y)
    cons = dx/dy
    #print(cons)
    k = 0.5
    plt.rcParams["svg.fonttype"] = "none" #fontlari editable yap: LaTex icin calismiyor.
    plt.rc('axes', linewidth=1.5)
    plt.figure(figsize=(5 * abs(cons) * k, 5  * abs(cons) * k) ) #Cizim alanini ayarla
    #plt.figure(figsize=(5, 5)) #Cizim alanini ayarla

    plt.tick_params(direction='in', top=True, right=True, left = True, bottom = True) # Sag ve ustteki tickleri goster



for i in range(len(xnesne)):
    carpim.append(ynesne[i]*-1)
print(xnesne)
print("****")
print(ynesne)
nesne_isimleri = loaded_dict_nesneler['nesne_isimleri']
karisik = [xnesne, ynesne, nesne_isimleri]

for i in range(len(nesne_isimleri)):
    if nesne_isimleri[i] != "bed" and nesne_isimleri[i] != "chair"  and nesne_isimleri[i] != "toilet"  and nesne_isimleri[i] != "diningtable"and nesne_isimleri[i] != "refrigerator":
        yeni_nesnelerx.append(xnesne[i])
        yeni_nesnelery.append(ynesne[i])
        yeninesneler.append(nesne_isimleri[i])
matplotlib_opt(ymap, xmap)
plt.xlabel('x-ekseni')
plt.ylabel('y-ekseni')

plt.plot(ymap,xmap,".")
plt.plot(0,0, "r*")
plt.plot(yeni_nesnelerx, yeni_nesnelery, "g*")
for i, label in enumerate(yeninesneler):
    plt.annotate(label, (yeni_nesnelerx[i],yeni_nesnelery[i]))
plt.show()


