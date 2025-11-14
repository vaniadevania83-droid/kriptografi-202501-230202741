# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: [diffie-hellman]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).
---

## 2. Dasar Teori
Protokol Diffie-Hellman adalah sebuah mekanisme pertukaran kunci kriptografi yang memungkinkan dua pihak menetapkan kunci rahasia bersama melalui saluran yang tidak aman, tanpa perlu sebelumnya berbagi rahasia; protokol ini bukan mekanisme enkripsi. Keamanannya didasarkan pada kesulitan komputasi dalam memecahkan Masalah Logaritma Diskrit (DLP), yaitu sulitnya mencari eksponen rahasia (a \text{ atau } b) dari nilai publik (A=g^a \pmod{p}). Proses utamanya melibatkan kedua pihak memilih rahasia pribadi, menghitung kunci publik yang dipertukarkan, dan kemudian menggunakan kunci publik lawan bersama rahasia pribadi mereka untuk mencapai satu kunci simetris yang identik, yaitu K = g^{ab} \pmod{p}, untuk mengamankan komunikasi selanjutnya.
---

## 3. Alat dan Bahan
1. Python
2. Visual Studio Code
3. Git dan akun GitHub

---

## 4. Langkah Percobaan
1. Membuat project baru dan repository Git, serta membuat file program, misalnya diffie_hellman.py.
2. Mendefinisikan dua parameter publik yang akan disepakati oleh Alice dan Bob, yaitu:
•	Bilangan prima besar (p).
•	Basis atau generator (g).
3. Membuat fungsi atau bagian program untuk Alice dan Bob:
•	Masing-masing pihak memilih bilangan rahasia (a \text{ dan } b) (kunci privat).
•	Masing-masing pihak menghitung kunci publik mereka, A = g^a \pmod{p} dan B = g^b \pmod{p}.
4. Mensimulasikan pertukaran kunci publik $A$ dan $B$.
5. Masing-masing pihak menghitung kunci rahasia bersama $K$:
•	Alice menghitung K_A = B^a \pmod{p}.
•	Bob menghitung K_B = A^b \pmod{p}.
6. Memverifikasi bahwa K_A dan K_B adalah sama (kunci rahasia bersama telah berhasil didirikan).
7. Menjalankan program dengan perintah, misalnya, python diffie_hellman.py.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# --- Parameter Publik (Disepakati) ---
P = 23 # Bilangan prima
G = 5  # Generator

# --- Pihak Alice ---
def alice_turn():
    # Kunci Rahasia Alice (a)
    a_private = 6
    print(f"Alice memilih kunci rahasia (a): {a_private}")
    
    # Hitung Kunci Publik Alice (A)
    # A = G^a mod P
    A_public = pow(G, a_private, P)
    print(f"Kunci Publik Alice (A): {G}^{a_private} mod {P} = {A_public}")
    return a_private, A_public

# --- Pihak Bob ---
def bob_turn():
    # Kunci Rahasia Bob (b)
    b_private = 15
    print(f"Bob memilih kunci rahasia (b): {b_private}")

    # Hitung Kunci Publik Bob (B)
    # B = G^b mod P
    B_public = pow(G, b_private, P)
    print(f"Kunci Publik Bob (B): {G}^{b_private} mod {P} = {B_public}")
    return b_private, B_public

# --- Pertukaran Kunci dan Hasil Akhir ---
def exchange_and_calculate(A, B, a, b):
    print("\n--- Pertukaran Kunci Publik (A dan B) ---")
    
    # Alice menghitung kunci rahasia bersama (K_A)
    # K_A = B^a mod P
    K_A = pow(B, a, P)
    print(f"Alice menghitung Kunci Bersama (K_A): {B}^{a} mod {P} = {K_A}")

    # Bob menghitung kunci rahasia bersama (K_B)
    # K_B = A^b mod P
    K_B = pow(A, b, P)
    print(f"Bob menghitung Kunci Bersama (K_B): {A}^{b} mod {P} = {K_B}")

    print("\n--- Verifikasi ---")
    if K_A == K_B:
        print(f"Kedua kunci bersama sama! Kunci Rahasia Bersama: {K_A}")
    else:
        print("Gagal! Kedua kunci tidak sama.")

# --- Eksekusi Program Utama ---
if __name__ == "__main__":
    print(f"Parameter Publik: P={P}, G={G}")
    
    a_private, A_public = alice_turn()
    b_private, B_public = bob_turn()
    
    exchange_and_calculate(A_public, B_public, a_private, b_private)
