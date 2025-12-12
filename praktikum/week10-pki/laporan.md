# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [PKI]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  
 

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
PKI adalah kerangka kerja yang terdiri dari kebijakan, prosedur, hardware, software, dan orang yang diperlukan untuk mengelola sertifikat digital, yang memungkinkan autentikasi dan enkripsi komunikasi. Komponen utama PKI adalah Certificate Authority (CA). CA bertindak sebagai pihak ketiga tepercaya (Trusted Third Party) yang memverifikasi identitas pemilik sertifikat (Subject) dan menerbitkan sertifikat digital yang ditandatangani menggunakan Private Key milik CA. Sertifikat ini mengikat identitas Subject dengan Public Key-nya. PKI sangat penting dalam protokol keamanan web modern seperti Transport Layer Security (TLS) atau HTTPS, di mana sertifikat digunakan untuk memastikan bahwa pengguna benar-benar berkomunikasi dengan server yang diklaim (autentikasi server), sehingga mencegah serangan Man-in-the-Middle (MITM).

---

## 3. Alat dan Bahan
1. Python 3.11 atau lebih baru.
2. Visual Studio Code / editor lain.
3. Git dan akun GitHub.
4. Library tambahan: cryptography dan pyopenssl.
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat folder struktur praktikum, termasuk praktikum/week10-pki/src/.
2. Menginstal library yang dibutuhkan: pip install cryptography pyopenssl.
3. Membuat file src/pki_cert.py dan menyalin kode program yang disediakan.
4. Menjalankan program dengan perintah python src/pki_cert.py.
5. Memastikan dua file output berhasil dibuat di direktori: private.key dan cert.pem.
6. Mengambil screenshot hasil eksekusi program.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week10-pki/screnshoot/hasil-pki.png)

)

---

## 7. Jawaban Pertanyaan
1. Apa fungsi utama Certificate Authority (CA)?
Fungsi utama Certificate Authority (CA) adalah sebagai pihak ketiga tepercaya (Trusted Third Party) yang menjamin autentisitas identitas pemegang sertifikat (subjek) kepada pihak lain (klien/pengguna). CA bertugas untuk:
•	Memverifikasi identitas pemohon.
•	Menerbitkan dan menandatangani sertifikat digital menggunakan Private Key CA.
•	Mengelola pencabutan sertifikat yang sudah tidak berlaku atau terkompromi (melalui CRL/OCSP).
2. Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Self-signed certificate tidak cukup untuk sistem produksi (terutama yang menghadap publik) karena tidak memiliki rantai kepercayaan (Chain of Trust) yang terverifikasi secara global. Klien (browser) tidak akan menemukan Issuer (yang merupakan dirinya sendiri) di dalam Trust Store bawaan sistem. Akibatnya, browser akan menampilkan peringatan keamanan serius, membuat pengguna tidak dapat mempercayai koneksi, meskipun secara teknis koneksi tersebut terenkripsi.
3. Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah serangan Man-in-the-Middle (MITM) dengan menyediakan mekanisme autentikasi server yang kuat sebelum pertukaran kunci enkripsi:
1.	Verifikasi Sertifikat: Klien menerima sertifikat server dan memverifikasi tanda tangannya menggunakan Public Key dari CA yang tepercaya yang sudah tersimpan di sistem.
2.	Validitas Identitas: Jika verifikasi tanda tangan berhasil, klien yakin bahwa Public Key di dalam sertifikat benar-benar milik server yang diklaim (misalnya, bank.com), dan bukan penyerang.
3.	Kunci yang Aman: Setelah identitas terautentikasi, handshake TLS dilanjutkan, di mana kunci sesi (simetris) dinegosiasikan dan dienkripsi menggunakan Public Key yang sudah diverifikasi, memastikan kunci sesi hanya diketahui oleh klien dan server asli, bukan oleh MITM.

---

## 8. Kesimpulan
Praktikum ini berhasil menunjukkan proses pembuatan sertifikat digital self-signed menggunakan Python dan library cryptography. Dari analisis, dapat disimpulkan bahwa Public Key Infrastructure (PKI), dengan Certificate Authority (CA) sebagai intinya, adalah fondasi penting untuk keamanan komunikasi internet (HTTPS/TLS) karena menyediakan mekanisme autentikasi dan integritas yang mencegah serangan penipuan identitas seperti MITM.

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
commit e0fbd7e400a0a2eec10f809a169ae5ca78a9d816
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-12-13

    week10-pki: implementasi self-signed certificate dan laporan )
```
