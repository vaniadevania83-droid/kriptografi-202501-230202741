# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: [Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)]  
Nama: [Deviana Ainul Riqoh] 
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2. Menggambarkan proses enkripsi dan dekripsi sederhana.
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).
---

## 2. Dasar Teori
Sebuah kriptosistem adalah kerangka kerja yang terdiri dari lima elemen kunci untuk mengamankan komunikasi: pesan asli (plaintext), pesan tersandi (ciphertext), algoritma enkripsi dan dekripsi (metode matematis untuk transformasi), serta kunci (parameter rahasia yang mengendalikan proses). Dalam sistem modern, algoritma biasanya bersifat publik, dan keamanan sistem sepenuhnya bergantung pada kerahasiaan kunci yang digunakan. Secara umum, kriptosistem terbagi menjadi dua kelompok utama: kriptografi simetris, yang menggunakan satu kunci yang sama untuk menyandikan dan membuka sandi; dan kriptografi asimetris (kunci publik), yang menggunakan sepasang kunci berbeda satu kunci publik untuk mengenkripsi dan satu kunci privat untuk mendekripsi.

---

## 3. Alat dan Bahan
- Python 3.11  
- Visual Studio Code   
- Git dan akun GitHub  
- Draw.io 

---

## 4. Langkah Percobaan
1.	Membuat diagram/skema alur kerja kriptosistem dasar yang menggambarkan proses enkripsi dan dekripsi, lalu menyimpannya sebagai screenshots/diagram_kriptosistem.png.
2.	Membuat file Python bernama simple_crypto.py di dalam folder praktikum/week2-cryptosystem/src/.
3.	Menyalin dan menulis kode program dari modul praktikum untuk mengimplementasikan Caesar Cipher sederhana.
4.	Menjalankan program dari terminal dengan perintah python src/simple_crypto.py.
5.	Mengambil screenshot hasil eksekusi program dan menyimpannya sebagai screenshots/hasil_eksekusi.png.
6.	Menyusun laporan laporan.md yang berisi semua komponen, dari tujuan hingga jawaban diskusi.
7.	Melakukan commit dan push ke repositori GitHub dengan pesan week2-cryptosystem.

---

## 5. Source Code


```python
def shift_cipher(text: str, shift: int = 3) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif '0' <= ch <= '9':
            result.append(chr((ord(ch) - ord('0') + shift) % 10 + ord('0')))
        else:
            result.append(ch)
    return ''.join(result)

def main():
    print("=== SHIFT CIPHER SEDERHANA ===")
    plaintext = input("Masukkan plaintext: ")
    ciphertext = shift_cipher(plaintext, 3)
    print("\nHasil Enkripsi (shift = 3):", ciphertext)
    print("Hasil Dekripsi :", plaintext)
     
if __name__ == "__main__":
    main()
 ...
```


---

## 6. Hasil dan Pembahasan
Diagram menunjukkan proses enkripsi dan dekripsi menggunakan algoritma Shift Cipher dengan kunci simetris. Pesan asli (plaintext) “Deviana Ainul Riqoh (230202741)” dienkripsi menggunakan key = 3, menghasilkan ciphertext yang kemudian dapat dikembalikan ke bentuk semula melalui proses dekripsi dengan kunci yang sama.Dari hasil eksekusi program di Visual Studio Code, input deviana menghasilkan ciphertext ghlyldqd dan berhasil didekripsi kembali menjadi deviana. Hal ini membuktikan bahwa algoritma Shift Cipher bekerja dengan benar. Proses enkripsi dilakukan dengan menggeser setiap huruf sebanyak tiga posisi dalam alfabet.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week2-cryptosystem/screensshot/diagram_kriptosistem.jpg)
![Hasil Input](/praktikum/week2-cryptosystem/screensshot/hasil_eksekusi.png)



---

## 7. Jawaban Pertanyaan
1.	Sebutkan komponen utama dalam sebuah kriptosistem. Komponen utamanya ada lima:
•	Plaintext: Pesan asli yang dapat dibaca.
•	Ciphertext: Pesan tersandi hasil enkripsi.
•	Algoritma Enkripsi: Aturan untuk mengubah plaintext menjadi ciphertext.
•	Algoritma Dekripsi: Aturan untuk mengubah ciphertext kembali menjadi plaintext.
•	Kunci: Parameter yang digunakan oleh algoritma untuk proses enkripsi dan dekripsi.
2.	Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris? Sistem Simetris:
•	Kelebihan: Proses enkripsi/dekripsi sangat cepat dan efisien secara komputasi. Cocok untuk mengenkripsi data dalam jumlah besar.
•	Kelemahan: Masalah distribusi kunci. Kunci rahasia harus dibagikan antara pengirim dan penerima melalui saluran yang aman terlebih dahulu. Sistem Asimetris:
•	Kelebihan: Memecahkan masalah distribusi kunci. Kunci publik dapat dibagikan secara bebas tanpa memerlukan saluran aman.
•	Kelemahan: Prosesnya jauh lebih lambat dan membutuhkan sumber daya komputasi yang lebih besar dibandingkan sistem simetris.
3.	Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris? Karena kunci yang sama digunakan untuk enkripsi dan dekripsi, maka kunci tersebut harus dirahasiakan dan hanya diketahui oleh pihak-pihak yang berkomunikasi. Masalahnya adalah bagaimana cara mengirimkan kunci rahasia ini kepada penerima secara aman? Jika kunci dikirim melalui saluran yang tidak aman, pihak ketiga dapat menyadap kunci tersebut dan membahayakan seluruh komunikasi selanjutnya. Ini menciptakan dilema "ayam dan telur": untuk berkomunikasi secara aman, kita butuh kunci aman, tetapi untuk mengirim kunci aman, kita butuh saluran komunikasi yang aman.
 
---

## 8. Kesimpulan
Shift Cipher merupakan algoritma kriptografi klasik yang menggunakan metode substitusi sederhana.
Proses enkripsi dilakukan dengan menggeser setiap karakter sejauh nilai kunci tertentu.
Meskipun sederhana dan tidak aman untuk digunakan secara praktis, algoritma ini sangat efektif untuk memahami konsep dasar enkripsi, dekripsi, dan peran kunci dalam sistem kriptografi simetris.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-10-12

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
