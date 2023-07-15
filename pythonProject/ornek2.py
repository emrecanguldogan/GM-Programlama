import cv2
import numpy as np


# 'image.jpeg' yerine sizin proje klasörüne eklediğiniz resmin adı ve uzantısı
cap = cv2.imread('image.jpeg')
frame = cap
# Burda cv2.COLOR_BGR2HSV sayesinde resim BGR (BLUE GREEN RED) renk uzayından HSV renk uzayına dönüştürülür
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

"""_, frame = cap.read()
# It converts the BGR color space of image to HSV color space
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
"""

"""
# Threshold of blue in HSV space
lower_blue = np.array([60, 35, 140])
upper_blue = np.array([180, 255, 255])
"""

# Yeşil renk aralığı (HSV renk uzayında)
lower_blue = np.array([30, 100, 100])  # Minimum ton, doygunluk ve parlaklık değerleri
upper_blue = np.array([70, 255, 255])  # Maksimum ton, doygunluk ve parlaklık değerleri

# preparing the mask to overlay
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Matematiksel kıyaslama yapılır eğer piksel rengi belirtilen renk aralığında değilse
# rengi siyah yapılır eğer belirtilen renk aralığındaysa rengi olduğu gibi korunur
result = cv2.bitwise_and(frame, frame, mask=mask)

# Resimler ekranda gösterilir
cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
