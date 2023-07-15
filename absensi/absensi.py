import psycopg2

class Absen():
    def __init__(self):
        self.name = input("Masukkan nama Anda: ")
        self.keterangan = input("Masukkan keterangan absensi Anda: ")
        self.nilai = int(input("Masukkan nilai harian Anda: "))
        self.tanggal = input("Masukkan tanggal absensi Anda (format: YYYY-MM-DD): ")
        
    def cek_nama(self):
        if not self.name.strip():
            return "Nama tidak boleh kosong, silahkan isi terlebih dahulu."
        elif self.name == self.name:
            return "Silahkan lanjut isi keterangan :D"
        else:
            return "Nama salah, silahkan coba lagi dengan benar."
        
    def data_nilai(self):
        if not self.nilai:
            return "Nilai Kosong"
        elif self.nilai <= 75 :
            return "Remedial"
        else:
            return "Alhamdulillah"
            

if __name__ == "__main__":
    absensi = Absen()

    while True:
        result = absensi.cek_nama()
        print(result)
        cek_result = absensi.data_nilai()
        print(cek_result)
        
        if result == "Silahkan lanjut isi keterangan :D":
            break
        if cek_result == "Terima Kasih Sudah Mengisi :)":
            break
        
    # Menyimpan data ke dalam database PostgreSQL
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="admin12345",
            host="localhost",
            port="5432",
            database="postgres"
        )

        cursor = connection.cursor()

        # Query untuk menyimpan data absensi ke dalam tabel absensi
        query = "INSERT INTO absensi (nama, keterangan, nilai, tanggal) VALUES (%s, %s, %s, %s);"
        data = (absensi.name, absensi.keterangan, absensi.nilai, absensi.tanggal)

        cursor.execute(query, data)
        connection.commit()

        print("Data berhasil disimpan ke dalam database.")

    except (Exception, psycopg2.Error) as error:
        print("Error saat menyimpan data:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Koneksi ke database ditutup.")
