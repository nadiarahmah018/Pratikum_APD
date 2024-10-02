# mahasiswa = (69, "informatika", "2209106044", "Aldy aeptian")
# absen, prodi, nim, nama = mahasiswa
# print(nim)

#CRUD
print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")

               