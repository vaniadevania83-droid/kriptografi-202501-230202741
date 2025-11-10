from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad # Tambahkan impor untuk padding

# --- Parameter Kunci & Cipher ---
key = get_random_bytes(8) # Kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

# --- Proses Enkripsi ---
# Plaintext lebih panjang, tidak kelipatan 8, atau sembarang
plaintext = b"Ini adalah pesan rahasia yang lebih panjang." 

# Lakukan padding agar panjang plaintext menjadi kelipatan 8 byte
padded_plaintext = pad(plaintext, DES.block_size) 
print("Panjang Plaintext (setelah padding):", len(padded_plaintext))

ciphertext = cipher.encrypt(padded_plaintext)
print("Ciphertext:", ciphertext.hex()) # Tampilkan sebagai hex agar lebih mudah dibaca

# --- Proses Dekripsi ---
# Objek decipher harus dibuat ulang (best practice, walau bisa menggunakan objek cipher yang sama)
decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)

# Hapus padding untuk mendapatkan plaintext asli
try:
    unpadded_decrypted = unpad(decrypted, DES.block_size)
    print("Decrypted:", unpadded_decrypted.decode())
except ValueError:
    print("Gagal mendekripsi atau membatalkan padding.")