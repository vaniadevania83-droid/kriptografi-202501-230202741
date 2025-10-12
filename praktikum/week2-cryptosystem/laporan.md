# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)  
Nama: Deviana Ainul Riqoh 
NIM: 230202741 
Kelas: 5IKRB 

---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2. Menggambarkan proses enkripsi dan dekripsi sederhana.
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori
Sebuah kriptosistem adalah kerangka kerja yang terdiri dari lima elemen kunci untuk mengamankan komunikasi: pesan asli (plaintext), pesan tersandi (ciphertext), algoritma enkripsi dan dekripsi (metode matematis untuk transformasi), serta kunci (parameter rahasia yang mengendalikan proses). Dalam sistem modern, algoritma biasanya bersifat publik, dan keamanan sistem sepenuhnya bergantung pada kerahasiaan kunci yang digunakan. Secara umum, kriptosistem terbagi menjadi dua kelompok utama: kriptografi simetris, yang menggunakan satu kunci yang sama untuk menyandikan dan membuka sandi; dan kriptografi asimetris (kunci publik), yang menggunakan sepasang kunci berbeda—satu kunci publik untuk mengenkripsi dan satu kunci privat untuk mendekripsi.

---

## 3. Alat dan Bahan
(- Python 3.11  
- Visual Studio Code   
- Git dan akun GitHub  
- Draw.io  )

---

## 4. Langkah Percobaan
1. Membuat diagram/skema alur kerja kriptosistem dasar yang menggambarkan proses enkripsi dan dekripsi, lalu menyimpannya sebagai screenshots/diagram_kriptosistem.png.
2. Membuat file Python bernama simple_crypto.py di dalam folder praktikum/week2-cryptosystem/src/.
3. Menyalin dan menulis kode program dari modul praktikum untuk mengimplementasikan Caesar Cipher sederhana.
4. Mengubah variabel message di dalam program menjadi (<2310112345>).
5. Menjalankan program dari terminal dengan perintah python src/simple_crypto.py.
6. Mengambil screenshot hasil eksekusi program dan menyimpannya sebagai screenshots/hasil_eksekusi.png.
7. Menyusun laporan laporan.md yang berisi semua komponen, dari tujuan hingga jawaban diskusi.
8. Melakukan commit dan push ke repositori GitHub dengan pesan week2-cryptosystem.

---

## 5. Source Code
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


## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week2-cryptosystem/screensshot/hasil_eksekusi.png)
![Hasil Input](/praktikum/week2-cryptosystem/screensshot/diagram_kriptosistem.jpg)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
