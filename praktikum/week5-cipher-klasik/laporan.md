# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1.	Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2.	Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3.	Mengimplementasikan algoritma transposisi sederhana.
4.	Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Kriptografi klasik adalah metode enkripsi historis yang beroperasi pada karakter atau blok karakter kecil, digunakan sebelum era komputasi modern. Cipher klasik utama dibagi menjadi dua jenis: Cipher Substitusi dan Cipher Transposisi. Cipher Substitusi bekerja dengan mengganti setiap unit plaintext (biasanya satu huruf) dengan unit ciphertext yang berbeda. Caesar Cipher adalah bentuk paling sederhana dari substitusi, di mana setiap huruf digeser sejumlah posisi tetap (kunci) di seluruh pesan (monoalfabetik).  Vigenère Cipher adalah pengembangan polialfabetik yang menggunakan kunci berupa frasa, di mana pergeseran (shift) bervariasi untuk setiap huruf plaintext, membuatnya lebih aman dari analisis frekuensi sederhana. Sebaliknya, Cipher Transposisi tidak mengubah karakter, melainkan mengubah urutan atau posisi huruf dalam plaintext. Intinya, metode ini melakukan permutasi pada huruf-huruf plaintext untuk menyembunyikan struktur pesan, seperti pada contoh Transposisi Kolom.
---

## 3. Alat dan Bahan
1. Python
2. Visual Studio Code
3. Git dan akun GitHub

---

## 4. Langkah Percobaan

1.	Inisialisasi Lingkungan: Membuat struktur folder praktikum/ week5-cipher-klasik/ dan subfolder src/ serta file laporan.md.
2.	Implementasi Caesar Cipher (src/caesar.py): Mengimplementasikan fungsi caesar_encrypt dan caesar_decrypt yang ringkas, menggunakan logika pergeseran modulo 26 dan operator walrus untuk efisiensi.
3.	Implementasi Vigenère Cipher (src/vigenere.py): Mengimplementasikan fungsi enkripsi dan dekripsi yang menggunakan kunci berupa string, dengan mengulang kunci jika panjangnya lebih pendek dari pesan.
4.	Implementasi Transposisi Sederhana (src/transpose.py): Mengimplementasikan Transposisi Kolom (Rail Fence sederhana) untuk mengubah posisi karakter.
5.	Pengujian: Melakukan uji coba pada setiap program dengan plaintext dan kunci yang berbeda, kemudian memverifikasi hasil dekripsi.
6.	Penyusunan Laporan: Merangkum teori, hasil, dan menjawab pertanyaan diskusi dalam file ini.


---

## 5. Source Code


