def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Pilih operasi (1: Enkripsi, 2: Dekripsi): ")
    
    if choice == "1":
        plaintext = input("Masukkan pesan yang ingin Anda enkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran: "))
        encrypted_text = encrypt(plaintext, shift)
        print(f"Pesan Terenkripsi: {encrypted_text}")
    elif choice == "2":
        ciphertext = input("Masukkan pesan yang ingin Anda dekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran: "))
        decrypted_text = decrypt(ciphertext, shift)
        print(f"Pesan Terdekripsi: {decrypted_text}")
    else:
        print("Pilihan tidak valid. Silakan pilih 1 (Enkripsi) atau 2 (Dekripsi).")

if __name__ == "__main":
    main()
