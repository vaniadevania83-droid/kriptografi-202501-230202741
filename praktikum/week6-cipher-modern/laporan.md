# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: [cipher-modern]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
1. Python
2. Visual Studio Code
3. Git dan akun GitHub

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
def run_aes_implementation():
    """Menjalankan implementasi enkripsi dan dekripsi AES-128 (MODE_EAX)."""
    try:
        # 1. Pembangkitan Kunci (128 bit = 16 byte)
        key = get_random_bytes(16)
        
        # Data yang akan dienkripsi
        plaintext = b"Modern Cipher AES Example 128 bit" 

        # 2. Enkripsi (MODE_EAX menghasilkan ciphertext dan authentication tag)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        
        print("--- AES-128 (Advanced Encryption Standard) ---")
        print(f"Kunci (16 byte): {key.hex()}")
        print(f"Plaintext: {plaintext.decode()}")
        print(f"Nonce (IV): {cipher.nonce.hex()}")
        print(f"Ciphertext: {ciphertext.hex()}")
        print(f"Tag: {tag.hex()}")

        # 3. Dekripsi (memerlukan kunci, mode, dan nonce yang sama dari proses enkripsi)
        cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
        decrypted = cipher_dec.decrypt(ciphertext)
        
        # Verifikasi tag (penting untuk EAX)
        try:
            cipher_dec.verify(tag)
            print(f"Decrypted: {decrypted.decode()}")
        except ValueError:
            print("Verifikasi Tag Gagal: Data mungkin telah dirusak atau kunci salah.")
        
        print("-" * 43)

    except Exception as e:
        print(f"Terjadi Error pada AES: {e}")

if __name__ == "__main__":
    run_aes_implementation()


