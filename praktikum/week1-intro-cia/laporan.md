# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: [Intro CIA]  
Nama: [Deviana Ainul Riqoh]  
NIM: [230202741]  
Kelas: [5IKRB]  

---

## 1. Tujuan
•	Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
•	Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan Benar.
•	Menyimpulkan peraan kriptografi dalam sistem keamanan informasi modern.
•	Menyiapkan repositori GitHub sebagai media kerja praktikum.

---

## 2. Dasar Teori
Kriptografi merupakan bidang ilmu sekaligus seni yang berfokus pada upaya menjaga kerahasiaan dan keamanan pesan. Perkembangannya terbagi dalam dua masa, yaitu era klasik dan era modern. Pada masa klasik, metode seperti Caesar Cipher dan Vigenère Cipher bekerja dengan memanipulasi huruf-huruf dalam teks dan sangat bergantung pada kerahasiaan teknik penyandiannya. Namun, dengan kemajuan teknologi komputer, muncul kriptografi modern yang didasarkan pada konsep matematika yang lebih kompleks. Dalam era ini, keamanan sistem tidak lagi bergantung pada kerahasiaan algoritmanya, melainkan pada kunci enkripsi, sesuai dengan Prinsip Kerckhoffs. Beberapa algoritma modern yang populer dan menjadi dasar keamanan digital saat ini antara lain AES (kriptografi simetris) dan RSA (kriptografi asimetris).
Dalam konteks keamanan informasi, terdapat tiga komponen utama yang dikenal dengan istilah CIA Triad, yaitu Confidentiality (menjaga data agar tidak diakses pihak yang tidak berwenang), Integrity (menjamin data tetap utuh dan tidak diubah secara tidak sah), serta Availability (memastikan data dapat diakses ketika dibutuhkan oleh pengguna yang berhak). Kriptografi berperan penting dalam penerapan ketiga prinsip tersebut, khususnya dalam menjaga kerahasiaan dan integritas data.

---

## 3. Alat dan Bahan
•	Leptop
•	Visual Studio Code
•	Akun GitHub yang aktif

---

## 4. Langkah Percobaan
•	Melakukan fork.
•	Menngubah nama repositori hasil fork.
•	Melakukan clone repositori yang sudah diubah namanya ke komputer lokal.
•	Membuat struktur folder baru di dalam repositori lokal.
•	Di dalam ringkasan mengenai sejarah kriptografi dan prinsip CIA di dalam file lapoan.md .
•	Menjawab pertanyaan quiz yang diberikan di dalam file laporan.md .
•	Mengambil screenshot sebagai bukti penyiapan repositori dan menyimpannya di folder screenshots/ .
•	Menambahkan (add), melakukan commit (commits), dan mengirim (push) perubahan ke repositori GitHub dengan pesan commit week1-intro-cia .

---

## 5. Source Code
pada praktikum minggu ini tidak ada pembuatan atau modifikasi source code program. Kegiatan berfokus pada penyimpanan lingkungan kerja dan penyusuan laporan.

---

## 6. Hasil dan Pembahasan
Praktikum ini telah terlaksana dengan baik melalui penyiapan repositori GitHub sebagai sarana kerja serta penyusunan laporan pendahuluan. Proses fork, clone, dan penyesuaian struktur repositori telah dilakukan dengan sukses. Selain itu, laporan yang memuat rangkuman materi dan hasil pengerjaan kuis telah disusun sesuai dengan ketentuan yang diberikan.
Berikut adalah bukti Screenshot :


---

