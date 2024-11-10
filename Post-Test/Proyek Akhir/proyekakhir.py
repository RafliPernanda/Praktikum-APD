# Data pengguna dan pendaftaran
pengguna = []  # Menggunakan list untuk menyimpan pengguna
pendaftaran = {}
pengguna_login = None

# Data admin menggunakan list
akunAdmin = [["admin", "admin"]]  # List berisi [username, password]

# Fungsi untuk login
def login():
    global pengguna_login
    print("Pilih jenis login:")
    print("1. Login sebagai Pengguna")
    print("2. Login sebagai Admin")
    pilihan_login = input("Pilih (1/2): ")

    if pilihan_login == "1":
        return login_pengguna()
    elif pilihan_login == "2":
        return login_admin()
    else:
        print("Pilihan tidak valid.")
        return False

def login_pengguna():
    global pengguna_login
    while True:
        if len(pengguna) == 0:
            print("Belum ada pengguna yang terdaftar. Silakan registrasi terlebih dahulu.")
            return False

        input_username = input("Masukkan nama pengguna: ")
        input_pw = input("Masukkan kata sandi: ")

        for user in pengguna:
            if user["username"] == input_username and user["kata_sandi"] == input_pw:
                pengguna_login = user
                print(f"Login Berhasil, Selamat datang {input_username}!")
                return True
        print("Nama pengguna atau kata sandi salah, silahkan coba lagi.")

def login_admin():
    global pengguna_login
    input_username = input("Masukkan username admin: ")
    input_pw = input("Masukkan kata sandi admin: ")

    for admin in akunAdmin:
        if admin[0] == input_username and admin[1] == input_pw:
            pengguna_login = {"username": admin[0], "role": "admin"}
            print(f"Login Berhasil, Selamat datang Admin!")
            return True
    print("Username atau kata sandi admin salah.")
    return False

# Pilih lomba dan kategori
def pilih_lomba_kategori():
    while True:
        print("""
        ==================================
        | Pilih Lomba yang Ingin Diikuti |
        ==================================
        | 1. Kukar Fun Run               |
        | 2. Mahakam Run                 |
        | 3. Yok Etam Lari               |
        ==================================
        """)
        
        pilihan_lomba = input("Pilih Lomba (1-3): ")
        
        if pilihan_lomba in ["1", "2", "3"]:
            lomba = ["Kukar Fun Run", "Mahakam Run", "Yok Etam Lari"][int(pilihan_lomba) - 1]
            break
        else:
            print("Pilihan lomba tidak valid.")

    while True:
        print("""
        ======================
        |Pilih Kategori Lomba|
        ======================
        | 1. 5km              |
        | 2. 10km             |
        | 3. Full Marathon     |
        ======================
        """)
        
        pilihan_kategori = input("Pilih kategori (1-3): ")
        
        if pilihan_kategori in ["1", "2", "3"]:
            kategori = ["5km", "10km", "Full Marathon"][int(pilihan_kategori) - 1]
            break
        else:
            print("Pilihan kategori tidak valid.")

    return lomba, kategori

# Program utama dan fungsi lainnya tetap sama...

# Mengecek apakah pengguna sudah mendaftar lomba 
def cek_pendaftaran(username):
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
        
        # Memperbarui data pendaftaran
        pendaftaran[username] = {"nama_peserta": nama_peserta, "lomba": lomba, "kategori": kategori}
        
        print(f"Pendaftaran untuk peserta {nama_peserta} telah diperbarui menjadi lomba {lomba} dengan kategori {kategori}.")
    else:
        print("Anda belum mendaftar lomba.")

# Registrasi pengguna baru
def registrasi_pengguna():
    global pengguna
    print("=== Registrasi Pengguna Baru ===")
    
    nama_pengguna = input("Masukkan nama pengguna: ")
    
    # Memastikan username unik
    for user in pengguna:
        if user["username"] == nama_pengguna:
            print("Nama pengguna sudah terdaftar, silakan gunakan nama lain.")
            return
    
    kata_sandi = input("Masukkan kata sandi: ")

    # Menambahkan pengguna baru ke dalam list
    pengguna.append({"username": nama_pengguna, "kata_sandi": kata_sandi, "role": "pengguna"})
    
    print(f"Registrasi pengguna dengan username {nama_pengguna} berhasil! Silahkan Login.")

# untuk mendaftar lomba marathon
def daftar_marathon(username):
    global pendaftaran
    if cek_pendaftaran(username):
        print("Anda hanya bisa mendaftar 1 lomba.")
    else:
        nama_peserta = input("Masukkan nama peserta: ")
        lomba, kategori = pilih_lomba_kategori()
        
        # Menyimpan data pendaftaran ke dalam dictionary berdasarkan username
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
|       Menu Admin          |
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

            else:  # Menu untuk pengguna biasa
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