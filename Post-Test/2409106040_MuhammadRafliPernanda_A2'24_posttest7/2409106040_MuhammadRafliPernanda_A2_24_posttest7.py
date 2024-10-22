# Data pengguna dan pendaftaran
pengguna = {}
pendaftaran = {}
pengguna_login = None

# Fungsi untuk login 
def login():
    global pengguna_login
    if len(pengguna) == 0:
        print("Belum ada pengguna yang terdaftar. Silakan registrasi terlebih dahulu.")
        return False

    input_username = input("Masukkan nama pengguna: ")
    input_pw = input("Masukkan kata sandi: ")

    if input_username in pengguna and pengguna[input_username]["kata_sandi"] == input_pw:
        pengguna_login = pengguna[input_username]
        pengguna_login['username'] = input_username  # menyimpan username ke dalam dict
        print(f"Login Berhasil, Selamat datang {input_username}!")
        return True
    else:
        print("Nama pengguna atau kata sandi salah, silahkan coba lagi.")
        return False

# Pilih lomba dan kategori
def pilih_lomba_kategori():
    print(
        """
==================================
| Pilih Lomba yang Ingin Diikuti |
==================================
|        1. Kukar Fun Run        |
|        2. Mahakam Run          |
|        3. Yok Etam Lari        |
==================================
""")
    pilihan_lomba = input("Pilih Lomba (1-3): ")

    if pilihan_lomba == "1":
        lomba = "Kukar Fun Run"
    elif pilihan_lomba == "2":
        lomba = "Mahakam Run"
    elif pilihan_lomba == "3":
        lomba = "Yok Etam Lari"
    else:
        print("Pilihan lomba tidak valid.")
        return pilih_lomba_kategori()

    print(
        """
======================
|Pilih Kategori Lomba|
======================
|  1. 5km            |
|  2. 10km           |
|  3. Full Marathon  |
======================
""")
    pilihan_kategori = input("Pilih kategori (1-3): ")

    if pilihan_kategori == "1":
        kategori = "5km"
    elif pilihan_kategori == "2":
        kategori = "10km"
    elif pilihan_kategori == "3":
        kategori = "Full Marathon"
    else:
        print("Pilihan kategori tidak valid.")
        return pilih_lomba_kategori()

    return lomba, kategori

# Mengecek apakah pengguna sudah mendaftar lomba 
def cek_pendaftaran(username):
    global pendaftaran
    return username in pendaftaran

# Mengambil data lomba dan kategorinya
def data_lomba_kategori(username):
    if username in pendaftaran:
        data = pendaftaran[username]
        return f"{data['nama_peserta']} telah mendaftar lomba {data['lomba']} dengan kategori {data['kategori']}."
    else:
        return "Anda belum mendaftar lomba."

# Untuk melihat pendaftaran
def lihat_pendaftaran(username):
    if cek_pendaftaran(username):
        print(data_lomba_kategori(username))
    else:
        print("Anda belum mendaftar lomba.")

# Untuk membatalkan pendaftaran
def batalkan_pendaftaran(username):
    global pendaftaran

    if cek_pendaftaran(username):
        del pendaftaran[username]
        print("Pendaftaran berhasil dibatalkan.")
    else:
        print("Anda belum mendaftar lomba.")

# untuk mengedit pendaftaran
def edit_pendaftaran(username):
    global pendaftaran

    if cek_pendaftaran(username):
        nama_peserta = input("Masukkan nama peserta baru: ")
        lomba, kategori = pilih_lomba_kategori()
        pendaftaran[username] = {"nama_peserta": nama_peserta, "lomba": lomba, "kategori": kategori}
        print(f"Pendaftaran untuk peserta {nama_peserta} telah diperbarui menjadi lomba {lomba} dengan kategori {kategori}.")
    else:
        print("Anda belum mendaftar lomba.")

# Registrasi pengguna baru
def registrasi_pengguna():
    global pengguna
    print("=== Registrasi Pengguna Baru ===")
    nama_pengguna = input("Masukkan nama pengguna: ")
    kata_sandi = input("Masukkan kata sandi: ")

    # Memastikan input role hanya "admin" atau "pengguna"
    while True:
        role = input("Masukkan role (admin/pengguna): ")
        if role == "admin" or role == "pengguna":
            break
        else:
            print("Role tidak valid. Silakan masukkan 'admin' atau 'pengguna'.")

    if nama_pengguna in pengguna:
        print("Nama pengguna sudah terdaftar, silakan gunakan nama lain.")
    else:
        pengguna[nama_pengguna] = {"kata_sandi": kata_sandi, "role": role}
        print(f"Registrasi {role} dengan username {nama_pengguna} berhasil! Silahkan Login.")

# untuk mendaftar lomba marathon
def daftar_marathon(username):
    global pendaftaran
    if cek_pendaftaran(username):
        print("Anda hanya bisa mendaftar 1 lomba.")
    else:
        nama_peserta = input("Masukkan nama peserta: ")
        lomba, kategori = pilih_lomba_kategori()
        pendaftaran[username] = {"nama_peserta": nama_peserta, "lomba": lomba, "kategori": kategori}
        print(f"{pendaftaran[username]['nama_peserta']} telah mendaftar lomba {pendaftaran[username]['lomba']} dengan kategori {pendaftaran[username]['kategori']}.")
        
# Program utama
while True:
    print(
        """
===================================
|Program Pendaftaran Lari Marathon|
===================================
|          1. Registrasi          |
|          2. Login               |
|          3. Keluar              |
===================================
""")
    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        registrasi_pengguna()

    elif pilihan == "2":
        if login():
            if pengguna_login['role'] == "admin":
                while True:
                    print(
                        """
=============================
|        Menu Admin         |
=============================
| 1. Lihat Semua Pendaftaran|
| 2. Keluar                 |
=============================
""")
                    pilihan_admin = input("Pilih Menu: ")

                    if pilihan_admin == "1":
                        if len(pendaftaran) == 0:
                            print("Belum ada peserta yang mendaftar.")
                        else:
                            for username, data in pendaftaran.items():
                                print(f"Pengguna {username} telah mendaftar lomba {data['lomba']} dengan kategori {data['kategori']}.")
                    elif pilihan_admin == "2":
                        break
                    else:
                        print("Pilihan tidak valid.")

            else:
                while True:
                    print(
                        """
===========================
|      Menu Pengguna      |
===========================
| 1. Daftar Marathon      |
| 2. Lihat Pendaftaran    |
| 3. Edit Pendaftaran     |
| 4. Batalkan Pendaftaran |
| 5. Keluar               |
===========================
""")
                    pilihan_pengguna = input("Pilih Menu: ")

                    if pilihan_pengguna == "1":
                        daftar_marathon(pengguna_login['username'])

                    elif pilihan_pengguna == "2":
                        lihat_pendaftaran(pengguna_login['username'])

                    elif pilihan_pengguna == "3":
                        edit_pendaftaran(pengguna_login['username'])

                    elif pilihan_pengguna == "4":
                        batalkan_pendaftaran(pengguna_login['username'])

                    elif pilihan_pengguna == "5":
                        break
                    else:
                        print("Pilihan tidak valid")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid.")
