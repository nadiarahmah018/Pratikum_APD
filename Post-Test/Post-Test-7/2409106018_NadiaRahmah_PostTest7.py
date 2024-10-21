#PROGRAM MANAJEMEN RESERVASI ROOM KARAOKE
# data pengguna: {username: [password, peran]}
pengguna = {"adminkaraoke": ["nyanyiterus12", "admin"]}  # variable global
#data reservasi
reservasi_karaoke = {}  # variable global
reservasi_counter = 1   # variable global

#fungsi untuk menambahkan reservasi
def tambah_reservasi(tipe_user):  # fungsi dengan parameter
    print("\n =========== TAMBAH RESERVASI ===========")
    global reservasi_counter  # memanfaatkan variable global
    nama_tamu = input("Nama tamu: ")
    tanggal = input("Tanggal reservasi(DD-MM-YYYY): ")
    jam = input("Jam reservasi (HH.MM): ")
    durasi = input("Durasi karaoke(dalam jam): ")
    print(
    """
    ===============================
    |          MENU ROOM SIZE      |
    ===============================
    |        1. SMALL (4 ORANG)    |           
    |        2. MEDIUM (8 ORANG)   |          
    |        3. LARGE (10 ORANG)   |      
    ===============================
    """
    )
    room_size = int(input("Size room (1/2/3): "))
    
    # menentukan status reservasi
    status = "dipesan" if tipe_user == "pelanggan" else input("Status reservasi: ")

    reservasi_karaoke[reservasi_counter] = {  
        "nama_tamu": nama_tamu,
        "tanggal": tanggal,
        "jam": jam,
        "durasi": durasi,
        "room_size": room_size,
        "status": status
    }
    print(f"Reservasi berhasil ditambahkan untuk {nama_tamu}.")
    reservasi_counter += 1 

#fungsi rekursif
def rekursif_reservasi(idx, jumlah): 
    if idx > jumlah:
        return
    if idx in reservasi_karaoke:
        reservasi = reservasi_karaoke[idx]
        print(f"\nReservasi {idx}\n Nama tamu: {reservasi['nama_tamu']}\n Tanggal: {reservasi['tanggal']}\n Jam: {reservasi['jam']}\n Durasi: {reservasi['durasi']} jam\n Room size: {reservasi['room_size']}\n Status: {reservasi['status']}")
    rekursif_reservasi(idx + 1, jumlah)

#fungsi untuk lihat daftar reservasi
def lihat_reservasi():  # fungsi tanpa parameter
    print("\n =========== DAFTAR RESERVASI ===========")
    if len(reservasi_karaoke) <= 0:
        print("Belum ada reservasi.")
    else:
        rekursif_reservasi(1, reservasi_counter -1) #fungsi rekursif untuk tampilin daftar reservasi 

#fungsi untuk memperbarui status reservasi
def update_reservasi():
    print("\n =========== UPDATE RESERVASI ============")
    lihat_reservasi()
    idx = int(input("Pilih nomor reservasi yang ingin diperbarui: "))

    if idx in reservasi_karaoke:
        reservasi_karaoke[idx]['status'] = input("Status reservasi (dipesan/selesai/dibatalkan): ")
        print("Reservasi berhasil diperbarui.")
    else:
        print("Nomer reservasi tidak valid.")        

#fungsi untuk menghapus reservasi:
def hapus_reservasi():
    print("\n =========== HAPUS RESERVASI ============")
    lihat_reservasi()
    idx = int(input("Pilih nomor reservasi yang ingin dihapus: "))
    if idx in reservasi_karaoke:
        del reservasi_karaoke[idx]
        print(f"Reservasi nomer {idx} berhasil dihapus.")
    else:
        print("Nomer reservasi tidak ditemukan.")

def menu_admin():  # prosedur (tanpa parameter)
    while True:
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
            tambah_reservasi("admin")  # manggil fungsi dengan parameter

        elif pilihan_admin == 2:
            lihat_reservasi()  # manggil fungsi tanpa parameter

        elif pilihan_admin == 3:
            update_reservasi() # manggil fungsi tanpa parameter   

        elif pilihan_admin == 4:
            hapus_reservasi()  # manggil fungsi tanpa parameter

        elif pilihan_admin == 5:
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid.")
            

def menu_pelanggan():  # prosedur (tanpa parameter)
    while True:
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
        pilihan_user = int(input("PILIH MENU PELANGGAN(1/2/3): "))

        if pilihan_user == 1:
            tambah_reservasi("pelanggan")  # panggil fungsi dengan parameter

        elif pilihan_user == 2:
            lihat_reservasi()  # panggil fungsi tanpa parameter

        elif pilihan_user == 3:
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid.")
#fungsi utama
def utama():  #fungsi utama berada di bawah agar bisa memanggil fungsi yang udah didefinisikan sebelumnya
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
|    3. LOGOUT       |
======================
"""
        )
        pilihan = int(input("PILIH MENU(1/2/3): "))

        if pilihan == 1:
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            pengguna[username] = [password, "pelanggan"]
            print(f"Akun {username} berhasil didaftarkan. Silakan lanjut login.")

        elif pilihan == 2:
            username = input("USERNAME: ")
            password = input("PASSWORD: ")

            if username in pengguna and pengguna[username][0] == password:
                print(f"Login berhasil, Selamat datang {username}!")
                if username == "adminkaraoke":  # admin khusus
                    menu_admin()  # panggil prosedur menu admin
                else:
                    menu_pelanggan()  # panggil prosedur menu pelanggan
            else:
                print("Login gagal! Username atau password salah.")

        elif pilihan == 3:
            print("Terimakasih sudah menggunakan aplikasi ini.")
            break

        else:
            print("Pilihan tidak valid.")

utama()

