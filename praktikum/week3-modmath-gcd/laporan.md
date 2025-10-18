# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: [Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
---

## 2. Dasar Teori
Greatest Common Divisor (GCD) dari dua bilangan adalah bilangan bulat positif terbesar yang dapat membagi habis kedua bilangan tersebut. Algoritma Euclidean adalah metode yang sangat efisien untuk menghitung GCD. Dalam kriptografi, GCD digunakan untuk menentukan apakah dua bilangan koprima (GCD=1), yang merupakan syarat penting untuk mencari invers modular.

---

## 3. Alat dan Bahan
1. Python
2. Visual Studio Code
3. Git dan akun GitHub
---

## 4. Langkah Percobaan
1. Membuat struktur folder praktikum/week3-modmath-gcd/src/ dan file modular_math.py.
2. Mengimplementasikan fungsi Aritmetika Modular (mod_add, mod_sub, mod_mul, mod_exp).
3. Mengimplementasikan Algoritma Euclidean untuk GCD (gcd).
4. Mengimplementasikan Extended Euclidean Algorithm (egcd) dan fungsi invers modular (modinv).
5. Mengimplementasikan simulasi Logaritma Diskrit sederhana (discrete_log).
6. Menjalankan program (python src/modular_math.py) untuk menguji semua fungsi yang diimplementasikan.
7. Merekam hasil eksekusi dalam folder screenshots/.

---

## 5. Source Code


```python
# contoh potongan kode
# --- Aritmetika Modular ---
def A(a,b,n):return (a+b)%n               # Penjumlahan
def B(a,b,n):return ((a-b)%n+n)%n        # Pengurangan (aman)
def C(a,b,n):return (a*b)%n               # Perkalian
def D(b,e,n):return pow(b,e,n)            # Eksponensiasi

# --- GCD & Extended Euclidean ---
def G(a,b): # GCD rekursif
    if b==0:return a
    return G(b,a%b)

def E(a,b): # EGCD iteratif
    x0,x1,y0,y1=1,0,0,1
    while b!=0:
        q=a//b
        a,b=b,a%b
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1
    return a,x0,y0

def I(a,n): # Invers Modular
    g,x,_=E(a,n)
    if g!=1:return None
    return ((x%n)+n)%n

# --- Logaritma Diskrit ---
def L(a,b,n):
    for x in range(n):
        if D(a,x,n)==b:return x
    return None

# PENGUJIAN SATU BARIS (Output Bersatu)

# Aritmetika Modular
print(f"7 + 5 mod 12 = {A(7, 5, 12)}")
print(f"5 - 7 mod 12 = {B(5, 7, 12)}")
print(f"7 * 5 mod 12 = {C(7, 5, 12)}")
print(f"7^128 mod 13 = {D(7, 128, 13)}")

# GCD
print(f"gcd(270, 192) = {G(270, 192)}")

# Invers Modular
print(f"Invers 10 mod 17 = {I(10, 17)}")

# Logaritma Diskrit
print(f"3^x ≡ 4 (mod 7), x = {L(3, 4, 7)}")

print("\n=== EKSEKUSI SELESAI ===")

```

---

## 6. Hasil dan Pembahasan


Hasil eksekusi program modmath-gcd:

![Hasil Eksekusi](/praktikum/week3-modmath-gcd/Screnshoot/hasil_eksekusi.png)

---

## 7. Jawaban Pertanyaan
Pertanyaan 1: Apa peran aritmetika modular dalam kriptografi modern?
Aritmetika modular adalah dasar matematis yang:
•	Menciptakan Keterbatasan: Membatasi data enkripsi dalam rentang terkelola ($0$ hingga $n-1$).
•	Membangun Keamanan: Memungkinkan Eksponensiasi Modular ($a^x \pmod n$), yang berfungsi sebagai fungsi satu arah (one-way function) yang sulit dibalik.

Pertanyaan 2: Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
Invers modular ($d$) sangat penting karena memungkinkan Dekripsi.
•	Hubungan Kunci: Kunci privat $d$ adalah invers modular dari kunci publik $e$ terhadap modulus $\phi(n)$, di mana $e \cdot d \equiv 1 \pmod{\phi(n)}$.
•	Fungsi: Invers modular (ditemukan dengan Algoritma Euclidean Diperluas) menjamin reversibilitas unik, artinya pesan yang dienkripsi dengan $e$ pasti dapat didekripsi kembali dengan $d$.

Pertanyaan 3: Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
Tantangan utamanya adalah kompleksitas komputasi eksponensial.
•	Masalah Sulit: Logaritma Diskrit (mencari $x$ dari $a^x \equiv b \pmod n$) tidak memiliki algoritma efisien yang diketahui di komputer klasik.
•	Serangan Brute Force Mustahil: Untuk modulus 2048-bit, mencoba semua kemungkinan nilai $x$ adalah mustahil dalam jangka waktu yang realistis (secara komputasi).
•	Jaminan Keamanan: Kesulitan ini adalah pilar keamanan untuk skema kunci publik modern (seperti Diffie-Hellman dan ECC).


---

## 8. Kesimpulan
Kegiatan praktikum ini telah sukses menerapkan operasi fundamental dari teori bilangan yang menjadi pilar utama kriptografi, termasuk aritmetika modular, Algoritma Euclidean, Algoritma Euclidean Diperluas, dan simulasi Logaritma Diskrit. Keberhasilan skema kunci publik sangat bergantung pada peran penting GCD dan invers modular untuk menjamin kemampuan pembalikan proses (dekripsi), di sisi lain, kerumitan Logaritma Diskrit berfungsi sebagai penjamin keamanan sistem dari upaya serangan brute force ketika modulus yang digunakan berukuran besar.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 9d5ef67b8c99f9ed99ee3209901ba24d67af241c
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-10-18

    week3--modmath-gcd)
```
