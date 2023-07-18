import csv
import psycopg2

class Absen():
    def __init__(self, csv_file=None):
        if csv_file:
            with open(csv_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                row = next(reader)
                self.name = row.get('nama')
                self.keterangan = row.get('keterangan')
                self.nilai = int(row.get('nilai'))
                self.tanggal = row.get('tanggal')
        else:
            self.name = input("Masukkan nama Anda: ")
            self.keterangan = input("Masukkan keterangan absensi Anda: ")
            self.nilai = int(input("Masukkan nilai harian Anda: "))
            self.tanggal = input("Masukkan tanggal absensi Anda (format: YYYY-MM-DD): ")
            self.info = None
        
    def cek_nama(self):
        if not self.name.strip():
            return "Nama tidak boleh kosong, silahkan isi terlebih dahulu."
        else:
            return "Silahkan lanjut isi keterangan :D"
        
    def data_nilai(self):
        if not self.nilai:
            return "Nilai Kosong"
        elif self.nilai <= 75 :
            return "Remedial"
        else:
            return "Alhamdulillah"
        
    def cek_promosi_kelas(self):
        if self.data_nilai() == "Alhamdulillah":
            self.info = "naik kelas."
        else:
            self.info = "Maaf, Anda harus mengulang tahun depan."
    
if __name__ == "__main__":
    csv_file_path = input("Masukkan path file CSV (kosongkan jika ingin input manual): ")
    absensi = Absen(csv_file_path)

    while True:
        result = absensi.cek_nama()
        print(result)
        cek_result = absensi.data_nilai()
        print(cek_result)
        absensi.cek_promosi_kelas()
        print("Status Promosi Kelas:", absensi.info)
        
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
        query = "INSERT INTO new_absen (nama, keterangan, nilai, tanggal, info) VALUES (%s, %s, %s, %s, %s);"
        data = (absensi.name, absensi.keterangan, absensi.nilai, absensi.tanggal, absensi.info)

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
