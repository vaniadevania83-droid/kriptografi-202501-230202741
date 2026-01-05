# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: [Analisis Serangan Kriptografi]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB] 

---

## 1. Tujuan
(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.
---

## 2. Capaian Kegiatan
- Laporan studi kasus analisis serangan sistem nyata.
- Rekomendasi solusi/algoritma pengganti.
- Commit Git dengan format week14-analisis-serangan.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Python 3.11  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (hashlib dan time) )

---

## 4. Persiapan Lingkungan
(Serangan kriptografi pada sistem nyata sering terjadi akibat penggunaan algoritma lemah dan implementasi keamanan yang tidak tepat. Salah satu contoh yang umum adalah serangan brute force pada password lemah, di mana penyerang dengan mudah menebak password sederhana, terutama jika disimpan menggunakan hash lama seperti MD5 tanpa salt. Selain itu, serangan Man-in-the-Middle (MITM) pada komunikasi TLS dapat terjadi akibat konfigurasi sertifikat yang tidak valid atau pengguna yang mengabaikan peringatan keamanan, sehingga data sensitif dapat disadap. Serangan replay pada protokol autentikasi juga sering terjadi pada sistem yang tidak menggunakan nonce atau timestamp, memungkinkan penyerang mengirim ulang pesan autentikasi yang sah untuk memperoleh akses ilegal. Kasus-kasus tersebut menunjukkan pentingnya penggunaan algoritma kriptografi yang kuat, implementasi yang benar, dan kebijakan keamanan yang baik.)

---

## 5. Panduan Langkah demi Langkah
(

```Langkah 1 – Identifikasi Serangan
1 Studi Kasus Serangan
Kasus yang dianalisis dalam praktikum ini adalah serangan brute force dan dictionary attack terhadap password yang disimpan menggunakan hash MD5. MD5 merupakan algoritma hash lama yang sudah tidak direkomendasikan karena memiliki kelemahan kriptografis dan kecepatan komputasi yang tinggi, sehingga memudahkan penyerang melakukan percobaan hash secara masif.
2 Vektor Serangan
•	Database password bocor atau dapat diakses penyerang
•	Password di-hash menggunakan algoritma lemah (MD5)
•	Tidak adanya mekanisme salt pada hash
•	Password pengguna terlalu sederhana
3 Dampak Serangan
•	Password pengguna berhasil dipecahkan
•	Akses ilegal ke akun sistem
•	Potensi pencurian data dan penyalahgunaan akun
Langkah 2 – Evaluasi Kelemahan
1 Analisis Kelemahan Algoritma
MD5 memiliki beberapa kelemahan utama:
•	Rentan terhadap collision attack
•	Proses hashing sangat cepat sehingga cocok untuk brute force
•	Tidak dirancang untuk penyimpanan password
2 Sumber Kelemahan
Kelemahan pada kasus ini berasal dari:
•	Algoritma kriptografi: penggunaan MD5 yang sudah usang
•	Implementasi: tidak menggunakan salt
•	Kebijakan sistem: tidak membatasi percobaan login
Dengan demikian, kerentanan bukan hanya berasal dari algoritma, tetapi juga dari implementasi dan konfigurasi sistem yang tidak aman.
Langkah 3 – Rekomendasi Solusi
1 Algoritma dan Mekanisme Pengganti
Untuk meningkatkan keamanan sistem, rekomendasi yang dapat diterapkan adalah:
•	Mengganti MD5 dengan SHA-256 atau SHA-3 untuk hashing data umum
•	Menggunakan bcrypt, scrypt, atau Argon2 untuk penyimpanan password
•	Menerapkan salt unik pada setiap password
•	Membatasi percobaan login (rate limiting)
2 Alasan Pemilihan Solusi
•	Algoritma modern lebih tahan terhadap brute force
•	Password hashing modern bersifat lambat (computationally expensive)
•	Salt mencegah penggunaan rainbow table
•	Rate limiting mengurangi efektivitas serangan otomatis
3 Dampak terhadap Keamanan
Penerapan solusi tersebut dapat secara signifikan meningkatkan ketahanan sistem terhadap serangan kriptografi serta melindungi data pengguna dari kebocoran lebih lanjut.



```
)

---



---

## 6. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
1. Mengapa sistem lama masih rentan terhadap brute force atau dictionary attack?

Karena masih menggunakan algoritma kriptografi usang, kebijakan keamanan yang lemah, serta kurangnya pembaruan sistem dan audit keamanan berkala.

2. Perbedaan kelemahan algoritma dan kelemahan implementasi

Kelemahan algoritma berasal dari desain matematis algoritma itu sendiri, sedangkan kelemahan implementasi muncul akibat kesalahan penerapan, konfigurasi, atau manajemen kunci yang buruk.

3. Cara memastikan sistem tetap aman di masa depan

Organisasi harus melakukan pembaruan algoritma secara berkala, menerapkan standar keamanan terbaru, melakukan audit keamanan rutin, serta meningkatkan kesadaran keamanan bagi pengguna dan administrator sistem.
)
---

## 7. Kesimpulan
(Berdasarkan hasil analisis, dapat disimpulkan bahwa serangan kriptografi sering terjadi akibat penggunaan algoritma lemah dan implementasi yang tidak aman. Kasus serangan brute force pada hash MD5 menunjukkan pentingnya pemilihan algoritma kriptografi yang tepat dan penerapan mekanisme keamanan tambahan. Dengan mengganti algoritma lama dan memperbaiki konfigurasi sistem, tingkat keamanan informasi dapat ditingkatkan secara signifikan.  )

---

## 8. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 9. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2026-01-04

    week14-cryptosystem: Analisis Serangan Kriptografi )
```
