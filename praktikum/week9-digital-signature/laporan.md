# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [digital-signature]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori
(Tanda Tangan Digital (Digital Signature) merupakan mekanisme kriptografi penting yang berfungsi untuk menjamin otentikasi dan integritas data dalam komunikasi elektronik, seringkali diimplementasikan menggunakan algoritma asimetris seperti RSA (Rivest-Shamir-Adleman) atau DSA (Digital Signature Algorithm). Proses penandatanganan melibatkan pengirim yang pertama-tama menghitung nilai hash (misalnya, menggunakan SHA-256) dari pesan yang akan dikirim, lalu mengenkripsi nilai hash tersebut menggunakan kunci privat miliknya—hasil enkripsi inilah yang disebut sebagai tanda tangan digital. Ketika penerima menerima pesan beserta tanda tangan digital, penerima akan menghitung ulang hash dari pesan yang diterima, dan kemudian mendekripsi tanda tangan digital menggunakan kunci publik pengirim yang bersangkutan; jika kedua nilai hash (yang dihitung ulang dan yang didekripsi) sama persis, maka penerima yakin bahwa pesan tersebut tidak dimodifikasi (integritas) dan berasal dari pemilik kunci privat yang sah (otentikasi).  )

---

## 3. Alat dan Bahan
1. Python
2. Visual Studio Code
3. Git dan akun GitHub

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `digital_signature.py` di folder `praktikum/week9-digital_siganture/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python digital_signature.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# src/signature.py

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# --- Inisialisasi dan Pembuatan Kunci ---
print("1. Pembuatan Kunci & Tanda Tangan")
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Kunci untuk ditampilkan (opsional, untuk demonstrasi)
print("Private Key (excerpt):", private_key.export_key('PEM').decode().split('\n')[1] + '...')
print("Public Key (excerpt):", public_key.export_key('PEM').decode().split('\n')[1] + '...')

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
print("Pesan Asli:", message.decode())

# Hitung hash pesan
h = SHA256.new(message)

# Buat tanda tangan dengan private key (Penandatanganan)
# 
signer = pkcs1_15.new(private_key)
signature = signer.sign(h)
print("Signature:", signature.hex())

# --- Verifikasi Tanda Tangan Pesan Asli (Kasus Berhasil) ---
print("2. Verifikasi Tanda Tangan (Pesan Asli)")
try:
    # Verifikasi dengan public key
    verifier_original = pkcs1_15.new(public_key)
    verifier_original.verify(h, signature)
    print("Verifikasi BERHASIL: Tanda tangan valid untuk pesan asli.")
except (ValueError, TypeError):
    print("Verifikasi GAGAL: Tanda tangan tidak valid.")

# --- Uji Modifikasi Pesan (Kasus Gagal) ---
print(" 3. Uji Modifikasi Pesan (Verifikasi Gagal)")
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
print("Pesan Modifikasi:", fake_message.decode())

# Hitung hash pesan palsu
h_fake = SHA256.new(fake_message)

try:
    # Verifikasi signature lama dengan hash pesan palsu
    verifier_fake = pkcs1_15.new(public_key)
    verifier_fake.verify(h_fake, signature)
    print("Verifikasi BERHASIL (seharusnya GAGAL).") # Ini akan terjadi hanya jika ada bug, harusnya gagal
except (ValueError, TypeError) as e:
    # Pesan yang berbeda akan menghasilkan hash yang berbeda, sehingga verifikasi akan gagal
    print(f"Verifikasi GAGAL: Tanda tangan tidak cocok dengan pesan yang diubah.")
    print(f"   Detail: {e}") ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week9-digital-signature/Srenshoot/hasil-digital-signature.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Perbedaan Utama Enkripsi vs Tanda Tangan RSA: Enkripsi RSA bertujuan menjaga kerahasiaan pesan dengan menggunakan Kunci Publik Penerima untuk mengunci data, sedangkan Tanda Tangan Digital RSA bertujuan menjamin otentikasi dan integritas dengan menggunakan Kunci Privat Pengirim untuk menandatangani hash pesan.  
- Pertanyaan 2: Jaminan Integritas dan Otentikasi: Integritas terjamin karena perubahan satu karakter pun pada pesan akan mengubah nilai hash sehingga verifikasi gagal. Otentikasi terjamin karena tanda tangan yang valid secara matematis hanya bisa dibuat oleh pemilik sah Kunci Privat yang unik dan rahasia.
- Pertanyaan 3: Peran Certificate Authority (CA): CA bertindak sebagai pihak ketiga tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital, menjamin bahwa kunci publik yang digunakan untuk memverifikasi tanda tangan benar-benar milik entitas yang diklaim (mencegah penipuan identitas).  
)
---

## 8. Kesimpulan
(Berdasarkan praktikum implementasi tanda tangan digital menggunakan algoritma RSA, dapat disimpulkan bahwa mekanisme ini efektif dalam menjamin otentikasi dan integritas data. Percobaan membuktikan bahwa tanda tangan yang dibuat dengan kunci privat pengirim hanya dapat diverifikasi valid menggunakan kunci publik yang sesuai, dan setiap upaya modifikasi pada pesan asli akan menghasilkan nilai hash yang berbeda, menyebabkan kegagalan verifikasi. Hal ini menunjukkan bahwa tanda tangan digital tidak hanya memvalidasi identitas pengirim, tetapi juga melindungi data dari perubahan yang tidak sah selama transmisi.  )

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
Date:   2025-12-11

    week9-cryptosystem: digital-signature )
```
