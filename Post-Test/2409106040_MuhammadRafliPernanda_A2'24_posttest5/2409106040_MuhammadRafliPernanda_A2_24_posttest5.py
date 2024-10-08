# Data pengguna dan pendaftaran
pengguna = []
pendaftaran = []
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
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # Registrasi Pengguna
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

        # Cek apakah nama pengguna sudah ada
        penggunaTerdaftar = False
        for data_pengguna in pengguna:
            if data_pengguna["nama_pengguna"] == nama_pengguna:
                penggunaTerdaftar = True
                break

        if penggunaTerdaftar:
            print("Nama pengguna sudah terdaftar, silakan gunakan nama lain.")
        else:
            pengguna.append({"nama_pengguna": nama_pengguna, "kata_sandi": kata_sandi, "role": role})
            print("Registrasi berhasil! Silakan login.")

    elif pilihan == "2":
        # Cek apakah ada pengguna terdaftar
        if len(pengguna) == 0:
            print("Belum ada pengguna yang terdaftar. Silakan registrasi terlebih dahulu.")
        else:
            # Login Pengguna
            nama_pengguna = input("Masukkan nama pengguna: ")
            kata_sandi = input("Masukkan kata sandi: ")

            # Verifikasi login
            pengguna_ditemukan = False
            for data_pengguna in pengguna:
                if data_pengguna["nama_pengguna"] == nama_pengguna and data_pengguna["kata_sandi"] == kata_sandi:
                    pengguna_login = data_pengguna
                    pengguna_ditemukan = True
                    break
            
            if not pengguna_ditemukan:
                print("Nama pengguna atau kata sandi salah.")
            else:
                # Menu Pengguna dan Admin
                if pengguna_login["role"] == "admin":
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
                        pilihan_admin = input("Pilih menu: ")

                        if pilihan_admin == "1":
                            if not pendaftaran:
                                print("Belum ada peserta yang mendaftar.")
                            else:
                                for data_pendaftaran in pendaftaran:
                                    print(f"{data_pendaftaran['nama']} telah mendaftar lomba {data_pendaftaran['lomba']} dengan kategori {data_pendaftaran['kategori']}.")
                        elif pilihan_admin == "2":
                            pengguna_login = None
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
                        pilihan_pengguna = input("Pilih menu: ")

                        if pilihan_pengguna == "1":
                            # Cek apakah pengguna sudah mendaftar
                            sudah_mendaftar = False
                            for data_pendaftaran in pendaftaran:
                                if data_pendaftaran["nama_pengguna"] == pengguna_login["nama_pengguna"]:
                                    sudah_mendaftar = True
                                    print("Anda hanya bisa mendaftar 1 lomba")
                                    break
                            
                            if not sudah_mendaftar:
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
                                pilihan_lomba = input("Pilih lomba (1-3): ")
                                
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

                                # Simpan pendaftaran
                                pendaftaran.append({
                                    "nama_pengguna": pengguna_login["nama_pengguna"],
                                    "nama": nama_peserta,
                                    "lomba": lomba,
                                    "kategori": kategori
                                })
                                print(f"{nama_peserta} telah mendaftar lomba {lomba} dengan kategori {kategori}.")
                        
                        elif pilihan_pengguna == "2":
                            pendaftaran_ditemukan = False
                            for data_pendaftaran in pendaftaran:
                                if data_pendaftaran["nama_pengguna"] == pengguna_login["nama_pengguna"]:
                                    print(f"{data_pendaftaran['nama']} telah mendaftar lomba {data_pendaftaran['lomba']} dengan kategori {data_pendaftaran['kategori']}.")
                                    pendaftaran_ditemukan = True
                                    break
                            
                            if not pendaftaran_ditemukan:
                                print(f"{pengguna_login['nama_pengguna']} belum melakukan pendaftaran.")
                        
                        elif pilihan_pengguna == "3":
                            # Edit pendaftaran
                            pendaftaran_ditemukan = False
                            for data_pendaftaran in pendaftaran:
                                if data_pendaftaran["nama_pengguna"] == pengguna_login["nama_pengguna"]:
                                    pendaftaran_ditemukan = True
                                    nama_baru = input("Masukkan nama baru peserta: ")
                                    print(
                                        """
=====================================
|Pilih lomba baru yang ingin diikuti|
=====================================
|          1. Kukar Fun Run         |
|          2. Mahakam Run           |
|          3. Yok Etam Lari         |   
=====================================
""")
                                    pilihan_lomba = input("Pilih lomba (1-3): ")

                                    if pilihan_lomba == "1":
                                        lomba = "Kukar Fun Run"
                                    elif pilihan_lomba == "2":
                                        lomba = "Mahakam Run"
                                    elif pilihan_lomba == "3":
                                        lomba = "Yok Etam Lari"
                                    else:
                                        print("Pilihan lomba tidak valid.")
                                        break

                                    print(
                                        """
========================================
|Pilih kategori baru yang ingin diikuti|
========================================
|             1. 5km                   |           
|             2. 10km                  |           
|             3. Full Marathon         |
========================================
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
                                        break

                                    data_pendaftaran["nama"] = nama_baru
                                    data_pendaftaran["lomba"] = lomba
                                    data_pendaftaran["kategori"] = kategori
                                    print(f"Pendaftaran berhasil diubah menjadi {nama_baru} di lomba {lomba} kategori {kategori}.")
                                    break

                            if not pendaftaran_ditemukan:
                                print(f"{pengguna_login['nama_pengguna']} belum melakukan pendaftaran.")
                        
                        elif pilihan_pengguna == "4":
                            # Batalkan pendaftaran
                            pendaftaran_ditemukan = False
                            for i, data_pendaftaran in enumerate(pendaftaran):
                                if data_pendaftaran["nama_pengguna"] == pengguna_login["nama_pengguna"]:
                                    del pendaftaran[i]
                                    print(f"{pengguna_login['nama_pengguna']} telah membatalkan pendaftarannya.")
                                    pendaftaran_ditemukan = True
                                    break
                            
                            if not pendaftaran_ditemukan:
                                print(f"{pengguna_login['nama_pengguna']} belum melakukan pendaftaran.")
                        
                        elif pilihan_pengguna == "5":
                            # Logout
                            pengguna_login = None
                            break

                        else:
                            print("Pilihan tidak valid.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid.")