def caesar_encrypt(plaintext, key): # Baris 4
    """ # Baris 5
    Melakukan enkripsi Caesar Cipher. # Baris 6
    Logika enkripsi: (P + K) mod 26. # Baris 7
    """ # Baris 8
    return "".join( # Baris 9
        # Terapkan pergeseran hanya pada karakter alfabet. # Baris 10
        chr((ord(char) - # Baris 11
             (base := ord('A') if char.isupper() else ord('a')) # Tentukan basis (A/a) # Baris 12
             + key) % 26 + base) # Terapkan pergeseran dan modulus 26 # Baris 13
        if char.isalpha() # Cek huruf # Baris 14
        else char # Pertahankan karakter lain # Baris 15
        for char in plaintext # Iterasi # Baris 16
    ) # Baris 17

def caesar_decrypt(ciphertext, key): # Baris 18
    """ # Baris 19
    Melakukan dekripsi dengan kunci negatif. # Baris 20
    """ # Baris 21
    return caesar_encrypt(ciphertext, -key) # Baris 22

if __name__ == "__main__": # Blok eksekusi utama # Baris 23
    print("--- Caesar Cipher Uji Coba (30 Baris) ---") # Baris 24
    
    # Contoh 1: Menggabungkan Uppercase dan Lowercase # Baris 25
    msg = "Cipher Klasik (Kunci 10)" # Baris 26
    key = 10 # Baris 27
    enc = caesar_encrypt(msg, key) # Baris 28
    dec = caesar_decrypt(enc, key) # Baris 29
    print(f"P: {msg}\nK: {key}\nC: {enc}\nD: {dec}") # Baris 30
