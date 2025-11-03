def vigenere_encrypt(plaintext, key):
    """
    Melakukan enkripsi Vigenère Cipher.
    Kunci diulang sesuai panjang plaintext.
    """
    result = []
    # Pastikan kunci dalam huruf kecil untuk perhitungan shift
    key = key.lower()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Hitung shift berdasarkan karakter kunci saat ini (0='a', 25='z')
            shift = ord(key[key_index % len(key)]) - 97
            
            # Tentukan basis (65 untuk 'A', 97 untuk 'a')
            base = 65 if char.isupper() else 97
            
            # Enkripsi: (P + K) mod 26
            encrypted_char_code = (ord(char) - base + shift) % 26 + base
            result.append(chr(encrypted_char_code))
            
            # Maju ke karakter kunci berikutnya
            key_index += 1
        else:
            # Pertahankan karakter non-alfabet
            result.append(char)
            
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    """
    Melakukan dekripsi Vigenère Cipher.
    Dekripsi: (C - K) mod 26
    """
    result = []
    key = key.lower()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Hitung shift dari karakter kunci
            shift = ord(key[key_index % len(key)]) - 97
            
            # Tentukan basis
            base = 65 if char.isupper() else 97
            
            # Dekripsi: (C - K) mod 26
            decrypted_char_code = (ord(char) - base - shift) % 26 + base
            result.append(chr(decrypted_char_code))
            
            # Maju ke karakter kunci berikutnya
            key_index += 1
        else:
            result.append(char)
            
    return "".join(result)

# Contoh uji coba
print("--- Vigenère Cipher ---")
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)

print(f"Plaintext (P) : {msg}")
print(f"Kunci (K)     : {key}")
print(f"Ciphertext (C): {enc}")
print(f"Decrypted (D) : {dec}")

msg_2 = "SEMARANG ADALAH KOTA PENDIDIKAN"
key_2 = "RAHASIA"
enc_2 = vigenere_encrypt(msg_2, key_2)
dec_2 = vigenere_decrypt(enc_2, key_2)

print("\nContoh 2 (dengan kunci yang lebih panjang dan spasi):")
print(f"Plaintext (P) : {msg_2}")
print(f"Kunci (K)     : {key_2}")
print(f"Ciphertext (C): {enc_2}")
print(f"Decrypted (D) : {dec_2}")
