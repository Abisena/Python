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
                
    def delete(self):
        choice = input("Apakah Anda ingin menghapus data? (y/n): ")
        if choice.lower() == 'y':
            name_to_delete = input("Masukkan nama yang ingin dihapus: ")
            rows_to_delete = int(input("Masukkan jumlah row yang ingin dihapus: "))
            count = 0
            delete_list = []
            for entry in self.data:
                if entry['nama'] == name_to_delete and count < rows_to_delete:
                    count += 1
                    delete_list.append(entry)
            if count > 0:
                print(f"{count} data dengan nama '{name_to_delete}' siap untuk dihapus.")
                confirm = input("Apakah Anda yakin ingin menghapus data tersebut di database? (y/n): ")
                if confirm.lower() == 'y':
                    # Perform deletion in the database
                    try:
                        connection = psycopg2.connect(
                            user="postgres",
                            password="admin12345",
                            host="localhost",
                            port="5432",
                            database="postgres"
                        )

                        cursor = connection.cursor()

                        # Get the primary key values of the rows to delete
                        ids_to_delete = [item['tanggal'] for item in delete_list]

                        delete_query = "DELETE FROM new_absen WHERE tanggal IN %s;"
                        cursor.execute(delete_query, (tuple(ids_to_delete),))

                        connection.commit()
                        print(f"{count} data berhasil dihapus dari database.")

                    except (Exception, psycopg2.Error) as error:
                        print("Error saat menghapus data:", error)

                    finally:
                        if connection:
                            cursor.close()
                            connection.close()
                            print("Koneksi ke database ditutup.")
                else:
                    print("Penghapusan data di database dibatalkan.")
                # Remove the deleted entries from self.data
                for item in delete_list:
                    self.data.remove(item)
            else:
                print(f"Tidak ada data dengan nama '{name_to_delete}' untuk dihapus.")



    def update(self):
        name_to_update = input("Masukkan nama yang ingin diupdate: ")
        field_to_update = input("Masukkan field yang ingin diupdate (nama/keterangan/nilai/tanggal): ")
        new_value = input(f"Masukkan nilai baru untuk field {field_to_update}: ")

        updated_data = []
        for entry in self.data:
            if entry['nama'] == name_to_update:
                entry[field_to_update] = new_value
            updated_data.append(entry)

        # Update self.data with the updated data
        self.data = updated_data

        print(f"Data dengan nama '{name_to_update}' berhasil diupdate pada field {field_to_update}.")

    # ... (previous code)

if __name__ == "__main__":
    csv_file_path = input("Masukkan path file CSV (kosongkan jika ingin input manual): ")
    absensi = Absen(csv_file_path)

    absensi.delete()
    absensi.update()

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