#####################################################################
#
#
#
# Yazar         : Emrecan Guldogan
#
# Tarih         : Temmuz 2021
#
# Dosya         : SimpleRedDetection.py
#
# Yazım Dili    : Python
#
# Aciklama      : Kirmizi rengi algılayan ve nesnenin kirmizi olup 
#                 olmadiğini goruntuye ve terminal e yazdıran program.
#		
#####################################################################

# OpenCV ve numpy kutuphaneleri programa cagrilir.
import cv2 as cv
import numpy as np

# OpenCV nin goruntu yakalama class i cap değişkenine atanir.
cap = cv.VideoCapture(0)

# Dongu belirlenen klavye tusuna basilmadikca calisir.
while(1):
    # VideoCapture class indan read cagrilarak imagFrame degiskenine goruntu array vektoru olarak kaydedilir.
    # Ayrintili bilgi icin OpenCV VideoCapture dokumantasyonunu inceleyiniz.
    _, imageFrame = cap.read()
    
    # imageFrame e kaydedilen anlik goruntunun RGB/BGR renk degerlerini 0-180 degerleri arasindaki 
    # HSV renk degerlerine cevrilir ve hsv_frame e yazilir.
    hsv_frame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
    
    #Kirmizi renginin HSV deger araliklari tanimlanir. 
    #low_red = np.array([95,50,150])
    low_red = np.array([75, 100, 100])
    high_red = np.array([130,255,255])

    # OpenCV inrange fonksiyonu ile hsv donusumu yapilmis goruntunun belirlenen renk araligindaki
    # pikseller red_mask goruntu array vektorune kaydedilir.
    red_mask = cv.inRange(hsv_frame, low_red, high_red)

    # Numpy in nonzero fonksiyonu ile red_mask daki sifir olmayan elemanlarin 
    # (kirmizi piksellerin) kordinatlari 1x2 lik matris olarak hesaplanir.
    # Numpy in sum fonksiyonu ile bu degerler toplanarak sum degiskeniine kaydedilir.
    sum = np.sum(np.nonzero(red_mask))

    # Asagidaki yazim kirmizi piksel sayisini saymak icin kullanilabilir.
    # count=len(np.transpose(np.nonzero(red_mask)))

    #Toplam 0 dan farkliysa terminale "Red" degilse "Not Red" yazdirilir.
    if sum == 0:
        #
        print("Not Red")
    else:
        print("Red")

    print("")

    # OpenCV nin findContours fonksiyonu ile kirmizi renkli objenin konturlerinin kordinatlarini contours degiskenine kaydedilir.
    # Ayrintili bilgi icin OpenCV nin findCountours dokumantasyonunu inceleyiniz.
    contours, hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    #Contour icindeki tum elemanlarin sayisi kadar calisir.
    for pic, contour in enumerate(contours, start=0): 
        #Countour un alanini hesaplar.
        area = cv.contourArea(contour) 
        # Eger alan 300 den buyukse goruntude en buyuk kirmizi objenin 
        # etrafina kare cizdirir ve "Kirmizi" yazisini yazdirir.
        if(area > 500):
            x, y, w, h = cv.boundingRect(contour) 
            imageFrame = cv.rectangle(imageFrame, (x, y),  (x + w, y + h),  (0, 0, 255), 2) 
              
            cv.putText(imageFrame, "Kirmizi", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
    # OpenCV nin imshow fonksiyonu ile orjinal goruntu,kirmizi filtrelenmis goruntu ekrana yazdirilir.        
    cv.imshow('frame',imageFrame)
    cv.imshow('mask',red_mask)
    
    # Esc tusuna basildiginda acik tum pencereler ve kamera kapatilir.Program sonlandirilir.

    k=cv.waitKey(1) & 0xFF

    if k == 27:
        cap.release() 
        cv.destroyAllWindows()
        break
