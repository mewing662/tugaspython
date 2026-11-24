#Studi kasus - Hukum Waris Sederhana
# Sebuah keluarga meninggalkan warisan sebesar 120.000,000

#Aturan hukum waris sederhana menggunakan pemograman pythom
#1. jika ahli waris adalah laki-laki, mendapat 2 bagian
#2. jika ahli waris adalah perempuan, mendapat 1 bagian
#3. programmenghitung bagian masing-masing ahli waris

print("===Program Pembagian Waris Sederhana===")
warisan = int(input("Masukkan Jumlah Harta Warisan : Rp"))
lk = int(input("Masukan Jumlah anak laki-laki : "))
pr = int(input("Masukan Jumlah anak perempuan: "))

#menghitung jumlah bagian 
bagian_lk = lk * 2
bagian_pr = pr * 1
total_bagian = bagian_lk + bagian_pr

#percabangan waris
if total_bagian > 0:
    nilai_bagian = warisan / total_bagian

    print("\n=== HASIL PEMBAGIAN")
if lk > 0:
    print("Setiap anak laki-laki mendapatkan Rp", int(nilai_bagian*2))


if pr > 0:
    print("Setiap anak perempuan mendapatkan Rp", int(nilai_bagian*1))

else:
    print("Tidak ada ahli waris")
    