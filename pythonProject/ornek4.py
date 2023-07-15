# OpenCv ,numpy ve matematik kutuphaneleri programa cagrilir.
import cv2
import numpy as np
import math

# OpenCV nin goruntu yakalama class i değişkene atanir.
cap = cv2.VideoCapture(1)

# Video codec formati tanimlanir.
fourrcc = cv2.VideoWriter_fourcc(*'XVID')
# Video ismi kayit formati fps i ve pencere boyutu (pixel) belirlenir.
videoKayit = cv2.VideoWriter('video3.avi', fourrcc, 40.0, (640, 480))
videoKayit2 = cv2.VideoWriter('video4.avi', fourrcc, 40.0, (640, 480))


def gamma_trans(img, gamma):  # gamma fonksiyonu tanimlanir.
    gamma_table = [np.power(a / 255.0, gamma) * 255.0 for a in range(256)]  # Renk tablosu tanimlanir.
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # Renk degeri tam sayi (integer) dır.
    return cv2.LUT(img,
                   gamma_table)
    # Isik yogunlugu (renk) homojonize edilerek goruntude iyilestirme yapilmaya calisilir.


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mean = np.mean(img_gray)
    gamma_val = math.log10(0.5) / math.log10(mean / 255)  # Formula calculation gamma
    image_gamma_correct = gamma_trans(frame, gamma_val)  # gamma Transformation

    rows, cols, _ = frame.shape
    rows2, cols2, _ = image_gamma_correct.shape

    x_medium = int(cols / 2)
    y_medium = int(rows / 2)

    x_medium2 = int(cols2 / 2)
    y_medium2 = int(rows2 / 2)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_frame2 = cv2.cvtColor(image_gamma_correct, cv2.COLOR_BGR2HSV)

    # red color
    low_red = np.array([150, 155, 84])
    high_red = np.array([185, 255, 255])

    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red_mask2 = cv2.inRange(hsv_frame2, low_red, high_red)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda a: cv2.contourArea(a), reverse=True)

    contours2, _ = cv2.findContours(red_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours2 = sorted(contours2, key=lambda b: cv2.contourArea(b), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        break

    for cnt in contours2:
        (x2, y2, w2, h2) = cv2.boundingRect(cnt)

        x_medium2 = int((x2 + x2 + w2) / 2)
        y_medium2 = int((y2 + y2 + h2) / 2)

        cv2.rectangle(image_gamma_correct, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
        break

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 0), 2)

    cv2.line(image_gamma_correct, (x_medium2, 0), (x_medium2, 480), (0, 255, 0), 2)
    cv2.line(image_gamma_correct, (0, y_medium2), (640, y_medium2), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Gama_Corrected_Frame", image_gamma_correct)
    cv2.imshow("red mask 2", red_mask2)

    if ret is True:
        videoKayit.write(frame)
        videoKayit2.write(image_gamma_correct)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
cap.release()
videoKayit.release()
videoKayit2.release()
cv2.destroyAllWindows()
