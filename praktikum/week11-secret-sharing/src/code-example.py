def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Menyesuaikan shift untuk dekripsi
    if mode == 'decrypt':
        shift = -shift
    
    for i in range(len(text)):
        char = text[i]
        
        # Enkripsi/Dekripsi karakter huruf besar
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Enkripsi/Dekripsi karakter huruf kecil
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Karakter non-alfabet tidak diubah
            result += char
            
    return result

# Contoh Penggunaan
if __name__ == "__main__":
    message = input("Masukkan pesan: ")
    key = int(input("Masukkan kunci (angka): "))
    
    encrypted = caesar_cipher(message, key, 'encrypt')
    decrypted = caesar_cipher(encrypted, key, 'decrypt')
    
    print(f"\nPlaintext  : {message}")
    print(f"Ciphertext : {encrypted}")
    print(f"Decrypted  : {decrypted}")