## 7. Jawaban Pertanyaan
Soal 1 : Ringkasan Sejarah Kriptografi
1. Era Kriptografi Klasik: Metode Manual
•	Caesar Cipher: adalah sandi substitusi monoalfabetik tertua yang dikenal, di mana setiap huruf diganti dengan huruf lain dengan pergeseran tetap di seluruh pesan. Meskipun sederhana, keamanannya rendah karena mudah dipecahkan dengan analisis frekuensi.
•	Vigenere Cipher: adalah pengembangan yang jauh lebih kuat, menggunakan substitusi polialfabetik dengan kata kunci untuk menerapkan beberapa pergeseran Caesar yang berbeda. Teknik ini menyamarkan pola frekuensi huruf secara efektif, menjadikannya sangat sulit dipecahkan dan dijuluki "cipher yang tidak dapat dipecahkan" selama beberapa waktu.
•	Batasan Utama: bahwa kunci enkripsi dan dekripsi harus dibagikan secara rahasia, dan mereka rentan terhadap serangan analisis frekuensi yang dilakukan dengan tangan atau, dengan mesin.
2. Perkembangan Kriptografi Modern: Era Digital
Kriptografi modern terbagi menjadi dua era utama berdasarkan jenis kuncinya:
1.	Kriptografi Kunci Simetris (Satu Kunci)
o	Menggunakan kunci yang sama untuk mengenkripsi dan mendeskripsi data.
o	AES (Advanced Encryption Standard). Ini adalah cipher blok simetris yang sangat cepat, kuat, dan kini menjadi standar global untuk mengamankan data (misalnya, Wi-Fi dan komunikasi online).
2.	Kriptografi Kunci Asimetris (Kunci Publik)
o	Menggunakan sepasang kunci: Kunci Publik (dibagikan untuk enkripsi) dan Kunci Pribadi (dirahasiakan untuk dekripsi). Ini memecahkan masalah berbagi kunci secara rahasia.
o	RSA (Rivest-Shamir-Adleman). Sistem ini memungkinkan komunikasi aman tanpa harus bertemu untuk bertukar kunci rahasia terlebih dahulu. RSA juga digunakan untuk Tanda Tangan Digital.
Kriptografi modern menjamin tiga hal utama dalam keamanan data:
•	Kerahasiaan (melalui Enkripsi)
•	Integritas (melalui Fungsi Hash)
•	Otentikasi (melalui Tanda Tangan Digital)
3. Evolusi menuju Kriptografi Kontemporer: Kepercayaan Terdesentralisasi
•	Blockchain: Sebuah buku besar (ledger) terdistribusi yang mencatat transaksi secara permanen. Blockchain menggunakan fungsi hash dan tanda tangan digital untuk menghubungkan blok data, sehingga catatan di masa lalu hampir mustahil diubah. Inovasi terbesarnya adalah menciptakan konsensus di jaringan yang tidak saling percaya.
•	Cryptocurrency: Aplikasi paling terkenal dari blockchain (seperti Bitcoin), yang memungkinkan transfer nilai dari satu pihak ke pihak lain (peer-to-peer) tanpa perlu bank atau perantara terpusat.
Soal 2 : Detail Prinsip CIA
1. Confidentiality (Kerahasiaan) 
•	Menjaga data sensitif agar hanya bisa diakses oleh pihak yang berwenang melalui Enkripsi dan Kontrol Akses.
•	Contoh :
o	Pesan WhatsApp yang diamankan dengan Enkripsi End-to-End, memastikan hanya pengirim dan penerima yang dapat membaca isi pesan tersebut.
2. Integrity (Integritas) 
•	Memastikan data akurat dan utuh (tidak dimodifikasi secara tidak sah) melalui Fungsi Hash atau Tanda Tangan Digital.
•	Contoh :
o	Membandingkan nilai SHA-256 Checksum dari file unduhan. Jika nilai hash cocok, itu membuktikan file tersebut belum dirusak sejak dikeluarkan oleh sumbernya.
3. Availability (Ketersediaan) 
•	Menjamin sistem atau layanan selalu berfungsi dan dapat diakses oleh pengguna yang berhak, dicapai melalui Redundansi dan Pemulihan Bencana.
•	Contoh :
o	Bank online menggunakan server yang didistribusikan (Redundansi) dan Load Balancing untuk memastikan layanan tetap online dan tersedia 24/7, bahkan saat terjadi kegagalan sistem atau serangan DDoS.
Soal Quiz
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
Tokoh yang secara luas diakui sebagai bapak kriptografi modern adalah Claude Shannon. Kontribusinya yang paling signifikan adalah makalah “Communication Theory of Secrecy Systems” (1949), yang memperkenalkan dasar-dasar matematika untuk keamanan kriptografi melalui konsep confusion dan diffusion.
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
1.	RSA (Rivest Shamir Adleman): Algoritma klasik yang didasarkan pada kesulitan matematis faktorisasi bilangan prima besar. Digunakan luas untuk tanda tangan digital dan pertukaran kunci dalam protokol seperti TLS/SSL.
2.	ECC (Elliptic Curve Cryptography): Algoritma yang menawarkan keamanan setara dengan RSA tetapi dengan ukuran kunci yang jauh lebih kecil, menjadikannya lebih efisien untuk perangkat mobile dan lingkungan dengan sumber daya terbatas.
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
Perbedaan utama antara kriptografi klasik dan modern terletak pada basis operasional dan manajemen kunci. Kriptografi klasik didasarkan pada manipulasi karakter dan bahasa (seperti substitusi huruf) dan hanya menggunakan kunci simetris yang dibagikan secara rahasia, membuatnya rentan terhadap analisis frekuensi. Sebaliknya, kriptografi modern beroperasi pada bit menggunakan prinsip matematika kompleks dan memanfaatkan baik kunci simetris yang kuat (seperti AES) maupun kunci asimetris (publik/pribadi, seperti RSA) untuk mengatasi masalah distribusi kunci dan meningkatkan keamanan ke level yang jauh lebih tinggi.

---

## 8. Kesimpulan
Praktikum ini memberikan pemahaman awal tentang perkembangan kriptografi dari masa klasik hingga modern, serta memperkenalkan konsep dasar keamanan informasi melalui prinsip CIA Triad. Selain itu, lingkungan kerja menggunakan Git dan GitHub telah berhasil dikonfigurasi dengan baik untuk mendukung pelaksanaan praktikum berikutnya.

---

## 9. Daftar Pustaka

---

## 10. Commit Log

![Repo Setup](/praktikum/week1-intro-cia/Screenshot/repository.png)

```
(commit 2ee05ea85fbd987754df5ac61c0bc6878b71de10
Author: Deviana Ainul Riqh <vaniadevania83@gmail.com>
Date:   2025-09-12

    week1-intro: sejrah kriptografi dan prisip CIA )
```