# Opencv kütüphanes
import cv2

# 'image.jpeg' yerine sizin proje klasörüne eklediğiniz resmin adı ve uzantısı
# Burda cv2.IMREAD_GRAYSCALE sayesinde resim gri tonlamalı olarak okunur
img = cv2.imread('image.jpeg',cv2.IMREAD_GRAYSCALE)

# Resim 500 x 500 piksel boyutunda boyutlandırılır
resized = cv2.resize(img, (500,500),interpolation = cv2.INTER_LINEAR)

# Resimler ekranda gösterilir
cv2.imshow('image',img)
cv2.imshow('resized',resized)

cv2.waitKey(0)
cv2.destroyAllWindows()