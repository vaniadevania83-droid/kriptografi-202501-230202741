from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Pastikan Anda sudah mengimpor pustaka yang diperlukan
# from Crypto.Cipher import AES 
# from Crypto.Random import get_random_bytes
# (Diasumsikan sudah ada di lingkungan eksekusi)

def run_aes_implementation():
    """Menjalankan implementasi enkripsi dan dekripsi AES-128 (MODE_EAX) 
       dengan penambahan Associated Data (Header)."""
    try:
        # 1. Pembangkitan Kunci (128 bit = 16 byte)
        key = get_random_bytes(16)
        
        # Data yang akan dienkripsi
        plaintext = b"Modern Cipher AES Example 128 bit (Pesan Rahasia)" 

        # DATA TAMBAHAN yang akan diverifikasi integritasnya, tetapi TIDAK dienkripsi
        header = b"Version=1.0; UserID=456; Timestamp=2025-11-10"
        
        # 2. Enkripsi (MODE_EAX menghasilkan ciphertext dan authentication tag)
        cipher = AES.new(key, AES.MODE_EAX)
        
        # Tambahkan header ke cipher.heuristic (penting!)
        cipher.update(header) 
        
        # Enkripsi data utama dan dapatkan tag
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        
        print("--- AES-128 (Advanced Encryption Standard) ---")
        print(f"Kunci (16 byte): {key.hex()}")
        print(f"Associated Data (Header): {header.decode()}")
        print(f"Plaintext: {plaintext.decode()}")
        print(f"Nonce (IV): {cipher.nonce.hex()}")
        print(f"Ciphertext: {ciphertext.hex()}")
        print(f"Tag: {tag.hex()}")

        # ------------------------------------------------------------------
        
        # 3. Dekripsi (memerlukan kunci, mode, dan nonce yang sama dari proses enkripsi)
        cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
        
        # PENTING: Panggil cipher.update() lagi dengan Associated Data yang SAMA
        # Associated Data (header) harus diverifikasi sebelum dekripsi.
        cipher_dec.update(header) 
        
        decrypted = cipher_dec.decrypt(ciphertext)
        
        # Verifikasi tag (penting untuk EAX)
        try:
            cipher_dec.verify(tag)
            print(f"Decrypted: {decrypted.decode()}")
            print("\n**Integritas data (Plaintext & Header) Terverifikasi!**")
        except ValueError:
            # Ini akan terpicu jika ciphertext, tag, header, atau kunci diubah
            print("Verifikasi Tag Gagal: Data (Ciphertext/Header) mungkin telah dirusak atau kunci salah.")
        
        print("-" * 43)

    except Exception as e:
        print(f"Terjadi Error pada AES: {e}")

if __name__ == "__main__":
    run_aes_implementation()