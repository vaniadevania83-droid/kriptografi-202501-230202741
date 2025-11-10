def run_rsa_implementation():
    """Menjalankan implementasi pembangkitan kunci, enkripsi, dan dekripsi RSA."""
    try:
        # 1. Pembangkitan Pasangan Kunci (2048 bit)
        print("--- RSA (Rivest–Shamir–Adleman) ---")
        print("Membangkitkan pasangan kunci 2048 bit...")
        key = RSA.generate(2048)
        private_key = key
        public_key = key.publickey()
        print("Pembangkitan Kunci Selesai.")

        # Data yang akan dienkripsi (harus lebih pendek dari ukuran kunci dikurangi padding)
        plaintext = b"RSA Asymmetric Cipher Example"
        
        # 2. Enkripsi dengan Public Key
        cipher_rsa = PKCS1_OAEP.new(public_key)
        ciphertext = cipher_rsa.encrypt(plaintext)
        
        print(f"\nPlaintext: {plaintext.decode()}")
        print(f"Panjang Ciphertext: {len(ciphertext)} bytes")
        print(f"Ciphertext (sample 64 byte): {ciphertext[:64].hex()}...")

        # 3. Dekripsi dengan Private Key
        decipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted = decipher_rsa.decrypt(ciphertext)
        
        print(f"\nDecrypted: {decrypted.decode()}")
        print("-" * 38)

    except Exception as e:
        print(f"Terjadi Error pada RSA: {e}")

if __name__ == "__main__":
    run_rsa_implementation()