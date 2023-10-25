#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Mengenkripsi teks dengan Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()  # Untuk cek apakah karakter adalah huruf besar
            char = char.lower()  # Konversi huruf ke huruf kecil
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))  # Enkripsi karakter dengan Caesar Cipher
            if is_upper:
                encrypted_char = encrypted_char.upper()  # Konversi kembali ke huruf besar apabila semula huruf besar
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Tambahkan karakter non-huruf 

    return encrypted_text

# Fungsi untuk mendekripsikan teks Caesar Cipher
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Mendekripsi dengan menggeser mundur sebanyak shift

# Fungsi untuk mengenkripsi teks dengan Vigenere Cipher
def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()  # Cek karakter adalah huruf besar atau tidak
            char = char.lower()  # Konversi ke huruf kecil
            key_char = key[i % key_length]  # Ambil karakter kunci yang sesuai dengan indeks saat ini
            key_shift = ord(key_char) - ord('a')  # Hitung pergeseran berdasarkan karakter kunci
            encrypted_char = caesar_encrypt(char, key_shift)  # Enkripsi karakter Caesar Cipher menggunakan pergeseran kunci
            if is_upper:
                encrypted_char = encrypted_char.upper()  # Konversi kembali ke huruf besar jika semula huruf besar
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Tambahkan karakter non-huruf 

    return encrypted_text

# Fungsi untuk mendekripsikan teks Vigenere Cipher
def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()  # Cek apakah karakter adalah huruf besar
            char = char.lower()  # Konversi ke huruf kecil
            key_char = key[i % key_length]  # Ambil karakter kunci yang sesuai dengan indeks saat ini
            key_shift = ord(key_char) - ord('a')  # Hitung pergeseran berdasarkan karakter kunci
            decrypted_char = caesar_decrypt(char, key_shift)  # Mendekripsi karakter Caesar Cipher menggunakan pergeseran dari kunci
            if is_upper:
                decrypted_char = decrypted_char.upper()  # Konversi kembali ke huruf besar jika semula huruf besar
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Tambahkan karakter non-huruf 

    return decrypted_text

# Teks yang akan di Enkripsi
plaintext = "Success is not final, failure is not fatal, it is the courage to continue that counts"
vigenere_key = "sifa"
caesar_shift = 77

# Enkripsi teks dengan menggunakan Vigenere Cipher, kemudian Caesar Cipher
vigenere_encrypted_text = vigenere_encrypt(plaintext, vigenere_key) # Melakukan enkripsi Vigenere terlebih dahulu
final_encrypted_text = caesar_encrypt(vigenere_encrypted_text, caesar_shift) # Hasil vigener dienkripsi dengan Caesar

print("Teks Asli:", plaintext)
print("Hasil Enkripsi:", final_encrypted_text)

# Mendekripsi teks
decrypted_text = caesar_decrypt(final_encrypted_text, caesar_shift) # Dekrip menggunakan caesar cipher
vigenere_decrypted_text = vigenere_decrypt(decrypted_text, vigenere_key) #Dekrip hasil caesar dengan vigener

print("Hasil Dekripsi:", vigenere_decrypted_text)


# In[ ]:




