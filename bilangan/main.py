def angka(nilai):
    if nilai % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

try:
    nilai = int(input("Masukkan sebuah bilangan bulat: "))
    hasil = angka(nilai)
    print(f"angka ini adalah {hasil}")
except ValueError:
    print("Input yang Anda masukkan bukan bilangan bulat.")