# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---

## 2. capaian kegiatan
A. Tokopedia (www.tokopedia.com)
- Issuer CA: DigiCert Inc (atau GlobalSign).
- Masa Berlaku: [Contoh: 12 April 2025 s/d 12 April 2026]
- Algoritma Enkripsi: TLS 1.3, X25519, dan AES_128_GCM.
- Analisis: Menggunakan protokol TLS terbaru (1.3) yang lebih cepat dan aman dibandingkan versi 1.2 karena proses handshake yang lebih singkat.

B. Shopee (shopee.co.id)
- Issuer CA: Amazon / DigiCert.
- Masa Berlaku: [Contoh: 1 Januari 2025 s/d 1 Januari 2026]
- Algoritma Enkripsi: TLS 1.2/1.3, RSA 2048 bits.
- Analisis: Penggunaan RSA 2048 bits memberikan standar keamanan yang kuat untuk pertukaran kunci (key exchange).
---

## 3. Alat dan Bahan
(- Python 3.x  
- Laporan Studi Kasus: Dokumen tertulis mengenai penerapan riil SSL/TLS pada layanan email (seperti PGP/S-MIME) dan platform e-commerce.
- Analisis Isu Privasi & Etika: Penjelasan kritis mengenai dilema penggunaan kriptografi, seperti hak privasi individu vs kepentingan audit perusahaan/negara.
- Bukti Observasi Sertifikat: Dokumentasi (screenshot) dan rincian teknis sertifikat digital (Issuer, algoritma, masa berlaku) dari minimal 2 situs e-commerce.
- Repositori Terstruktur: Folder praktikum yang rapi dengan riwayat perubahan (commit) pada Git menggunakan format pesan: week12-aplikasi-tls. )

---

## 4. Langkah Percobaan
Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Pindah ke folder praktikum: cd praktikum/week12-aplikasi-tls/
2. Simpan screenshot: (Pastikan file sertifikat_tokopedia.png dan sertifikat_shopee.png sudah ada di folder screenshots/)
3. Tambahkan file ke git: git add .
4. Commit: git commit -m "week12-aplikasi-tls"
5. Push (Opsional): git push origin main

---

## 5. Panduan Langkah demi Langkah
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:
1. Analisis SSL/TLS pada Web E-commerce
Saya melakukan observasi pada dua platform e-commerce besar untuk menganalisis sertifikat digital mereka.
A. Tokopedia (www.tokopedia.com)
•	Issuer CA: DigiCert Inc (atau GlobalSign).
•	Masa Berlaku: [Contoh: 12 April 2025 s/d 12 April 2026]
•	Algoritma Enkripsi: TLS 1.3, X25519, dan AES_128_GCM.
•	Analisis: Menggunakan protokol TLS terbaru (1.3) yang lebih cepat dan aman dibandingkan versi 1.2 karena proses handshake yang lebih singkat.
B. Shopee (shopee.co.id)
•	Issuer CA: Amazon / DigiCert.
•	Masa Berlaku: [Contoh: 1 Januari 2025 s/d 1 Januari 2026]
•	Algoritma Enkripsi: TLS 1.2/1.3, RSA 2048 bits.
•	Analisis: Penggunaan RSA 2048 bits memberikan standar keamanan yang kuat untuk pertukaran kunci (key exchange).
2. Studi Kasus E-commerce & Ancaman
Enkripsi pada e-commerce bekerja dengan mengamankan jalur komunikasi antara browser pengguna dan server e-commerce.
•	Penerapan: Saat login atau memasukkan data kartu kredit, data tersebut dienkripsi di sisi klien menggunakan kunci publik server sebelum dikirim melalui internet.
•	Ancaman Tanpa TLS (Man-in-the-Middle): Tanpa TLS, penyerang yang berada di jaringan yang sama (misal: WiFi publik) dapat melakukan sniffing untuk melihat data plain-text. Penyerang bisa mencuri session cookie atau kredensial pembayaran secara langsung.
3. Analisis Etika & Privasi
Isu Privasi pada Email (PGP/S-MIME)
Penggunaan PGP (Pretty Good Privacy) memastikan hanya penerima yang memiliki kunci privat yang bisa membaca pesan. Isu muncul pada Metadata: meskipun isi pesan aman, informasi siapa yang mengirim ke siapa dan kapan tetap bisa terlihat oleh penyedia layanan (ISP).
Dilema Etika
1.	Dekripsi Perusahaan: Secara etika, perusahaan memiliki hak untuk mengaudit komunikasi di perangkat/aset kantor demi keamanan data perusahaan (mencegah kebocoran data). Namun, hal ini harus transparan dan tertuang dalam kontrak kerja agar tidak melanggar privasi personal karyawan.
2.	Pengawasan Pemerintah: Pemerintah seringkali meminta "backdoor" pada aplikasi terenkripsi (seperti WhatsApp) untuk alasan keamanan nasional. Dilemanya: backdoor untuk polisi juga bisa menjadi celah bagi hacker jahat, sehingga melemahkan keamanan semua orang.


```

```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:


![Hasil Input](/praktikum/week12-aplikasi-tls/screnshot/gambar-shopee.png)
![Hasil Output](/praktikum/week12-aplikasi-tls/screnshot/gambar-tokopedia.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara HTTP dan HTTPS? HTTP mengirimkan data secara plain-text (tidak terenkripsi), sedangkan HTTPS adalah HTTP yang berjalan di atas protokol TLS/SSL, sehingga semua data yang dikirimkan dienkripsi dan integritasnya terjamin.

2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS? Sertifikat digital berfungsi sebagai "identitas resmi" yang diverifikasi oleh pihak ketiga (CA). Tanpa sertifikat, kita mungkin terhubung ke server yang terenkripsi tetapi milik penyerang (imitasi), bukan server asli yang dituju.

3. Bagaimana kriptografi mendukung privasi tetapi menimbulkan tantangan hukum? Kriptografi memberikan privasi mutlak lewat End-to-End Encryption (E2EE). Namun, tantangan hukum muncul ketika pelaku kriminal menggunakan teknologi yang sama untuk menyembunyikan rencana kejahatan, sehingga aparat penegak hukum kesulitan melakukan penyidikan meskipun memiliki surat perintah.
---

## 8. Kesimpulan
Kesimpulan Implementasi SSL/TLS pada platform e-commerce merupakan standar keamanan krusial yang menjamin kerahasiaan, integritas, dan autentikasi data pengguna guna mencegah serangan Man-in-the-Middle. Meskipun kriptografi sangat efektif dalam melindungi privasi digital secara personal, penggunaannya menciptakan tantangan etika dan hukum yang kompleks, terutama terkait keseimbangan antara hak privasi individu dengan kebutuhan pengawasan keamanan serta audit profesional di lingkungan kerja.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 3ed366fd40ca43486bfaffdedc5b1b9bd66c9842
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2026-01-04

    week12-cryptosystem: Aplikasi TLS & E-commerce )
```