```python
import math
def caesar_encrypt(plaintext, key):
    """Mengenkripsi teks menggunakan Caesar Cipher."""
    return "".join(
        chr(
            (ord(char) - (base := (ord('A') if char.isupper() else ord('a'))) + key)
            % 26 + base
        )
        if char.isalpha() else char
        for char in plaintext
    )

def caesar_decrypt(ciphertext, key):
    """Mendekripsi teks menggunakan Caesar Cipher."""
    # Dekripsi adalah enkripsi dengan kunci negatif
    return caesar_encrypt(ciphertext, -key)

def vigenere_encrypt(plaintext, key):
    """Mengenkripsi teks menggunakan Vigenere Cipher."""
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Tentukan shift berdasarkan huruf kunci yang berulang
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            
            # Hitung pergeseran dan terapkan modulo 26
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    """Mendekripsi teks menggunakan Vigenere Cipher."""
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            # Tentukan shift berdasarkan huruf kunci yang berulang
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            
            # Hitung pergeseran ke belakang dan terapkan modulo 26
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def transpose_encrypt(plaintext, key=5):
    """Mengenkripsi teks menggunakan Transposisi Kolom."""
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    """Mendekripsi teks menggunakan Transposisi Kolom."""
    # Hitung dimensi matriks (kolom dan baris)
    num_of_cols = math.ceil(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        
        if (col == num_of_cols) or \
           (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
            
    return ''.join(plaintext)

if __name__ == "__main__":
    
    print("--- DEMO CIPHER KLASIK ---")
    
    # 1. Caesar Cipher
    msg_caesar = "INI ADALAH PESAN RAHASIA"
    key_caesar = 3
    enc_caesar = caesar_encrypt(msg_caesar, key_caesar)
    dec_caesar = caesar_decrypt(enc_caesar, key_caesar)
    print("\n[CAESAR CIPHER]")
    print(f"Plaintext : {msg_caesar}")
    print(f"Kunci     : {key_caesar}")
    print(f"Ciphertext: {enc_caesar}")
    print(f"Decrypted : {dec_caesar}")

    # 2. Vigenère Cipher
    msg_vigenere = "WIKIPEDIAENKRIPSI"
    key_vigenere = "KUNCI"
    enc_vigenere = vigenere_encrypt(msg_vigenere, key_vigenere)
    dec_vigenere = vigenere_decrypt(enc_vigenere, key_vigenere)
    print("\n[VIGENERE CIPHER]")
    print(f"Plaintext : {msg_vigenere}")
    print(f"Kunci     : {key_vigenere}")
    print(f"Ciphertext: {enc_vigenere}")
    print(f"Decrypted : {dec_vigenere}")

    # 3. Transposisi Sederhana
    msg_transpose = "TEKNOLOGIINFORMASI"
    key_transpose = 5
    enc_transpose = transpose_encrypt(msg_transpose, key_transpose)
    dec_transpose = transpose_decrypt(enc_transpose, key_transpose)
    print("\n[TRANSPOSISI SEDERHANA]")
    print(f"Plaintext : {msg_transpose}")
    print(f"Kunci     : {key_transpose}")
    print(f"Ciphertext: {enc_transpose}")
    print(f"Decrypted : {dec_transpose}")


```


---

## 6. Hasil dan Pembahasan
 Secara keseluruhan, hasil uji coba menunjukkan bahwa implementasi Caesar Cipher berhasil melakukan pergeseran tetap dengan memastikan *wrap-around* menggunakan `(P + K) mod 26`; Vigenère Cipher berhasil menerapkan sifat polialfabetik, di mana pergeseran untuk setiap karakter *plaintext* ditentukan oleh karakter kunci yang sesuai; sementara Transposisi Kolom berhasil mengubah urutan karakter dengan menyusun pesan berdasarkan kolom kunci *k*.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi1](/praktikum/week5-cipher-klasik/Screenshot/hasil1.png)
![Hasil Eksekusi2](/praktikum/week5-cipher-klasik/Screenshot/hasil2.png)

---

