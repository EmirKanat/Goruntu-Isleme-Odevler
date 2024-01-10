import numpy as np
import cv2
import matplotlib.pyplot as plt
# Gri seviye görüntüyü yükleme
I = cv2.imread('gri_seviye_resim.png', cv2.IMREAD_GRAYSCALE)
# Histogramı hesaplamak için Hist matrisini oluştur
Hist = np.zeros(256, dtype=int)
# Görüntünün boyutlarını al
h, w = I.shape
# Histogram h
for v in range(h):
    for u in range(w):
        i = I[v, u]
        Hist[i] = Hist[i] + 1
print("Histogram:")
for i in range(256):
    print(f"{i}: {Hist[i]}")
# Histogramı grafiğini çizmek için
plt.bar(range(256), Hist)
plt.title('Histogram')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')
plt.show()
