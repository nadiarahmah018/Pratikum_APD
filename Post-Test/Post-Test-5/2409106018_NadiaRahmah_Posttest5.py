# data pengguna: [username, password, peran]
pengguna = [["adminkaraoke", "nyanyiterus12", "admin"]] #nasted list
# data reservasi: [nama_tamu, tanggal, jam, durasi,room_size, status] 
reservasi_karaoke = []

print("=== SELAMAT DATANG DI APLIKASI RESERVASI ROOM KARAOKE BERNADYA ==")
print("Silahkan register terlebih dahulu, jika belum punya akun.")

while True:
    print( 
"""
======================
|   MENU REGISTER    |
======================
|    1. REGISTER     |           
|    2. LOGIN        |                  
======================
"""
)
    pilihan = int(input("PILIH MENU(1/2/3): "))
    if pilihan == 1: #REGISTRASI (hanya untuk pelanggan)
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        peran = str(input("masukkan peran(pelanggan): "))
        if peran == "pelanggan" :
            pengguna.append([username, password, peran])
            print(f"Akun {username} berhasil didaftarkan. Silakan lanjut login")
        else:
            print("Peran tidak valid! Hanya pelanggan yang dapat registrasi.") #error handling (ketika input peran tidak tersedia)
    elif pilihan == 2: #LOGIN
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        peran = None #jika input username atau password salah, otomatis peran None(tidak ada)

        for user in pengguna:
            if user[0] == username and user[1] == password:
                print(f"Login berhasil, Selamat datang {username}!")
                peran = user[2]
                break
        if peran is None: 
            print("Login gagal! username atau password salah.") #error handling, ketika salah input username atau password 
            continue

        # menu admin
        while True:
            if peran == "admin":
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
                pilihan_admin = int(input("PILIH MENU(1/2/3/4/5): "))

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
                    reservasi_karaoke.append([nama_tamu, tanggal, jam, durasi, room_size,status]) #menambahkan elemen baru kedalam list yg sudah ada
                    print("Reservasi berhasil ditambahkan.")

                elif pilihan_admin == 2:
                    print("\n =========== DAFTAR RESERVASI ===========")
                    if not reservasi_karaoke :
                        print("Belum ada reservasi.")
                    else:
                        for idx, reservasi in enumerate (reservasi_karaoke):
                            print(f"reservasi {idx + 1}\n Nama tamu: {reservasi [0]}\n Tanggal:{reservasi[1]}\n jam : {reservasi[2]}\n Durasi :{reservasi[3]} jam\n room size: {reservasi[4]}\n Status: {reservasi[5]}")

                elif pilihan_admin == 3:
                    print("\n =========== UPDATE RESERVASI ============")
                    
                    idx = int(input("Pilih nomer reservasi yang ingin diperbarui: ")) - 1 # mengurangi dengan satu karena index phyton dimulai dari 0
                    if idx < 0 or idx >= len(reservasi_karaoke):
                        print("invalid!")
                        continue

                    for i in range(len(reservasi_karaoke)):
                        if i == idx:
                            reservasi_karaoke[i][5] = input("status reservasi(dipesan/selesai/dibatalkan): ")
                    
                    print("Reservasi berhasil diperbarui.")
                
                elif pilihan_admin == 4:
                    print("\n =========== HAPUS RESERVASI ============")
                    idx= int(input("Pilih nomer reservasi yang ingin di hapus: ")) - 1
                    if  0 < idx <=  len(reservasi_karaoke) :
                        print("invalid!")
                        continue
                    for i in range(len(reservasi_karaoke)):
                        if i == idx:
                            reservasi_karaoke.pop(idx)
                        print("Nomer reservasi berhasil dihapus.")
                    

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
                    status = input("Status reservasi: ")
                    reservasi_karaoke.append([nama_tamu, tanggal, jam, durasi, room_size,status])
                    print("Reservasi berhasil ditambahkan.")
                
                
                elif pilihan_user == 2:
                    
                    print("\n=========== DAFTAR RESERVASI ===========")
                    if not reservasi_karaoke:
                        print("Belum ada reservasi")
                    else:
                        for idx, reservasi in enumerate (reservasi_karaoke):
                            print(f"reservasi {idx + 1}\n Nama tamu: {reservasi [0]}\n Tanggal:{reservasi[1]}\n jam : {reservasi[2]}\n Durasi :{reservasi[3]} jam\n room size: {reservasi[4]}\n Status: {reservasi[5]}")

                elif pilihan_user == 3:
                    print("Terimakasih sudah melakukan reservasi di Karaoke Bernadya.")
                    break
                else:
                    print("Pilihan tidak valid.")
                    

  
    
