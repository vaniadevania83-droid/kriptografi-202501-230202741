def run_aes_implementation():
    """Menjalankan implementasi enkripsi dan dekripsi AES-128 (MODE_EAX)."""
    try:
        # 1. Pembangkitan Kunci (128 bit = 16 byte)
        key = get_random_bytes(16)
        
        # Data yang akan dienkripsi
        plaintext = b"Modern Cipher AES Example 128 bit" 

        # 2. Enkripsi (MODE_EAX menghasilkan ciphertext dan authentication tag)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        
        print("--- AES-128 (Advanced Encryption Standard) ---")
        print(f"Kunci (16 byte): {key.hex()}")
        print(f"Plaintext: {plaintext.decode()}")
        print(f"Nonce (IV): {cipher.nonce.hex()}")
        print(f"Ciphertext: {ciphertext.hex()}")
        print(f"Tag: {tag.hex()}")

        # 3. Dekripsi (memerlukan kunci, mode, dan nonce yang sama dari proses enkripsi)
        cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
        decrypted = cipher_dec.decrypt(ciphertext)
        
        # Verifikasi tag (penting untuk EAX)
        try:
            cipher_dec.verify(tag)
            print(f"Decrypted: {decrypted.decode()}")
        except ValueError:
            print("Verifikasi Tag Gagal: Data mungkin telah dirusak atau kunci salah.")
        
        print("-" * 43)

    except Exception as e:
        print(f"Terjadi Error pada AES: {e}")

if __name__ == "__main__":
    run_aes_implementation()