class BankAccount:
    def __init__(self, nama, saldo=0):
        self.nama = nama
        self.saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Jumlah {jumlah} berhasil disetor. Saldo Anda sekarang adalah {self.saldo}")
        else:
            print("Jumlah setoran harus lebih dari 0.")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Jumlah {jumlah} berhasil ditarik. Saldo Anda sekarang adalah {self.saldo}")
        else:
            print("Jumlah penarikan tidak valid atau melebihi saldo Anda.")

    def cek_saldo(self):
        print(f"Saldo Anda adalah {self.saldo}")


def main():
    print("Selamat datang di Bank XYZ!")
    nama_pengguna = input("Masukkan nama Anda: ")
    akun = BankAccount(nama_pengguna)

    while True:
        print("\nPilih tindakan:")
        print("1. Setor")
        print("2. Tarik")
        print("3. Cek Saldo")
        print("4. Keluar")

        pilihan = input("Masukkan nomor tindakan: ")

        if pilihan == "1":
            jumlah_setoran = float(input("Masukkan jumlah setoran: "))
            akun.setor(jumlah_setoran)
        elif pilihan == "2":
            jumlah_penarikan = float(input("Masukkan jumlah penarikan: "))
            akun.tarik(jumlah_penarikan)
        elif pilihan == "3":
            akun.cek_saldo()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor pilihan yang benar.")


if __name__ == "__main__":
    main()
