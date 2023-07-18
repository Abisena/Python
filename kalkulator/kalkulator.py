def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        raise ValueError("Tidak dapat melakukan pembagian dengan nol.")
    return x / y

def kalkulator():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

    if pilihan not in ('1', '2', '3', '4'):
        print("Pilihan tidak valid.")
        return

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        hasil = tambah(angka1, angka2)
    elif pilihan == '2':
        hasil = kurang(angka1, angka2)
    elif pilihan == '3':
        hasil = kali(angka1, angka2)
    else:
        hasil = bagi(angka1, angka2)

    print("Hasil: ", hasil)

if __name__ == "__main__":
    kalkulator()
