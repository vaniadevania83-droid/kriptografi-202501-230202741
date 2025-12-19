# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [secret sharing (shamir's secret sharing)]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Caesar Cipher merupakan salah satu teknik enkripsi paling sederhana dan paling awal yang dikenal dalam kriptografi. Algoritma ini termasuk dalam jenis Cipher Substitusi, di mana setiap huruf pada teks terang (plaintext) digantikan oleh huruf lain yang memiliki selisih posisi tertentu dalam alfabet. Pergeseran ini bersifat statis dan dikenal sebagai "kunci" (k).
Di mana x adalah nilai numerik dari karakter (A=0, B=1, ..., Z=25) dan k adalah nilai pergeseran. Karena hanya memiliki 25 kemungkinan kunci fungsional, algoritma ini sangat rentan terhadap serangan brute-force.
---

## 3. Alat dan Bahan
1. Python 3.10+
2. Visual Studio Code sebagai IDE
3. Git dan GitHub untuk version control

---

## 4. Langkah Percobaan
1.  Membuka terminal dan melakukan navigasi ke folder proyek: praktikum/week2-cryptosystem/.
2. Membuat file baru bernama caesar_cipher.py di dalam subfolder src/.
3. Menuliskan logika fungsi encrypt dan decrypt sesuai dengan rumus modular aritmetika.
4. Menambahkan fungsi main untuk menerima input pengguna berupa pesan dan jumlah pergeseran.
5. Menjalankan program melalui terminal dengan perintah python src/caesar_cipher.py.
6. Melakukan commit hasil pekerjaan ke repositori lokal dan melakukan push ke GitHub.
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Menyesuaikan shift untuk dekripsi
    if mode == 'decrypt':
        shift = -shift
    
    for i in range(len(text)):
        char = text[i]
        
        # Enkripsi/Dekripsi karakter huruf besar
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Enkripsi/Dekripsi karakter huruf kecil
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Karakter non-alfabet tidak diubah
            result += char
            
    return result

# Contoh Penggunaan
if __name__ == "__main__":
    message = input("Masukkan pesan: ")
    key = int(input("Masukkan kunci (angka): "))
    
    encrypted = caesar_cipher(message, key, 'encrypt')
    decrypted = caesar_cipher(encrypted, key, 'decrypt')
    
    print(f"\nPlaintext  : {message}")
    print(f"Ciphertext : {encrypted}")
    print(f"Decrypted  : {decrypted}")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week11-secret-sharing/srenshoot/hasil-secret%20sharing.png)

)

---

## 7. Jawaban Pertanyaan
1. Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?
Keuntungan utamanya terletak pada kombinasi antara keamanan tinggi dan fleksibilitas. Jika kita hanya membagikan salinan kunci langsung, satu orang yang kehilangan kunci atau berkhianat sudah cukup untuk membocorkan rahasia tersebut. Sebaliknya, pada SSS:
•	Tidak ada kebocoran informasi: Pemegang saham (share) tunggal tidak mendapatkan informasi apa pun mengenai rahasia aslinya kecuali jika jumlah saham mencapai ambang batas (threshold).
•	Ketahanan terhadap kehilangan: Jika beberapa pemegang saham kehilangan datanya, rahasia tetap bisa dipulihkan selama jumlah pemegang saham lainnya masih memenuhi ambang batas.
•	Minimalisir Titik Kegagalan (Single Point of Failure): Rahasia tidak disimpan di satu tempat, melainkan terdistribusi.
2. Apa peran threshold (k) dalam keamanan secret sharing?
Ambang batas atau threshold (k) menentukan jumlah minimum partisipan atau bagian kunci yang diperlukan untuk merekonstruksi rahasia asli.
•	Dalam SSS, ini direpresentasikan sebagai derajat polinomial (k-1). Misalnya, untuk threshold 3, kita membutuhkan polinomial derajat 2 (parabola).
•	Keamanan: Jika jumlah bagian yang terkumpul kurang dari k (misal hanya k-1), maka secara matematis rahasia asli tetap tidak mungkin ditemukan karena terdapat tak terhingga banyaknya polinomial yang bisa melewati titik-titik tersebut. Jadi, k berfungsi sebagai sistem pengaman "multi-persetujuan".
3. Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.
Skenario yang paling nyata adalah pada Penyimpanan Kunci Utama (Master Key) Dompet Kripto atau Root Key Otoritas Sertifikat (CA).
•	Contoh: Sebuah perusahaan memiliki kunci enkripsi cadangan untuk seluruh data nasabahnya. Jika kunci ini disimpan oleh CEO saja, itu berisiko (jika CEO menghilang atau kunci dicuri). Dengan SSS, kunci tersebut dipecah menjadi 5 bagian: diberikan kepada CEO, CTO, CFO, Komisaris, dan Pengacara Perusahaan, dengan threshold k=3.
•	Manfaatnya: Kunci hanya bisa digunakan jika minimal 3 dari 5 petinggi tersebut setuju untuk hadir dan menggabungkan kunci mereka. Ini mencegah penyalahgunaan wewenang secara sepihak sekaligus melindungi dari risiko kehilangan kunci secara individual.

---

## 8. Kesimpulan
Praktikum ini membuktikan bahwa Caesar Cipher bekerja dengan prinsip substitusi sederhana berbasis pergeseran posisi alfabet menggunakan operasi modulo 26. Melalui implementasi Python, terlihat bahwa algoritma ini sangat bergantung pada kerahasiaan kunci, namun sangat tidak aman untuk melindungi data sensitif karena jumlah kombinasi kunci yang sangat terbatas (hanya 25 kemungkinan) sehingga mudah ditembus dengan metode brute-force. Selain itu, karena karakter non-alfabet tidak dienkripsi, struktur pesan tetap terlihat, yang menunjukkan bahwa algoritma klasik ini hanya cocok digunakan untuk tujuan edukasi dasar mengenai logika enkripsi.

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
Date:   2025-12-19

    week11-cryptosystem: secret sharing (shamir's secret sharing) )
```
