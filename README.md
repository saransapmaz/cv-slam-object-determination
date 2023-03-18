# cv-slam-object-determination

Projenin amacı bilgisayarlı görü ile eş zamanlı haritalama ve lokalizasyon tekniklerini birleştirerek obje tanımlaması yapmaktır.
Özel yapım otonom gezgin robot SLAM tekniği kullanarak iç mekanın haritasını ekrana yansıtırken aynı zamanda kendisine yakın olan engellerin fotoğrafını çeker ve tanımlama yapmak için kaydeder.
Tüm nesneleri gördüğünden emin olduktan sonra algoritma durdurulur ve o ana kadar çekilmiş olan fotoğraflarla, engellerin ya da nesnelerin muhtemel yerleriyle beraber kaydedilir.
Bu fotoğraflar, Python 3.x'in OpenCV ile birlikte kurulduğu sanal ortam içerisinde değiştirilmiş YOLO v3 Python kodu ile işlemden geçirilir. Bu bir nevi nesneleri anlamsız bilgilerden arındırma işlemidir.
Tanımlanmış nesneler ve konumları matplotlib kütüphanesi kullanılarak oluşturulan harita üzerinde belirir.

Haritalama tekniği olarak Hector SLAM kullanılmıştır. Hector SLAM tekniği ROS Kinetic ile birlikte kullanılmış ve Ubuntu 16.04 üzerine kurulmuştur. Daha fazla bilgi için
link aşağıdadır.

http://wiki.ros.org/hector_slam

Bilgisayarlı görü için YOLO v3 tercih edilmiştir. Aşağıdaki linkten yararlanılmıştır.

https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html

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





