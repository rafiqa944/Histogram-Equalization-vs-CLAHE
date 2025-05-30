import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio as psnr

img = cv2.imread('church.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lab_eq = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB)
l_eq, a_eq, b_eq = cv2.split(lab_eq)
l_eq = cv2.equalizeHist(l_eq)
lab_eq_img = cv2.merge((l_eq, a_eq, b_eq))
img_eq = cv2.cvtColor(lab_eq_img, cv2.COLOR_LAB2RGB)

lab_clahe = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB)
l_clahe, a_clahe, b_clahe = cv2.split(lab_clahe)

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(13, 13))
cl = clahe.apply(l_clahe)

lab_clahe_img = cv2.merge((cl, a_clahe, b_clahe))
img_clahe = cv2.cvtColor(lab_clahe_img, cv2.COLOR_LAB2RGB)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.title('Gambar Asli')
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('Histogram Equalization')
plt.imshow(img_eq)
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('CLAHE')
plt.imshow(img_clahe)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Histogram Asli')
plt.hist(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY).ravel(),bins=256, range=[0, 256], color='blue')
plt.xlabel('Intensitas')
plt.ylabel('Frekuensi')

plt.subplot(2, 3, 5)
plt.title('Histogram Equalization')
plt.hist(l_eq.ravel(), bins=256, range=[0, 256], color='blue')
plt.xlabel('Intensitas')

plt.subplot(2, 3, 6)
plt.title('Histogram CLAHE')
plt.hist(cl.ravel(), bins=256, range=[0, 256], color='blue')
plt.xlabel('Intensitas')

plt.tight_layout()
plt.show()


def psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))


psnr_he = psnr(img_rgb, img_eq)
psnr_clahe = psnr(img_rgb, img_clahe)

print(f"PSNR Histogram Equalization: {psnr_he:.2f} dB")
print(f"PSNR CLAHE: {psnr_clahe:.2f} dB")