```
)

---

## 6. Hasil dan Pembahasan
(Hasil eksekusi program sesuai ekspektasi, memvalidasi Protokol Diffie-Hellman melalui tiga tahap: Generasi Kunci Publik (Alice menghasilkan A=8 dan Bob menghasilkan B=19), Generasi Kunci Bersama (Alice menghitung K_A = B^a \pmod{P} dan Bob menghitung K_B = A^b \pmod{P}), dan Verifikasi yang menunjukkan bahwa kedua kunci rahasia bersama adalah sama, yaitu 2. Kesamaan ini membuktikan keberhasilan penetapan kunci identik melalui saluran tidak aman, di mana keamanan kunci 2 tersebut dijamin oleh kerumitan komputasi untuk memecahkan Masalah Logaritma Diskrit yang diperlukan untuk menemukan kunci rahasia pribadi a atau b dari nilai-nilai publik yang diketahui. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week7-diffie-hellman/screenshot/hasil-diffie-hellman.png)

)

---

## 7. Jawaban Pertanyaan
1.	Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
Protokol Diffie-Hellman memungkinkan penetapan kunci rahasia bersama melalui saluran publik yang tidak aman karena mengandalkan sifat asimetris dari Masalah Logaritma Diskrit (Discrete Logarithm Problem/DLP) dalam aritmetika modular.
1.	Publik vs. Rahasia: Protokol ini menggunakan parameter publik (P dan G) dan nilai-nilai yang dipertukarkan (Kunci Publik A dan B). Namun, untuk menghasilkan kunci bersama (K), pihak manapun (Alice atau Bob) harus mengetahui kunci rahasia pribadi mereka (a atau b).
2.	Kunci Bersama: Kunci bersama K dihitung sebagai K = g^{ab} \pmod{P}$. Meskipun eavesdropper (penyadap) mengetahui g^a \pmod{P} dan g^b \pmod{P}, sangat sulit secara komputasi untuk menghitung eksponen rahasia a atau b (memecahkan DLP) ketika P adalah bilangan prima yang sangat besar.
3.	Kerahasiaan Eksponen: Karena penyadap tidak dapat menentukan eksponen rahasia a atau b dalam waktu yang wajar, penyadap juga tidak dapat menghitung kunci bersama K. Ini memastikan bahwa rahasia K hanya diketahui oleh dua pihak yang memiliki eksponen pribadi yang benar.

2.	Apa kelemahan utama protokol Diffie-Hellman murni?
Kelemahan utama dari protokol Diffie-Hellman murni (tanpa modifikasi atau integrasi tambahan) adalah kurangnya otentikasi dari pihak-pihak yang berkomunikasi.
•	Protokol DH dasar hanya membuktikan bahwa kedua pihak telah mencapai kunci rahasia bersama; ia tidak membuktikan identitas siapa yang berada di ujung komunikasi.
•	Kelemahan ini secara langsung membuka pintu bagi Serangan Man-in-the-Middle (MITM). Penyerang (Eve) dapat menyamar sebagai Alice di mata Bob, dan sebagai Bob di mata Alice, sehingga Eve menjalin dua kunci rahasia terpisah (satu dengan Alice dan satu dengan Bob) dan dapat membaca serta memodifikasi semua komunikasi di antara keduanya.

3.	Bagaimana cara mencegah serangan MITM pada protokol ini?
Serangan MITM dicegah dengan menambahkan mekanisme yang memberikan otentikasi identitas ke dalam proses pertukaran kunci. Cara yang paling umum dilakukan adalah:
1.	Sertifikat Digital (PKI):
o	Setiap pihak (Alice dan Bob) menggunakan Sertifikat Digital yang dikeluarkan oleh Certificate Authority (CA) tepercaya. Sertifikat ini secara kriptografi mengikat kunci publik mereka ke identitas mereka yang sebenarnya.
o	Dalam protokol modern seperti TLS/SSL, pertukaran kunci DH (atau varian seperti DHE/ECDHE) hanya dilakukan setelah server (dan terkadang klien) membuktikan identitasnya menggunakan tanda tangan digital dari sertifikatnya.
2.	Diffie-Hellman Tanda Tangan (Signed DH):
o	Pihak-pihak yang berkomunikasi menandatangani (menggunakan kunci privat yang sudah ada, misalnya dari RSA atau ECDSA) nilai-nilai kunci publik DH yang mereka hasilkan (A atau B) sebelum mengirimkannya.
o	Penerima memverifikasi tanda tangan menggunakan kunci publik yang diketahui dari pengirim. Jika tanda tangan valid, penerima yakin bahwa kunci publik DH tersebut benar-benar berasal dari pihak yang diklaim.


---

## 8. Kesimpulan
Protokol Diffie-Hellman berhasil dalam menciptakan kunci rahasia bersama yang identik antara dua pihak (Alice dan Bob) melalui saluran yang tidak aman, seperti yang ditunjukkan oleh kesamaan nilai K_A dan K_B. Keamanan protokol ini didasarkan pada kerumitan komputasi untuk memecahkan Masalah Logaritma Diskrit pada bilangan prima besar. Namun, Diffie-Hellman yang mendasar rentan terhadap serangan Man-in-the-Middle karena kurangnya mekanisme otentikasi, sehingga implementasi di dunia nyata harus menggabungkannya dengan sistem Sertifikat Digital (PKI) untuk memverifikasi identitas.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Deviana Ainul Riqoh <vaniadevania83@gmail.com>
Date:   2025-11-12

    week7-cryptosystem: diffie-hellman )
```
