# Data pengguna dan pendaftaran
pengguna = {}
pendaftaran = {}
pengguna_login = None

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

    # Tahap Registrasi
    if pilihan == "1":
        print("=== Registrasi Pengguna Baru ===")
        nama_pengguna = input("Masukkan nama pengguna: ")
        kata_sandi = input("Masukkan kata sandi: ")

        # Memastikan input role hanya "admin" atau "pengguna"
        while True:
            role = input("Masukkan role (admin/pengguna): ")
            if role == "admin" or role == "pengguna":
                break
            else:
                print("role tidak valid. Silakan masukkan 'admin' atau 'pengguna'.")

        # Pengecekan apakah username sudah terpakai
        penggunaTerdaftar = nama_pengguna in pengguna
        if penggunaTerdaftar:
            print("Nama pengguna sudah terdaftar, silakan gunakan nama lain.")
        # Registrasi Berhasil
        else:
            pengguna[nama_pengguna] = {"kata_sandi":kata_sandi, "role":role}
            print(f"Registrasi {role} dengan username {nama_pengguna} berhasil! Silahkan Login.")
        
    elif pilihan == "2":
        # Pengecekan apakah sudah ada pengguna yang terdaftar
        if len(pengguna) == 0:
            print("Belum ada pengguna yang terdaftar. Silakan registrasi terlebih dahulu.")
            continue
        else:
            # Input username dan password untuk Login
            pengguna_ditemukan = False  
            while not pengguna_ditemukan:
                inputUsername = input("Masukkan nama pengguna: ")
                inputPw = input("Masukkan kata sandi: ")

                # Proses verifikasi login
                if inputUsername in pengguna and pengguna[inputUsername]["kata_sandi"] == inputPw:
                    print(f"Login Berhasil, Selamat datang {inputUsername}!")
                    role = pengguna[inputUsername]["role"]
                    pengguna_login = pengguna[inputUsername]
                    pengguna_ditemukan = True  # Login berhasil, keluar dari loop
                else:
                    print("Nama pengguna atau kata sandi salah, silahkan coba lagi")
                    continue    # Mengulang proses input username dan password

        # Login Berhasil, Lanjut ke Program CRUD
        if pengguna_ditemukan:
            if role == "admin":
                #Menu utama admin
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

                    # Melihat Pendaftaran Pengguna 
                    if pilihan_admin == "1":
                        if len(pendaftaran) == 0:
                            print("Belum ada peserta yang mendaftar")
                        else:
                            for username, data_pendaftaran in pendaftaran.items():
                                print(f"Pengguna {username} telah mendaftar lomba {data_pendaftaran['lomba']} dengan kategori {data_pendaftaran['kategori']}")

                    
                    # Keluar dari Menu Admin
                    elif pilihan_admin == "2":
                        break      

                    else:
                        print("Pilihan tidak valid")

            else:
                # Menu Utama Pengguna
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

                    # Pendaftaran lomba 
                    if pilihan_pengguna == "1":
                        # Cek apakah pengguna sudah mendaftar
                        sudah_mendaftar = inputUsername in pendaftaran
                        if sudah_mendaftar:
                            print("Anda hanya bisa mendaftar 1 lomba")
                        else:
                             # Input data pendaftaran
                            nama_peserta = input("Masukkan nama peserta: ")
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
                                continue
                            
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
                                continue
                            
                            # Simpan Pendaftaran
                            pendaftaran[inputUsername] = {"nama_peserta": nama_peserta, "lomba": lomba, "kategori": kategori}
                            print(f"{pendaftaran[inputUsername]['nama_peserta']} telah mendaftar lomba {pendaftaran[inputUsername]['lomba']} dengan kategori {pendaftaran[inputUsername]['kategori']}.")


                    # Lihat Pendaftaran Lomba
                    elif pilihan_pengguna == "2":
                        # Cek apakah pengguna sudah mendaftar
                        sudah_mendaftar = inputUsername in pendaftaran
                        if inputUsername not in pendaftaran:
                            print(f"Anda belum melakukan pendaftaran.")
                        else:
                            print(f"{pendaftaran[inputUsername]['nama_peserta']} telah mendaftar lomba {pendaftaran[inputUsername]['lomba']} dengan kategori {pendaftaran[inputUsername]['kategori']}.")


                    # Mengedit Pendaftaran Lomba
                    elif pilihan_pengguna == "3":
                        if inputUsername in pendaftaran:
                            print("===Mengubah Pendaftaran===")
                            nama_peserta = input("Masukkan nama peserta baru: ")
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
                                continue

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
                                continue

                            # Update pendaftaran dengan data baru
                            pendaftaran[inputUsername] = {"nama_peserta": nama_peserta, "lomba": lomba, "kategori": kategori}
                            print(f"Pendaftaran untuk peserta {nama_peserta} telah diperbarui menjadi lomba {lomba} dengan kategori {kategori}.")
                        else:
                            print("Anda belum mendaftar lomba.")


                    # Batalkan Pendaftaran
                    elif pilihan_pengguna == "4":
                        if inputUsername in pendaftaran:
                            del pendaftaran[inputUsername]
                            print("Pendaftaran berhasil dibatalkan.")
                        else:
                            print("Anda belum mendaftar lomba.")


                    # Keluar dari Menu Pengguna
                    elif pilihan_pengguna == "5":
                        break

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid.")      