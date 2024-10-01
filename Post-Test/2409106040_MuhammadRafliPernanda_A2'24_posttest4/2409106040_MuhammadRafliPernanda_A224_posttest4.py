# Variabel Username dan Password
username = "pernanda"
password = 40
percobaanLogin = 0
pengulangan = 1

# Proses Login
print("Silahkan Login Dengan Username Nama Anda dan Password 3 Digit Terakhir NIM Anda")
nama = input("Masukkan Username Anda: ")
pW = int(input("Masukkan Password Anda: "))

#Pengulangan Jika Salah Input Username dan Password 
while not (nama == username and pW == password):
    percobaanLogin = percobaanLogin + 1
    if percobaanLogin == 3:
        nama = username
        pW = password
        pengulangan = 2
        print("Percobaan Login Maksimal 3x, Silahkan Coba Lagi Nanti")
    else:
        print("Username atau Password Anda Salah, Masukkan Username atau Password yang Benar")
        print("Silahkan Login Dengan Username Nama Anda dan Password 3 Digit Terakhir NIM Anda")
        nama = input("Masukkan Username Anda: ")
        pW = int(input("Masukkan Password Anda: "))

# Pengulangan Jika Login Berhasil
while pengulangan == 1:
    print("***Anda Berhasil Login, Silahkan Masukkan Data Anda***")
    namaLengkap = input("Masukkan Nama Lengkap Anda: ")
    NIM = int(input("Masukkan NIM Anda: "))
    totalPinjaman = int(input("Masukkan Jumlah Pinjaman Anda: "))
    lamaCicilan = int(input("Masukkan Lama Waktu Cicilan: "))
    totalBulan = lamaCicilan * 12
    if lamaCicilan == 1:
        bungaTahunan = 0.07
    elif lamaCicilan == 2:
        bungaTahunan = 0.13
    elif lamaCicilan == 3:
        bungaTahunan = 0.19
    else:
        print("Maaf Anda Tidak Memiliki Pinjaman dalam Rentang Waktu 1-3 tahun")
        pengulangan = 2
    if pengulangan == 1:
        bungaBulanan = bungaTahunan / 12 * totalPinjaman
        cicilanBulanan = (totalPinjaman + bungaBulanan) / totalBulan
        print(f"{namaLengkap} dengan NIM {NIM}, Bunga Perbulanmu adalah Rp.{bungaBulanan} dan Cicilan yang Harus Dibayar Perbulan Adalah Rp.{cicilanBulanan}")
    pengulangan = int(input("Apakah Anda Ingin Mengulang Program?" + " Ketik 1 Untuk Mengulang dan 2 Untuk Berhenti: "))
print("Program Berhenti")