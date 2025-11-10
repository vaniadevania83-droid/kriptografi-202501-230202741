from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes # Diperlukan secara implisit oleh RSA.generate()

def run_rsa_simple():
    """Menjalankan implementasi enkripsi dan dekripsi RSA (OAEP) yang disederhanakan."""
    try:
        plaintext = b"Pesan Rahasia Sederhana RSA"
        
        # 1. Pembangkitan Kunci (2048 bit)
        key = RSA.generate(2048)
        private_key = key
        public_key = key.publickey()
        
        # 2. Enkripsi (Public Key)
        cipher_rsa = PKCS1_OAEP.new(public_key)
        ciphertext = cipher_rsa.encrypt(plaintext)
        
        # 3. Dekripsi (Private Key)
        decipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted = decipher_rsa.decrypt(ciphertext)
        
        print("--- RSA Simplified ---")
        print(f"Plaintext Asli: {plaintext.decode()}")
        print(f"Ciphertext (Hex): {ciphertext.hex()[:60]}...")
        print(f"Dekripsi Sukses: {decrypted.decode()}")
        print("-" * 20)

    except Exception as e:
        print(f"Terjadi Error pada RSA: {e}")

if __name__ == "__main__":
    run_rsa_simple()