## 7. Jawaban Pertanyaan
1. Kelemahan Utama Caesar Cipher dan Vigenère Cipher 
Caesar Cipher
Kelemahan utamanya adalah ruang kunci yang sangat kecil (hanya 25 kemungkinan pergeseran yang tidak trivial).
•	Karena hanya ada 25 kunci yang mungkin (pergeseran 1 hingga 25), cipherteks (teks terenkripsi) dapat dengan mudah diserang menggunakan serangan brute-force (mencoba semua kemungkinan kunci) dalam hitungan detik.
•	Setiap huruf dienkripsi menjadi huruf yang sama setiap kali muncul, yang membuatnya sangat rentan terhadap analisis frekuensi.
Vigenère Cipher
Meskipun jauh lebih kuat daripada Caesar Cipher, kelemahan utamanya adalah sifat pengulangan kata kunci (key).
•	Vigenère Cipher menggunakan skema substitusi polialfabetik (menggunakan beberapa cipher Caesar yang berbeda berdasarkan huruf pada kata kunci).
•	Kelemahannya adalah jika kata kunci diulang, periode pengulangan tersebut dapat ditemukan (misalnya, menggunakan Uji Kasiski atau Metode Friedman).
•	Setelah panjang kunci ditemukan, cipherteks dapat dipecah menjadi beberapa cipher Caesar terpisah, yang kemudian dapat dipecahkan satu per satu dengan analisis frekuensi.
2. Mengapa Cipher Klasik Mudah Diserang dengan Analisis Frekuensi? 
Cipher klasik, terutama yang substitusi monoalfabetik seperti Caesar Cipher, mudah diserang dengan analisis frekuensi karena mereka tidak mengubah distribusi frekuensi huruf dari bahasa asli (plaintext).
•	Substitusi Monoalfabetik: Setiap huruf dalam plaintext selalu dienkripsi menjadi huruf yang sama dalam cipherteks. Misalnya, dalam bahasa Indonesia, huruf 'A' adalah yang paling sering muncul. Dalam cipherteks Caesar, jika 'A' dienkripsi menjadi 'D', maka 'D' akan menjadi huruf yang paling sering muncul, mencerminkan frekuensi 'A'.
•	Analisis Frekuensi: Penyerang dapat menghitung frekuensi setiap huruf yang muncul dalam cipherteks. Mereka kemudian membandingkan frekuensi tersebut dengan frekuensi kemunculan huruf yang diketahui dalam bahasa yang digunakan (plaintext), seperti bahasa Indonesia, Inggris, dll.
•	Pemetaan: Huruf cipherteks dengan frekuensi tertinggi hampir pasti sesuai dengan huruf plaintext dengan frekuensi tertinggi (misalnya, 'E' atau 'A'). Dengan memetakan beberapa huruf yang paling sering dan paling jarang, penyerang dapat merekonstruksi kuncinya dengan cepat.
3. Perbandingan Kelebihan dan Kelemahan Cipher Substitusi vs Transposisi 
Perbandingan Cipher Substitusi vs. Transposisi 
Cipher Substitusi bekerja dengan mengganti setiap huruf plaintext (teks asli) dengan huruf atau simbol lain, sehingga tujuan utamanya adalah mengaburkan identitas karakter. Kelebihan utama dari cipher jenis ini adalah kemudahan implementasi manual. Namun, kelemahan fatalnya, terutama pada jenis monoalfabetik seperti Caesar Cipher, adalah kerentanan tinggi terhadap analisis frekuensi, karena distribusi frekuensi huruf aslinya tetap tercermin pada cipherteks.
Sebaliknya, Cipher Transposisi beroperasi dengan cara mengubah atau mengacak urutan huruf-huruf plaintext, tanpa mengubah huruf itu sendiri, sehingga tujuannya adalah mengaburkan posisi karakter. Kelebihan utamanya adalah bahwa cipher ini tidak mengubah distribusi frekuensi huruf dalam bahasa aslinya, yang membuat serangan analisis frekuensi yang efektif pada cipher substitusi menjadi kurang berguna. Akan tetapi, kelemahan cipher transposisi adalah kerentanannya terhadap serangan yang berfokus pada pola kata dan anagram, serta dapat dipecahkan dengan mencari panjang kunci yang tepat untuk mengembalikan urutan kolom atau barisnya.

---

## 8. Kesimpulan

Praktikum ini berhasil mengimplementasikan tiga algoritma kriptografi klasik (Caesar Cipher sebagai substitusi monoalfabetik, Vigenère Cipher sebagai substitusi polialfabetik, dan Transposisi Sederhana yang mengubah posisi) dengan mencapai tujuan pembelajaran melalui demonstrasi fungsi enkripsi dan dekripsi yang akurat, namun kami menyimpulkan bahwa semua cipher klasik, meskipun algoritma polialfabetik dan transposisi lebih kuat, memiliki kelemahan mendasar berupa ketergantungan pada Analisis Frekuensi dan ruang kunci yang kecil, sehingga menjadikannya tidak aman untuk komunikasi modern.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 7e32317359e93be09425c50758b56a8bdf9bc04e
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-09-20

    week5-cryptosystem: Cipher Klasik (Caesar, Vigenère, Transposisi) )
```
