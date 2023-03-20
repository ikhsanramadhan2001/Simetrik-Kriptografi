# Description: Shift Cipher

# Fungsi untuk mengenkripsi pesan dengan algoritma shift cipher
def encrypt(message, key):
    cipher = ''  # inisialisasi variabel cipher
    for char in message:
        if char.isupper():  # jika karakter saat ini adalah huruf kapital
            # tambahkan karakter yang telah dienkripsi ke variabel cipher
            cipher += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():  # jika karakter saat ini adalah huruf kecil
            # tambahkan karakter yang telah dienkripsi ke variabel cipher
            cipher += chr((ord(char) - 97 + key) % 26 + 97)
        else:  # jika karakter saat ini bukan huruf
            cipher += char  # tambahkan karakter asli ke variabel cipher
    return cipher

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan algoritma shift cipher


def decrypt(cipher, key):
    message = ''  # inisialisasi variabel message
    for char in cipher:
        if char.isupper():  # jika karakter saat ini adalah huruf kapital
            # tambahkan karakter yang telah didekripsi ke variabel message
            message += chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():  # jika karakter saat ini adalah huruf kecil
            # tambahkan karakter yang telah didekripsi ke variabel message
            message += chr((ord(char) - 97 - key) % 26 + 97)
        else:  # jika karakter saat ini bukan huruf
            message += char  # tambahkan karakter asli ke variabel message
    return message

# Fungsi utama


def main():
    message = input('Masukkan pesan: ')  # input pesan
    # NIM L200204207
    # Menggunakan shift 07, dikarenakan 2 Digit terakhir NIM saya adalah 07
    key = 7  # inisialisasi variabel key
    cipher = encrypt(message, key)  # enkripsi pesan
    # cetak pesan yang telah dienkripsi
    print('Pesan yang telah dienkripsi: ', cipher)
    # cetak pesan yang telah didekripsi
    print('Pesan yang telah didekripsi: ', decrypt(cipher, key))


# Panggil fungsi utama
if __name__ == '__main__':
    main()
