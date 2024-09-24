# Input nama, NIM, total pinjaman dan lama cicilan
Nama = str(input("Siapa nama Anda? "))
NIM = int(input("Masukkan NIM Anda "))
totalPinjaman = int(input("Masukkan total pinjaman Anda = "))
lamaCicilan = int(input("Berapa lama waktu cicilan Anda = "))
totalBulan = lamaCicilan * 12

# Percabangan lama cicilan
if lamaCicilan == 1:
    bungaTahunan = 0.07
    bungaBulanan = bungaTahunan / 12 * totalPinjaman
    cicilanBulanan = (totalPinjaman + bungaBulanan) / totalBulan
    print("Bunga perbulan adalah =" , bungaBulanan)
    print(Nama , "dengan NIM" , NIM , "Total cicilan Perbulanmu Adalah =" , cicilanBulanan)
elif lamaCicilan == 2:
    bungaTahunan = 0.13
    bungaBulanan = bungaTahunan / 12 * totalPinjaman
    cicilanBulanan = (totalPinjaman + bungaBulanan) / totalBulan
    print("Bunga perbulan adalah =" , bungaBulanan)
    print(Nama , "dengan NIM" , NIM , "Total cicilan Perbulanmu Adalah =" , cicilanBulanan)
elif lamaCicilan == 3:
    bungaTahunan = 0.19
    bungaBulanan = bungaTahunan / 12 * totalPinjaman
    cicilanBulanan = (totalPinjaman + bungaBulanan) / totalBulan
    print("Bunga perbulan adalah =" , bungaBulanan)
    print(Nama , "dengan NIM" , NIM , "Total cicilan Perbulanmu Adalah =" , cicilanBulanan)
else:
    print("Maaf," , Nama , "dengan NIM" , NIM , "Anda tidak meminjam uang selama antara 1 sampai 3 tahun")