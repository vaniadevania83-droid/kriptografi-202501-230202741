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

## 2. Dasar Teori
Kriptografi merupakan teknik pengamanan informasi yang berfungsi melindungi data dari akses tidak sah dengan menjaga kerahasiaan, integritas, dan autentikasi komunikasi digital. Dalam jaringan komputer, kriptografi banyak diterapkan melalui protokol Secure Sockets Layer (SSL) dan Transport Layer Security (TLS) yang berperan membangun saluran komunikasi aman antara klien dan server agar data tidak dapat disadap atau dimodifikasi oleh pihak ketiga.

TLS bekerja melalui proses handshake yang melibatkan pertukaran sertifikat digital untuk memverifikasi identitas server melalui Certificate Authority (CA) serta pembentukan kunci sesi untuk enkripsi data. Implementasi TLS pada layanan web dikenal sebagai HTTPS dan sangat penting pada sistem e-commerce untuk melindungi data login dan transaksi pembayaran. Selain itu, kriptografi juga digunakan pada sistem email melalui enkripsi end-to-end seperti PGP dan S/MIME untuk menjaga privasi pesan, meskipun penerapannya menimbulkan tantangan etika dan hukum terkait pengawasan dan perlindungan privasi.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (hashlib dan time)  )

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

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week12-aplikasi-tls/screnshot/gambar-lazada.png)
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
commit abc12345
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2026-01-04

    week12-cryptosystem: Aplikasi TLS & E-commerce )
```
