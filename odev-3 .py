import cv2
import numpy as np
image = cv2.imread('pirinc_resmi.jpg')  # Resmi uygun bir şekilde değiştirin
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Gaussian bulanıklığı uygula
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
# kenar tespiti uygula
edges = cv2.Canny(blurred, 30, 150)
# Toplulukları bul
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Belirli bir alan eşiğini tanımla
min_area = 100
# Pirinçleri saymak için bir sayaç
rice_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_area:
        rice_count += 1
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
# Sonucu ekrana yazdır
print(f"Pirinç Sayısı: {rice_count}")
# Görüntüyü göster
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
