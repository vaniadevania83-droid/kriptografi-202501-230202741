# src/signature.py

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# --- Inisialisasi dan Pembuatan Kunci ---
print("1. Pembuatan Kunci & Tanda Tangan")
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Kunci untuk ditampilkan (opsional, untuk demonstrasi)
print("Private Key (excerpt):", private_key.export_key('PEM').decode().split('\n')[1] + '...')
print("Public Key (excerpt):", public_key.export_key('PEM').decode().split('\n')[1] + '...')

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
print("Pesan Asli:", message.decode())

# Hitung hash pesan
h = SHA256.new(message)

# Buat tanda tangan dengan private key (Penandatanganan)
# 
signer = pkcs1_15.new(private_key)
signature = signer.sign(h)
print("Signature:", signature.hex())

# --- Verifikasi Tanda Tangan Pesan Asli (Kasus Berhasil) ---
print("2. Verifikasi Tanda Tangan (Pesan Asli)")
try:
    # Verifikasi dengan public key
    verifier_original = pkcs1_15.new(public_key)
    verifier_original.verify(h, signature)
    print("Verifikasi BERHASIL: Tanda tangan valid untuk pesan asli.")
except (ValueError, TypeError):
    print("Verifikasi GAGAL: Tanda tangan tidak valid.")

# --- Uji Modifikasi Pesan (Kasus Gagal) ---
print(" 3. Uji Modifikasi Pesan (Verifikasi Gagal)")
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
print("Pesan Modifikasi:", fake_message.decode())

# Hitung hash pesan palsu
h_fake = SHA256.new(fake_message)

try:
    # Verifikasi signature lama dengan hash pesan palsu
    verifier_fake = pkcs1_15.new(public_key)
    verifier_fake.verify(h_fake, signature)
    print("Verifikasi BERHASIL (seharusnya GAGAL).") # Ini akan terjadi hanya jika ada bug, harusnya gagal
except (ValueError, TypeError) as e:
    # Pesan yang berbeda akan menghasilkan hash yang berbeda, sehingga verifikasi akan gagal
    print(f"Verifikasi GAGAL: Tanda tangan tidak cocok dengan pesan yang diubah.")
    print(f"   Detail: {e}")