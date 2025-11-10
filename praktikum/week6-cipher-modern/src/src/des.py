def run_des_simulation():
    """Menjalankan simulasi enkripsi dan dekripsi DES (MODE_ECB)."""
    try:
        # 1. Pembangkitan Kunci (64 bit = 8 byte)
        key = get_random_bytes(8)
        
        # Data yang akan dienkripsi (harus kelipatan 8 byte untuk ECB)
        plaintext = b"ABCDEFGH" 

        # 2. Enkripsi
        cipher = DES.new(key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        
        print("--- DES (Data Encryption Standard) ---")
        print(f"Kunci (8 byte): {key.hex()}")
        print(f"Plaintext: {plaintext.decode()}")
        print(f"Ciphertext: {ciphertext.hex()}")

        # 3. Dekripsi
        # Kunci dan mode harus sama.
        decipher = DES.new(key, DES.MODE_ECB)
        decrypted = decipher.decrypt(ciphertext)
        
        print(f"Decrypted: {decrypted.decode()}")
        print("-" * 37)

    except Exception as e:
        print(f"Terjadi Error pada DES: {e}")

if __name__ == "__main__":
    run_des_simulation()