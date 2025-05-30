# Peningkatan Kontras dengan Histogram Equalization dan CLAHE

Proyek ini menunjukkan teknik peningkatan gambar menggunakan **Histogram Equalization** dan **CLAHE (Contrast Limited Adaptive Histogram Equalization)** dalam Python dengan OpenCV. Selain itu, kode ini menghitung **PSNR (Peak Signal-to-Noise Ratio)** untuk mengevaluasi kualitas gambar yang ditingkatkan.

## 📁 File
- `church.jpg` — Gambar sumber yang digunakan untuk peningkatan.
- `image_contrast.py` — Skrip Python utama untuk melakukan peningkatan dan analisis.

## 📷 Teknik yang Diimplementasikan

### 1. Histogram Equalization
Meningkatkan kontras dengan menyebarluaskan nilai intensitas yang paling sering muncul.

### 2. CLAHE (Contrast Limited Adaptive Histogram Equalization)
Meningkatkan kontras lokal, terutama berguna di area dengan pencahayaan yang bervariasi.

### 3. PSNR (Peak Signal-to-Noise Ratio)
Metrik yang digunakan untuk membandingkan kesamaan antara gambar asli dan yang ditingkatkan.

## 📊 Output
Skrip akan menampilkan:
- Gambar asli, gambar yang telah disetarakan histogram, dan gambar CLAHE.
- Histogram dari setiap versi.
- Nilai PSNR untuk kedua teknik peningkatan.
