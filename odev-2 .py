import cv2
import numpy as np
# Kamerayı başlat
cap = cv2.VideoCapture(0)
while True:
    # Görüntüyü yakala
    ret, frame = cap.read()
    # RGB'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Kırmızı renk aralığını belirle
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    # HSV görüntüsünü belirtilen aralıkta maskeleyin
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Orijinal görüntü ve maske arasındaki bitwise AND işlemi
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # Sonuçları göster
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
cap.release()
cv2.destroyAllWindows()
