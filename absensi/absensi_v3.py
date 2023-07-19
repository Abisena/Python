import csv
import psycopg2

class Absen():
    def __init__(self, csv_file=None):
        self.data = []  # List to store multiple rows of data
        if csv_file:
            with open(csv_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.data.append({
                        'nama': row.get('nama'),
                        'keterangan': row.get('keterangan'),
                        'nilai': int(row.get('nilai')),
                        'tanggal': row.get('tanggal'),
                        'info': None
                    })
                    

    def cek_nama(self):
        for entry in self.data:
            if not entry['nama'].strip():
                return "Nama tidak boleh kosong, silahkan isi terlebih dahulu."
        return "Silahkan lanjut isi keterangan :D"

    def data_nilai(self):
        for entry in self.data:
            if entry['nilai'] <= 75:
                entry['info'] = "Remedial"
            else:
                entry['info'] = "Alhamdulillah"
        return "Terima Kasih Sudah Mengisi :)"
    
    def cek_promosi_kelas(self):
        for entry in self.data:
            if entry['info'] == "Alhamdulillah":
                entry['info'] = "naik kelas."
            else:
                entry['info'] = "Maaf, Anda harus mengulang tahun depan."

if __name__ == "__main__":
    csv_file_path = input("Masukkan path file CSV (kosongkan jika ingin input manual): ")
    absensi = Absen(csv_file_path)

    while True:
        result = absensi.cek_nama()
        print(result)
        cek_result = absensi.data_nilai()
        print(cek_result)
        absensi.cek_promosi_kelas()
        print("Status Promosi Kelas:")
        for entry in absensi.data:
            print(entry['nama'], "-", entry['info'])

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

        for entry in absensi.data:
            data = (entry['nama'], entry['keterangan'], entry['nilai'], entry['tanggal'], entry['info'])
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