def run_des_simulation():
    """Menjalankan simulasi enkripsi dan dekripsi DES (MODE_ECB)."""
    try:
        # 1. Pembangkitan Kunci (64 bit = 8 byte)
        key = get_random_bytes(8)
        
        # Data yang akan dienkripsi (harus kelipatan 8 byte untuk ECB)
        plaintext = b"ABCDEFGH" 

        # 2. Enkripsi
        cipher = DES.new(key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        
        print("--- DES (Data Encryption Standard) ---")
        print(f"Kunci (8 byte): {key.hex()}")
        print(f"Plaintext: {plaintext.decode()}")
        print(f"Ciphertext: {ciphertext.hex()}")

        # 3. Dekripsi
        # Kunci dan mode harus sama.
        decipher = DES.new(key, DES.MODE_ECB)
        decrypted = decipher.decrypt(ciphertext)
        
        print(f"Decrypted: {decrypted.decode()}")
        print("-" * 37)

    except Exception as e:
        print(f"Terjadi Error pada DES: {e}")

if __name__ == "__main__":
    run_des_simulation()


def run_rsa_implementation():
    """Menjalankan implementasi pembangkitan kunci, enkripsi, dan dekripsi RSA."""
    try:
        # 1. Pembangkitan Pasangan Kunci (2048 bit)
        print("--- RSA (Rivest–Shamir–Adleman) ---")
        print("Membangkitkan pasangan kunci 2048 bit...")
        key = RSA.generate(2048)
        private_key = key
        public_key = key.publickey()
        print("Pembangkitan Kunci Selesai.")

        # Data yang akan dienkripsi (harus lebih pendek dari ukuran kunci dikurangi padding)
        plaintext = b"RSA Asymmetric Cipher Example"
        
        # 2. Enkripsi dengan Public Key
        cipher_rsa = PKCS1_OAEP.new(public_key)
        ciphertext = cipher_rsa.encrypt(plaintext)
        
        print(f"\nPlaintext: {plaintext.decode()}")
        print(f"Panjang Ciphertext: {len(ciphertext)} bytes")
        print(f"Ciphertext (sample 64 byte): {ciphertext[:64].hex()}...")

        # 3. Dekripsi dengan Private Key
        decipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted = decipher_rsa.decrypt(ciphertext)
        
        print(f"\nDecrypted: {decrypted.decode()}")
        print("-" * 38)

    except Exception as e:
        print(f"Terjadi Error pada RSA: {e}")

if __name__ == "__main__":
    run_rsa_implementation()
```
)

---

## 6. Hasil dan Pembahasan
(Implementasi ketiga algoritma (DES, AES, dan RSA) berhasil menghasilkan ciphertext yang unik dan kemudian mendekripsinya kembali menjadi plaintext asli, yang mengonfirmasi bahwa proses kriptografi berjalan dengan benar.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week6-cipher-modern/srenshot/hasil-aes.png)
![Hasil Input](/praktikum/week6-cipher-modern/srenshot/hasil-des.png)
![Hasil Output](/praktikum/week6-cipher-modern/srenshot/hasil-sra.png)
)

---

## 7. Jawaban Pertanyaan
1.	Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?
 DES (Data Encryption Standard) dan AES (Advanced Encryption Standard) adalah algoritma simetris (symmetric ciphers), yang berarti mereka menggunakan satu kunci rahasia yang sama untuk proses enkripsi dan dekripsi. DES menggunakan kunci efektif 56-bit, yang dianggap rentan terhadap serangan brute-force dalam komputasi modern, sehingga menjadikannya usang. Sebagai penggantinya, AES menggunakan panjang kunci yang jauh lebih besar (128, 192, atau 256 bit), menawarkan keamanan yang kuat dan menjadikannya standar enkripsi global saat ini.
RSA adalah algoritma asimetris (asymmetric cipher atau public-key cryptography) yang beroperasi menggunakan sepasang kunci yang berbeda: Kunci Publik untuk enkripsi dan Kunci Privat untuk dekripsi. Keamanannya bergantung pada kesulitan faktorisasi bilangan prima besar dan menggunakan panjang kunci yang jauh lebih besar (umumnya 2048 bit atau lebih) dibandingkan dengan DES dan AES. Namun, karena kompleksitas matematisnya, RSA jauh lebih lambat daripada AES, sehingga umumnya digunakan untuk pertukaran kunci sesi (kunci simetris) atau tanda tangan digital, bukan untuk enkripsi data dalam jumlah besar.

2.	Mengapa AES lebih banyak digunakan dibanding DES di era modern?
AES (Advanced Encryption Standard) lebih banyak digunakan dibandingkan DES (Data Encryption Standard) di era modern karena alasan utama yang berkaitan dengan keamanan kriptografi dan efisiensi komputasi:
a.	Panjang Kunci yang Lebih Besar: Kunci DES hanya 56 bit (efektif), yang saat ini dianggap terlalu pendek. Dengan peningkatan daya komputasi modern, kunci 56-bit dapat dipecahkan menggunakan serangan brute-force dalam waktu yang relatif singkat (bahkan kurang dari 24 jam oleh mesin khusus). Sebaliknya, AES menggunakan kunci dengan panjang 128, 192, atau 256 bit, yang secara eksponensial lebih sulit untuk dipecahkan.
Contoh: Untuk AES-128, ada 2^{128} kemungkinan kunci, yang menjadikannya aman secara komputasi untuk masa mendatang.
b.	Struktur Algoritma yang Lebih Baik: AES didasarkan pada Rijndael cipher, yang merupakan Substitution-Permutation Network (SPN). Sementara DES menggunakan Feistel structure. Struktur AES (SPN) dianggap lebih efisien dan lebih resisten terhadap beberapa jenis serangan kriptanalisis dibandingkan DES.
c.	Kecepatan dan Efisiensi: Meskipun memiliki keamanan yang jauh lebih tinggi, AES dirancang agar sangat cepat dalam implementasi perangkat lunak maupun perangkat keras. Dalam banyak kasus, AES-128 berjalan lebih cepat daripada DES.
d.	Standar Pemerintah: AES telah diadopsi oleh NIST (National Institute of Standards and Technology) Amerika Serikat sebagai standar enkripsi federal sejak tahun 2001, menggantikan DES, dan direkomendasikan untuk melindungi informasi rahasia oleh pemerintah di seluruh dunia.
3.	Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
RSA disebut Asimetris karena ia menggunakan dua kunci berbeda (sepasang) untuk melakukan enkripsi dan dekripsi. Kunci ini adalah Kunci Publik (untuk mengenkripsi, dapat disebar) dan Kunci Privat (untuk mendekripsi, harus dirahasiakan).
Proses Pembangkitan Kunci:
Proses kuncinya bergantung pada matematika bilangan prima besar:
1.	Pilih Dua Bilangan Prima Besar (p dan q).
2.	Hitung Modulus (n): n = p \times q.
3.	Pilih Kunci Publik (e): Bilangan yang koprima dengan hasil perkalian (p-1)(q-1).
4.	Hitung Kunci Privat (d): Dihitung sebagai invers modular dari e.
Kunci Publik adalah pasangan (n, e), dan Kunci Privat adalah pasangan (n, d). Keamanannya didasarkan pada kesulitan untuk memfaktorkan kembali n menjadi p dan q.

---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan dan membandingkan tiga algoritma kriptografi modern. Mahasiswa dapat memahami perbedaan fundamental antara algoritma simetris (DES dan AES) yang cepat dan menggunakan satu kunci, dengan algoritma asimetris (RSA) yang menggunakan pasangan kunci dan cocok untuk pertukaran kunci/tanda tangan digital. AES-128 terbukti menjadi standar yang kuat dan efisien untuk enkripsi data massal saat ini.
---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-11-09

    week6-cryptosystem: cipher-modern )
```
