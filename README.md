# cv-slam-object-determination (EN)

The aim of the project is to combine hector SLAM and YOLO v3 in order to detect small objects. It is possible to create the map using hector SLAM with custom made autonomous robot and take photos of nearby objects or obstacles. Those pictures are stored with its possible coordinates to process them by one one using YOLO v3. The map is projected to Python environment to show objects within. 

Further information about hector SLAM is in the link below:

http://wiki.ros.org/hector_slam

Further information about YOLO v3 is in the link below:

https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html

The codes and the packages that are used/created can be found in the link below:

https://github.com/saransapmaz/cv-slam-object-determination/tree/main/Ubuntu/necessary%20Ubuntu%20packages/cv-slam-object-determination
## Results

The rooms where the codes are executed can be seen left side of the picture. The pictures in the middle refer to RViz maps. N1, N2, R coordinate systems were added manually which are not random, to show objects and robot. All robotic calculations were made using these coordinate systems. The map is created using ROS topic called "/map" that is basically an array with 0, -1 and +100 (free, unexplored, obstacle). The pictures in the right side are the results that show objects.

![image](https://user-images.githubusercontent.com/126087406/226407378-4a3e3da8-1d65-4d23-9262-53610c1159ab.png)

## The Autonomous Custom Made Robot

<p float="left">
  <img src="https://user-images.githubusercontent.com/126087406/226122983-7e3175f6-46da-4510-a850-c12682e7f927.jpeg" width="250" />
  <img src="https://user-images.githubusercontent.com/126087406/226122986-a32fc508-554c-4276-93a4-fb09ef812a4a.jpeg" width="250" /> 
  <img src="https://user-images.githubusercontent.com/126087406/226122991-dc0e91ce-af6c-4bef-9d92-c69d2a0995b9.jpeg" width="250" />
</p>

Robot consists of two chassis. On the top chassis there are LiDAR, Raspberry Pi 3B+, Pi Camera, and 4 batteries; on the lower chassis there are powerbank, 4 batteries, Arduino UNO, L298N (motor driver), two DC motors and one caster wheel. 8 batteries are connected as serial, powerbank is used to power Raspberry Pi, and Arduino, Pi Camera, LiDAR are connected to Raspberry Pi. All connection is in the picture below: 

<img src="https://user-images.githubusercontent.com/126087406/226122543-f0a357a1-963d-42a1-aca1-6b752c0daef8.png"  width="500">

# cv-slam-object-determination (TR)

Projenin amacı bilgisayarlı görü ile eş zamanlı haritalama ve lokalizasyon tekniklerini birleştirerek küçük boyuttaki objelerin tanımlamasını yapmaktır.
Özel yapım otonom gezgin robot SLAM tekniği kullanarak iç mekanın haritasını ekrana yansıtırken aynı zamanda kendisine yakın olan engellerin fotoğrafını çeker ve tanımlama yapmak için kaydeder.
Tüm nesneleri gördüğünden emin olduktan sonra algoritma durdurulur ve o ana kadar çekilmiş olan fotoğraflarla, engellerin ya da nesnelerin muhtemel yerleriyle beraber kaydedilir.
Bu fotoğraflar, Python 3.x'in OpenCV ile birlikte kurulduğu sanal ortam içerisinde değiştirilmiş YOLO v3 Python kodu ile işlemden geçirilir. Bu bir nevi nesneleri anlamsız bilgilerden arındırma işlemidir.
Tanımlanmış nesneler ve konumları matplotlib kütüphanesi kullanılarak oluşturulan harita üzerinde belirir.

Haritalama tekniği olarak Hector SLAM kullanılmıştır. Hector SLAM tekniği ROS Kinetic ile birlikte kullanılmış ve Ubuntu 16.04 üzerine kurulmuştur. Daha fazla bilgi için
link aşağıdadır.

http://wiki.ros.org/hector_slam

Bilgisayarlı görü için YOLO v3 tercih edilmiştir. Aşağıdaki linkten yararlanılmıştır.

https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html

Oluşturulmuş kodlar ve diğer tüm detaylar için lütfen aşağıdaki linke tıklayınız.

https://github.com/saransapmaz/cv-slam-object-determination/tree/main/Ubuntu/necessary%20Ubuntu%20packages/hadibklm


## Örnek Sonuçlar


En soldaki fotoğraflar nesnelerin bulunduğu odaları göstermektedir. İkinci haritada N1, N2 ve R düzlemleri anlaşılabilirlik açışından manuel olarak eklenmiştir ve her biri koordinat sistemini temsil etmektedir. Hiçbir koordinat düzlemi rastgele değildir, hesaplamalar bu sistemlere göre yapılmıştır. RViz programı üzerinde çıkan bu harita, /map konusu üzerinden bir dizi (array) olarak dönmektedir. Bu özelliği kullanarak Python 3.x üzerinde üçüncü haritalar oluşturulmuştur. Gerçek odaların karşılığının haritalar üzerinde anlaşılabilmesi için göz alıcı renklerde şekiller kullanılarak ifade edilmiştir.

![image](https://user-images.githubusercontent.com/126087406/226407378-4a3e3da8-1d65-4d23-9262-53610c1159ab.png)


## Kullanılan Otonom Gezgin Robot
<p float="left">
  <img src="https://user-images.githubusercontent.com/126087406/226122983-7e3175f6-46da-4510-a850-c12682e7f927.jpeg" width="250" />
  <img src="https://user-images.githubusercontent.com/126087406/226122986-a32fc508-554c-4276-93a4-fb09ef812a4a.jpeg" width="250" /> 
  <img src="https://user-images.githubusercontent.com/126087406/226122991-dc0e91ce-af6c-4bef-9d92-c69d2a0995b9.jpeg" width="250" />
</p>


Robot iki iskeletten oluşmaktadır. Üst tarafında LiDAR sensörü, Raspberry Pi 3B+, kamera ve 4 tane pil; alt kısmında ise taşınabilir şarj cihazı, 4 tane pil, Arduino, motor sürücü ve motorlar bulunmaktadır.
8 tane 1.1V yeniden doldurabilir piller seri bir şekilde bağlanmıştır ve motor sürücüyü güçlendirmek için kullanılmıştır. Taşınabilir şarj cihazı ise sabit 2A, 5V çıkışlıdır ve Raspberry Pi'yı güçlendirmek için
kullanılmıştır. Bağlantı şeması şu şekildedir:

<img src="https://user-images.githubusercontent.com/126087406/226122543-f0a357a1-963d-42a1-aca1-6b752c0daef8.png"  width="500">





