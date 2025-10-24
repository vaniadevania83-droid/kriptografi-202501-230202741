# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.


---

## 2. Dasar Teori
Kekuatan kriptosistem diukur menggunakan tiga konsep utama. Pertama, Entropi Kunci ($H(K)$), yang diperkenalkan Claude Shannon, mengukur ketidakpastian atau keacakan ruang kunci (keyspace) dengan rumus $H(K) = \log_2(N)$, di mana $N$ adalah jumlah kunci. Entropi yang lebih tinggi berarti kunci lebih kuat. Kedua, Unicity Distance ($U$) adalah panjang ciphertext minimum yang diperlukan untuk menentukan kunci yang benar secara unik. Jika ciphertext lebih pendek dari $U$, banyak kunci mungkin tampak valid. Ketiga, Serangan Brute Force adalah metode serangan mendasar yang mencoba setiap kunci dalam keyspace ($N$). Keberhasilannya bergantung pada entropi kunci; kriptosistem modern seperti AES-128 memiliki entropi sangat tinggi ($128$ bit atau $2^{128}$ kunci) sehingga serangan ini tidak praktis (computationally infeasible).
---

## 3. Alat dan Bahan
1. Python
2. Visual Studio Code
3. Git dan akun GitHub

---

## 4. Langkah Percobaan
1.	 Mempersiapkan lingkungan pengembangan dengan memastikan Python telah terinstal.
2.	 Membuka Visual Studio Code dan membuat direktori kerja baru untuk praktikum minggu ke-4, misalnya praktikum/week4-entropy-unicity/.
3.	 Di dalam direktori tersebut, membuat sebuah file Python baru dengan nama analysis.py (atau nama serupa).
4.	 Menulis kode program ke dalam file analysis.py: a. Mengimpor library math untuk operasi logaritma. b. Mendefinisikan fungsi calculate_entropy(keyspace_size) untuk menghitung $H(K)$ menggunakan math.log2(). c. Mendefinisikan fungsi calculate_unicity_distance(HK, R, A) untuk menghitung $U$. Dalam percobaan ini, nilai Redundansi (R) diasumsikan $0.95$ dan Alfabet (A) adalah $26$. d. Mendefinisikan fungsi analyze_brute_force_time(keyspace_size, attempts_per_second) untuk mengestimasi waktu serangan dalam hari.
5.	 Menambahkan bagian eksekusi utama di akhir file untuk memanggil fungsi-fungsi di atas. Dilakukan dua skenario: a. Skenario 1: Kunci 16-bit (Ruang Kunci = $2^{16}$). b. Skenario 2: Kunci 64-bit (Ruang Kunci = $2^{64}$).
6.	 Menjalankan program dari terminal Visual Studio Code dengan perintah python analysis.py.
7.	 Mengamati dan mencatat hasil keluaran (output) yang ditampilkan pada terminal.



---

## 5. Source Code


```python
import math

def calculate_entropy(keyspace_size):
    return math.log2(keyspace_size)

def calculate_unicity_distance(HK, R=0.95, A=26):
    return HK / (R * math.log2(A))

def analyze_brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

# --- EKSEKUSI ---
# Kunci yang diuji
KEYS_16 = 2**16
KEYS_64 = 2**64

print("===Analisis Kekuatan Kunci===")
print(f"Entropi Ruang Kunci 2^16:{calculate_entropy(KEYS_16):.3f}bit") 
print(f"Entropi Ruang Kunci 2^64:{calculate_entropy(KEYS_64):.3f}bit") 

# Menghitung Unicity Distance langsung dengan fungsi di dalam print
print(f"Jarak Unicity Kunci 16-bit:{calculate_unicity_distance(calculate_entropy(KEYS_16)):.3f}") 

print(f"Estimasi Waktu  Brute Force(10^6attempts/sec):")
print(f"Kunci 16-bit:{analyze_brute_force_time(KEYS_16):.6f}hari") 
print(f"Kunci 64-bit:{analyze_brute_force_time(KEYS_64):.2f}hari") 
print("===EKSEKUSISELESAI===")


```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program sesuai:
1.	Analisis Entropi: Program mengkonfirmasi bahwa entropi kunci ekuivalen dengan panjang bit kunci tersebut. Kunci 16-bit memiliki entropi 16.000 bit, dan kunci 64-bit memiliki entropi 64.000 bit. Ini menunjukkan bahwa entropi adalah ukuran langsung dari 'kompleksitas' ruang kunci.
2.	Analisis Unicity Distance: Untuk kunci 16-bit (dengan asumsi redundansi R=0.95 dan alfabet 26), didapatkan unicity distance $\approx 3.583$. Ini berarti secara teoritis, seorang analis hanya memerlukan sekitar 4 karakter ciphertext untuk dapat menentukan kunci 16-bit yang benar secara unik.
3.	Analisis Brute Force: Perbedaan waktu brute force sangat drastis dan menunjukkan skala eksponensial dari keamanan kunci.
o	Kunci 16-bit: Waktu yang dibutuhkan adalah 0.000001 hari. Jika dikonversi ke detik ($0.0000007585 \times 86400 \approx 0.065$ detik), serangan ini dapat dilakukan secara instan.
o	Kunci 64-bit: Waktu yang dibutuhkan adalah $\approx 213.5$ juta hari. Ini menunjukkan bahwa meskipun kunci 64-bit (seperti pada standar DES) sudah tidak aman lagi bagi organisasi besar, kunci ini masih sangat kuat terhadap serangan brute force oleh individu dengan $1$ juta percobaan per detik. Perbandingan ini menyoroti mengapa standar modern seperti AES beralih ke kunci 128-bit atau 256-bit, yang waktu brute force-nya triliunan kali lebih lama.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week4-entropy-unicity/Screnshoot/hasil.png)



