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
Shamir's Secret Sharing (SSS) adalah algoritma kriptografi yang memungkinkan sebuah rahasia dipecah menjadi n bagian (shares), di mana rahasia tersebut hanya dapat direkonstruksi jika minimal ada k bagian yang dikumpulkan (k \le n). Algoritma ini didasarkan pada konsep matematika Interpolasi Polinomial Lagrange.Dalam skema (k, n), sebuah polinomial derajat k-1 dibuat dengan rahasia asli sebagai konstanta a_0. Titik-titik pada kurva polinomial tersebut kemudian dibagikan kepada para partisipan. Secara matematis, mustahil untuk menentukan polinomial tersebut (dan menemukan a_0) jika titik yang dimiliki kurang dari k.
---

## 3. Alat dan Bahan
1. Python 3.10+
2. Visual Studio Code sebagai IDE
3. Git dan GitHub untuk version control

---

## 4. Langkah Percobaan
1. Membuat struktur folder praktikum/week11-secret-sharing/src/.
2. Menginstal library yang dibutuhkan menggunakan perintah pip install secretsharing.
3. Membuat file secret_sharing.py dan mengimplementasikan fungsi untuk membagi rahasia menjadi 5 bagian dengan threshold 3.
4. Menjalankan skrip untuk memverifikasi bahwa rahasia dapat pulih dengan 3 shares, namun gagal jika kurang dari itu.
5. Mendokumentasikan hasil eksekusi dalam bentuk screenshot.
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import random
from typing import List, Tuple

# Fungsi untuk menghitung Modular Inverse (penting untuk pembagian dalam modulo)
def inverse(a, p):
    return pow(a, p - 2, p)

# 1. Implementasi Pembagian Rahasia (Split)
def split_secret(secret: int, k: int, n: int, p: int) -> List[Tuple[int, int]]:
    """
    secret: rahasia dalam angka
    k: threshold (minimal share)
    n: total shares yang dibuat
    p: bilangan prima (harus lebih besar dari secret dan n)
    """
    if k > n:
        raise ValueError("Threshold tidak boleh lebih besar dari total n")
    
    # Membuat koefisien polinomial secara acak: f(x) = secret + a1*x + a2*x^2 + ...
    # a0 adalah secret itu sendiri
    coefficients = [secret] + [random.randint(0, p - 1) for _ in range(k - 1)]
    
    def f(x):
        result = 0
        for i, coeff in enumerate(coefficients):
            result = (result + coeff * pow(x, i, p)) % p
        return result
    
    # Membuat n buah koordinat (x, f(x)) sebagai shares
    return [(i, f(i)) for i in range(1, n + 1)]

# 2. Implementasi Rekonstruksi Rahasia (Recover menggunakan Lagrange Interpolation)
def recover_secret(shares: List[Tuple[int, int]], p: int) -> int:
    """
    shares: daftar koordinat (x, y)
    p: bilangan prima yang sama saat split
    """
    secret = 0
    k = len(shares)
    
    for i in range(k):
        xi, yi = shares[i]
        num = 1
        den = 1
        for j in range(k):
            if i == j:
                continue
            xj, yj = shares[j]
            # Rumus Lagrange L_i(0) = PROD( -xj / (xi - xj) )
            num = (num * -xj) % p
            den = (den * (xi - xj)) % p
        
        # S_i = yi * L_i(0)
        term = (yi * num * inverse(den, p)) % p
        secret = (secret + term) % p
        
    return (secret + p) % p

# --- Main Program ---
if __name__ == "__main__":
    # Parameter: Bilangan prima besar (Mersenne Prime 2^13 - 1 sebagai contoh sederhana)
    P = 2**31 - 1 
    SECRET = 20251117  # Rahasia berupa angka (Contoh: NIM atau PIN)
    K = 3 # Minimal 3 orang
    N = 5 # Dibagi ke 5 orang

    print(f"Rahasia Asli: {SECRET}")
    
    # Langkah 1: Splitting
    shares = split_secret(SECRET, K, N, P)
    print("\nShares yang dihasilkan:")
    for s in shares:
        print(f"Partisipan {s[0]}: {s[1]}")

    # Langkah 2: Rekonstruksi (Gunakan 3 shares acak)
    subset_shares = shares[:3] 
    recovered = recover_secret(subset_shares, P)
    
    print("\n--- Hasil Uji ---")
    print(f"Menggunakan {len(subset_shares)} shares.")
    print(f"Rahasia yang dipulihkan: {recovered}")
    
    if recovered == SECRET:
        print("Status: BERHASIL (Rahasia Cocok)")
    else:
        print("Status: GAGAL")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week11-secret-sharing/srenshoot/hasil-scret-sharing.png)

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
Praktikum ini menunjukkan bahwa Shamir’s Secret Sharing adalah metode distribusi rahasia yang sangat efektif karena memanfaatkan sifat polinomial untuk menciptakan ambang batas keamanan. Dengan SSS, fleksibilitas operasional meningkat tanpa harus mengorbankan kerahasiaan data aslinya.

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
commit 4ac6b0ff53bd8cccc4390caabea0799f29cbe3b7
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-12-19

    week11-cryptosystem: secret sharing (shamir's secret sharing) )
```
