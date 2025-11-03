def transpose_encrypt(plaintext, key=5):
    """
    Melakukan enkripsi Transposisi Kolom Sederhana.
    (Membaca pesan kolom per kolom, menghasilkan ciphertext baris per baris)
    """
    # Inisialisasi daftar untuk menampung teks terenkripsi per kolom
    ciphertext = [''] * key
    
    # Iterasi melalui setiap kolom
    for col in range(key):
        pointer = col
        # Ambil karakter dari plaintext pada posisi kolom tersebut, lalu lompat sebesar kunci
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
            
    # Gabungkan hasil dari setiap kolom untuk membentuk ciphertext
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    """
    Melakukan dekripsi Transposisi Kolom Sederhana.
    Mencari tahu dimensi grid (jumlah baris dan kolom) untuk menyusun kembali teks.
    """
    # Hitung dimensi grid
    num_of_chars = len(ciphertext)
    num_of_cols = key
    
    # Jumlah baris = ceil(panjang pesan / kunci)
    num_of_rows = int(num_of_chars / key + 0.9999) # Menggunakan +0.9999 untuk fungsi ceiling
    
    # Hitung jumlah sel 'kosong' di grid (biasanya di baris terakhir)
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - num_of_chars
    
    # Plaintext akan diisi dengan karakter sebanyak jumlah kolom
    plaintext = [''] * num_of_rows 
    
    col = 0
    row = 0
    
    # Iterasi melalui ciphertext dan mengisinya kembali ke grid secara baris-per-baris
    for char in ciphertext:
        plaintext[row] += char
        row += 1
        
        # Cek apakah sudah mencapai akhir baris atau jika sudah mencapai sel 'kosong'
        if (row == num_of_rows) or (row == num_of_rows - 1 and col >= num_of_cols - num_of_shaded_boxes):
            row = 0
            col += 1
            
    return ''.join(plaintext)

# Contoh uji coba
print("--- Transposisi Sederhana Cipher ---")
msg = "TRANSPOSITIONCIPHER"
key = 5
enc = transpose_encrypt(msg, key)
dec = transpose_decrypt(enc, key)

print(f"Plaintext (P) : {msg}")
print(f"Kunci (K) (Kolom) : {key}")
print(f"Ciphertext (C): {enc}")
print(f"Decrypted (D) : {dec}")

msg_2 = "INI PESAN RAHASIA UNTUK ANDA SEMUA"
key_2 = 4
# Transposisi umumnya hanya bekerja baik dengan huruf, jadi kita hapus spasi
msg_clean = "".join(filter(str.isalpha, msg_2.upper()))

enc_2 = transpose_encrypt(msg_clean, key_2)
dec_2 = transpose_decrypt(enc_2, key_2)

print("\nContoh 2 (Pesan bersih):")
print(f"Plaintext (P) Bersih: {msg_clean}")
print(f"Kunci (K) (Kolom) : {key_2}")
print(f"Ciphertext (C): {enc_2}")
print(f"Decrypted (D) : {dec_2}")