---

## 7. Jawaban Pertanyaan
1. Apa arti dari nilai entropy dalam konteks kekuatan kunci?
Entropi ($H(K)$) dalam konteks kekuatan kunci adalah ukuran matematis yang menyatakan tingkat ketidakpastian (randomness) dan keragaman dari ruang kunci (keyspace).
•	Poin Utama: Nilai entropi menunjukkan jumlah bit informasi biner yang diperlukan untuk merepresentasikan kunci tersebut.
•	Korelasi dengan Kekuatan: Semakin tinggi nilai entropi (semakin besar bit), semakin kuat kuncinya. Kunci 128-bit memiliki entropi 128 bit, artinya seorang penyerang harus mencoba hingga $2^{128}$ kemungkinan kunci secara brute force untuk memecahkannya.

2. Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
Unicity Distance ($U$) adalah metrik yang menentukan panjang minimum ciphertext (pesan tersandi) yang diperlukan agar ciphertext tersebut hanya dapat didekripsi dengan satu kunci yang benar yang menghasilkan plaintext yang bermakna.
•	Poin Utama: Jika ciphertext yang dianalisis lebih pendek dari $U$, mungkin ada banyak kunci salah yang menghasilkan plaintext yang terlihat masuk akal, membuat kriptanalis kesulitan.
•	Korelasi dengan Keamanan: Jika panjang ciphertext jauh lebih besar dari $U$, maka setiap kunci yang salah kemungkinan besar akan menghasilkan plaintext yang acak (tidak bermakna), sehingga kunci yang benar menjadi unik dan mudah diidentifikasi. Cipher yang baik harus memiliki unicity distance yang sangat besar.

3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
Brute force adalah ancaman karena meskipun algoritma kriptografi (seperti AES) secara matematis kuat, serangan ini berfokus pada panjang kunci (entropy).
•	Ancaman Waktu: Brute force mengancam jika:
1.	Entropi Kunci Terlalu Kecil: Seperti pada Caesar Cipher (entropi $\approx 4.7$ bit), yang dapat dipecahkan dalam hitungan detik.
2.	Kemajuan Komputasi: Meskipun AES-128 saat ini aman, kemajuan teknologi (termasuk komputasi kuantum di masa depan) dapat secara drastis mengurangi waktu yang dibutuhkan untuk mencoba setiap kunci.
•	Ancaman Implementasi yang Lemah: Meskipun algoritma kuat, brute force juga dapat berhasil jika pengguna memilih kunci yang lemah (misalnya, kunci 128-bit yang memiliki hanya 40 bit entropi efektif), sehingga penyerang tidak perlu mencoba seluruh ruang kunci $2^{128}$, melainkan hanya ruang kunci yang lemah ($2^{40}$).

---

## 8. Kesimpulan
Percobaan ini menunjukkan bahwa entropi kunci adalah ekuivalen dengan panjang bitnya ($H(K) = k$ untuk kunci $k$-bit). Peningkatan panjang kunci dari 16-bit ke 64-bit meningkatkan entropi secara linear, namun meningkatkan waktu serangan brute force secara eksponensial. Kunci 16-bit dapat dipecahkan secara instan ($\approx 0.065$ detik), sedangkan kunci 64-bit memerlukan estimasi $\approx 213.5$ juta hari dengan daya komputasi yang sama, membuktikan pentingnya panjang kunci yang memadai untuk keamanan kriptografis.
---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit b5fa2a20c7eaf7adf03b688d8d40e12acba47667
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-10-25

    week4-cryptosystem: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force) )
```
