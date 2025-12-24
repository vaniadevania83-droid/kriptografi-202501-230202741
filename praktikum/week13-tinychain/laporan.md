# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [judul praktikum]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
(
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi..)

---

## 2. Dasar Teori
(Fungsi Hash Kriptografis Fungsi hash adalah algoritma matematika yang memetakan data dengan ukuran sembarang menjadi string bit dengan ukuran tetap (fixed size). Dalam notasi matematis, jika $m$ adalah pesan, maka fungsi hash $H$ menghasilkan $h = H(m)$. Sifat utama yang diperlukan dalam blockchain adalah pre-image resistance (sulit mencari $m$ jika diketahui $h$) dan collision resistance (sulit menemukan dua input berbeda yang menghasilkan hash yang sama). Dalam praktikum ini digunakan SHA-256.Proof of Work (PoW) Proof of Work adalah mekanisme konsensus yang mewajibkan miner untuk memecahkan teka-teki komputasi yang sulit sebelum berhak menambahkan blok baru ke dalam blockchain. Teka-teki ini melibatkan pencarian nilai nonce sedemikian rupa sehingga hash blok memenuhi target kesulitan tertentu (misalnya, hash harus diawali dengan empat angka nol: 0000...). Rumusnya dapat digambarkan sebagai:$$H(\text{index} + \text{timestamp} + \text{data} + \text{prev\_hash} + \text{nonce}) < \text{target}$$Mekanisme ini mencegah spam dan serangan manipulasi data karena membutuhkan daya komputasi dan energi listrik yang besar.  )

---

## 3. Alat dan Bahan
(- Python 3.11  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (hashlib dan time)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `src_tinychain.py` di folder `praktikum/week13-tinychain/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Menghitung hash SHA-256 dari konten blok.
        """
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Melakukan Proof of Work dengan mencari hash yang diawali dengan jumlah '0' 
        sesuai difficulty.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"[+] Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Tingkat kesulitan (jumlah nol di awal hash)

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        # Proses mining terjadi di sini
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# --- Main Program Execution ---
if __name__ == "__main__":
    print("=== TinyChain Proof of Work Demo ===")
    my_chain = Blockchain()
    
    print("\nSedang menambang (mining) blok 1...")
    start_time = time.time()
    my_chain.add_block(Block(1, "", "Transaksi A -> B: 10 Coin"))
    print(f"Waktu mining: {time.time() - start_time:.4f} detik")

    print("\nSedang menambang (mining) blok 2...")
    start_time = time.time()
    my_chain.add_block(Block(2, "", "Transaksi B -> C: 5 Coin"))
    print(f"Waktu mining: {time.time() - start_time:.4f} detik")
    
    print("\n=== Blockchain Valid ===")
    for block in my_chain.chain:
        print(f"Index: {block.index}, Hash: {block.hash}, Data: {block.data}") ...
```
)

---

## 6. Hasil dan Pembahasan
(- Berikut adalah hasil eksekusi dari program simulasi blockchain sederhana dengan tingkat kesulitan (difficulty) sebesar 4.

Analisis Hasil: Pada percobaan di atas, program berhasil menambang dua blok baru.

1. Difficulty: Diatur ke angka 4, yang berarti hash yang valid harus dimulai dengan "0000".
2. Proses Mining: Komputer melakukan iterasi (looping) untuk mengubah nilai nonce berulang kali. Setiap kali nonce berubah, nilai hash blok berubah drastis (sifat Avalanche Effect).
3. Validasi: Loop berhenti ketika hash yang dihasilkan memenuhi kriteria (prefix "0000").
4. Waktu: Dapat diamati bahwa waktu yang dibutuhkan untuk menemukan hash yang valid bervariasi untuk setiap blok, meskipun difficulty-nya sama, karena sifat acak dari output fungsi hash. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week13-tinychain/Screenshot/Cuplikan%20layar%202025-12-24%20201156.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Fungsi hash bertindak sebagai "sidik jari" digital yang unik untuk setiap blok. Hash menjamin integritas data; jika ada satu karakter saja pada data transaksi diubah, maka hash blok tersebut akan berubah total. Selain itu, hash digunakan untuk menghubungkan blok satu dengan blok sebelumnya (previous_hash), menciptakan rantai (chain) yang tidak dapat diputus atau disisipi tanpa merusak validitas seluruh rantai setelahnya.  
- Pertanyaan 2: PoW membuat proses penambahan blok menjadi mahal secara komputasi (membutuhkan waktu dan listrik). Untuk melakukan double spending (mengubah transaksi yang sudah dikonfirmasi), penyerang harus menambang ulang blok tempat transaksi tersebut berada DAN semua blok setelahnya (karena perubahan hash akan membatalkan link ke blok berikutnya). Penyerang harus memiliki kecepatan komputasi >51% dari total jaringan untuk mengejar ketertinggalan pembuatan blok rantai yang jujur (Longest Chain Rule), yang mana hal ini sangat sulit dan mahal dilakukan.
- Pertanyaan 3: Kelemahan utama PoW adalah konsumsi energi yang masif dan sia-sia (wasteful). Jutaan prosesor di seluruh dunia berlomba menghitung hash (brute force) secara bersamaan, namun hanya satu pemenang yang bloknya diterima. Energi yang dikeluarkan oleh miner lain yang kalah terbuang begitu saja. Hal ini menyebabkan jejak karbon yang tinggi pada cryptocurrency berbasis PoW seperti Bitcoin.  
)
---

## 8. Kesimpulan
(Simulasi ini menunjukkan bahwa Proof of Work (PoW) bekerja dengan memaksa komputer melakukan usaha komputasi (brute force hash) untuk menemukan nilai nonce yang valid. Mekanisme ini secara efektif mengamankan blockchain dari modifikasi data karena biaya untuk mengubah sejarah transaksi menjadi sangat mahal. Namun, keamanan ini harus dibayar dengan efisiensi waktu dan konsumsi energi yang tinggi seiring dengan meningkatnya difficulty.  )

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
Date:   2025-12-24

    week13-cryptosystem: secret sharing (shamir's secret sharing) )
```
