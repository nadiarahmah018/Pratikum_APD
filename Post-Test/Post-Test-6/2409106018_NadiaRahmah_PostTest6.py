# data pengguna: {username: [password, peran]}
pengguna = {"adminkaraoke": ["nyanyiterus12", "admin"]} 
# data reservasi: [nama_tamu, tanggal, jam, durasi,room_size, status] 
reservasi_karaoke = {} #dictionary utama
reservasi_counter = 1

print("=== SELAMAT DATANG DI APLIKASI RESERVASI ROOM KARAOKE BERNADYA ===")
print("Silahkan register terlebih dahulu, jika belum punya akun.")

while True:
    print( 
"""
======================
|   MENU REGISTER    |
======================
|    1. REGISTER     |           
|    2. LOGIN        |
|    2. LOGOUT       |                  
======================
"""
    )
    pilihan = int(input("PILIH MENU(1/2/3): "))
    if pilihan == 1: #REGISTRASI (hanya untuk pelanggan)
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        peran = str(input("masukkan peran (pelanggan): "))
        if peran == "pelanggan" :
            pengguna[username] = [password, peran]
            print(f"Akun {username} berhasil didaftarkan. Silakan lanjut login")
        else:
            print("Peran tidak valid! Hanya pelanggan yang dapat registrasi.") #error handling (ketika input peran tidak tersedia)
    elif pilihan == 2: #LOGIN
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        peran = None #jika input username atau password salah, otomatis peran None(tidak ada)

        if username in pengguna and pengguna[username][0] == password:
            print(f"Login berhasil, Selamat datang {username}!")
            peran = pengguna[username][1]
        else:  
            print("Login gagal! username atau password salah.") #error handling, ketika salah input username atau password 
            continue

        
        while True:
            if peran == "admin": #menu admin
                print( 
                """
====================================
|       MENU ADMIN RESERVASI       |
====================================
|    1. TAMBAH RESERVASI           |           
|    2. LIHAT DAFTAR RESERVASI     |          
|    3. UPDATE STATUS RESERVASI    |     
|    4. HAPUS RESERVASI            |      
|    5. LOGOUT                     |  
====================================
"""
                )
                pilihan_admin = int(input("PILIH MENU ADMIN(1/2/3/4/5): "))

                if pilihan_admin == 1:
                    nama_tamu = input("Nama tamu: ")
                    tanggal = input("Tanggal reservasi(DD-MM-YYYY): ") #contoh 08-12-2024
                    jam = input("Jam reservasi (HH.MM): ")#contoh 12.00
                    durasi = input("Durasi karaoke(dalam jam): ")
                    print( 
                    """
====================================
|          MENU ROOM SIZE          |
====================================
|        1. SMALL (4 ORANG)        |           
|        2. MEDIUM (8 ORANG)       |          
|        3. LARGE (10 ORANG)       |      
====================================
"""
                    )
                    
                    room_size = input("Size room(1/2/3): ")
                    status = input("Status reservasi: ")
                    reservasi_karaoke[reservasi_counter] = { #nested dictionary
                        "nama_tamu" : nama_tamu,
                        "tanggal" : tanggal,
                        "jam" : jam, 
                        "durasi" : durasi,
                        "room_size" : room_size,
                        "status" : status
                    } 
                    print("Reservasi berhasil ditambahkan.")
                    reservasi_counter +=1

                elif pilihan_admin == 2:
                    print("\n =========== DAFTAR RESERVASI ===========")
                    if not reservasi_karaoke :
                        print("Belum ada reservasi.")
                    else:
                        for idx, reservasi in reservasi_karaoke.items():
                            print(f"Reservasi {idx}\n Nama tamu: {reservasi['nama_tamu']}\n Tanggal: {reservasi['tanggal']}\n Jam: {reservasi['jam']}\n Durasi: {reservasi['durasi']} jam\n Room size: {reservasi['room_size']}\n Status: {reservasi['status']}")

                elif pilihan_admin == 3:
                    print("\n =========== UPDATE RESERVASI ============")
                    idx = int(input("Pilih nomer reservasi yang ingin diperbarui: ")) 
                    if idx not in reservasi_karaoke:
                        print("invalid!")
                        continue
                    reservasi_karaoke[idx]['status'] = input("Status reservasi (dipesan/selesai/dibatalkan): ")
                    print("Reservasi berhasil diperbarui.")
                
                elif pilihan_admin == 4:
                    print("\n =========== HAPUS RESERVASI ============")
                    idx= int(input("Pilih nomer reservasi yang ingin di hapus: ")) 
                    if idx in reservasi_karaoke :
                        del reservasi_karaoke[idx]
                        print("Reservasi berhasil dihapus.")
                    else:
                        print("Invalid! Nomer reservasi tidak ditemukan.")

                elif pilihan_admin == 5:
                    break
            elif peran == "pelanggan":
                print( 
                    """
====================================
|          MENU PELANGGAN          |
====================================
|        1. PESAN RESERVASI        |
|        2. LIHAT DAFTAR RESERVASI |           
|        3. LOGOUT                 |          
====================================
"""
                )
                pilihan_user = int(input("PILIHAN MENU PELANGGAN: "))
                if pilihan_user == 1:
                    nama_tamu = input("Nama tamu: ")
                    tanggal = input("Tanggal reservasi(DD-MM-YYYY): ") #contoh 08-12-2024
                    jam = input("Jam reservasi (HH.MM): ")#contoh 12.00
                    durasi = input("Durasi karaoke(dalam jam): ")
                    print( 
                    """
====================================
|          MENU ROOM SIZE          |
====================================
|        1. SMALL (4 ORANG)        |           
|        2. MEDIUM (8 ORANG)       |          
|        3. LARGE (10 ORANG)       |      
====================================
"""
                    )
                    
                    room_size = input("Size room(1/2/3): ")
                    status = "dipesan"
                    reservasi_karaoke[reservasi_counter] = {
                        "nama_tamu" : nama_tamu,
                        "tanggal" : tanggal,
                        "jam" : jam, 
                        "durasi" : durasi,
                        "room_size" : room_size,
                        "status" : status
                    } 
                    print("Reservasi berhasil ditambahkan.")
                    reservasi_counter +=1
                
                
                elif pilihan_user == 2:
                    
                    print("\n=========== DAFTAR RESERVASI ===========")
                    if not reservasi_karaoke:
                        print("Belum ada reservasi")
                    else:
                        for idx, reservasi in reservasi_karaoke.items():
                            print(f"Reservasi {idx}\n Nama tamu: {reservasi['nama_tamu']}\n Tanggal: {reservasi['tanggal']}\n Jam: {reservasi['jam']}\n Durasi: {reservasi['durasi']} jam\n Room size: {reservasi['room_size']}\n Status: {reservasi['status']}")

                elif pilihan_user == 3:
                    print("Terimakasih sudah melakukan reservasi di Karaoke Bernadya.")
                    break
                else:
                    print("Pilihan tidak valid.")
    elif pilihan == 3:
        print("Terimakasih sudah melakukan reservasi di Karaoke Bernadya.")
        break                
    else:
        print("Pilihan tidak valid.")                

  
    
