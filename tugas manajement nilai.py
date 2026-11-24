
# Program Tabel Data Nilai Siswa

data_siswa = []

# Fungsi untuk menambahkan keterangan nilai
def keterangan_nilai(nilai):
    if nilai >= 90:
        return "A (Sangat Baik)"
    elif nilai >= 80:
        return "B (Baik)"
    elif nilai >= 70:
        return "C (Cukup)"
    elif nilai >= 60:
        return "D (Kurang)"
    else:
        return "E (Tidak Lulus)"


# Fungsi untuk menambah data menggunakan while
def tambah_data():
    while True:
        nama = input("Masukkan nama siswa: ")
        nilai = float(input("Masukkan nilai siswa: "))

        if 0 <= nilai <= 100:
            data_siswa.append({
                "nama": nama,
                "nilai": nilai,
                "keterangan": keterangan_nilai(nilai)
            })
            print("Data berhasil ditambahkan!")
        else:
            print("Nilai harus antara 0 sampai 100!")

        lanjut = input("Tambah data lagi? (y/n): ")

        if lanjut.lower() != "y":
            break


# Fungsi menampilkan tabel data
def tampilkan_data():
    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        print("\n========== TABEL DATA NILAI SISWA ==========")
        print("{:<5} {:<20} {:<10} {:<20}".format(
            "No", "Nama", "Nilai", "Keterangan"))
        print("-" * 60)

        for i, siswa in enumerate(data_siswa, start=1):
            print("{:<5} {:<20} {:<10} {:<20}".format(
                i,
                siswa["nama"],
                siswa["nilai"],
                siswa["keterangan"]
            ))


# Fungsi menghitung nilai rata-rata menggunakan for
def rata_rata():
    if len(data_siswa) == 0:
        print("Data masih kosong.")
    else:
        total = 0

        for siswa in data_siswa:
            total += siswa["nilai"]

        rata = total / len(data_siswa)
        print("Nilai rata-rata siswa:", rata)


# Fungsi mencari nilai tertinggi menggunakan for
def nilai_tertinggi():
    if len(data_siswa) == 0:
        print("Data masih kosong.")
    else:
        tertinggi = data_siswa[0]

        for siswa in data_siswa:
            if siswa["nilai"] > tertinggi["nilai"]:
                tertinggi = siswa

        print("Nilai tertinggi:", tertinggi["nilai"])
        print("Nama siswa:", tertinggi["nama"])


# Fungsi utama menggunakan percabangan if/else
def main():
    while True:
        print("\n===== MENU DATA NILAI SISWA =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hitung Nilai Rata-rata")
        print("4. Cari Nilai Tertinggi")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            rata_rata()
        elif pilihan == "4":
            nilai_tertinggi()
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")


# Menjalankan program
main()
