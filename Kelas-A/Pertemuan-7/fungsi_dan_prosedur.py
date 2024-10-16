# # CARA MEMBUAT FUNGSI PADA PYTHON (prosedur) tidak menggunakan return
# def salam():
#     print ("Selamat datang mahasiswa baru 2024")
# def kali():
#     x = 6*4
#     print(x)
# # Pemanggilan Fungsi
# salam()
# kali()

# #FUNGSI DENGAN PARAMETER
# # Membuat fungsi dengan parameter (panjang, lebar)
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("Luas persegi panjang:", luas)
# # Pemanggilan fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 6)

# #FUNGSI PENGEMBALIAN NILAI
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # pemanggilan fungsi luas persegi
# print ("Luas persegi :", luas_persegi(8))

# #contoh pengembalian nilai(return)
# # rumus: sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
# # pemanggilan Fungsi
# luas_persegi(4)
# volume_persegi(6)


# #Variabel global dan lokal
# # membuat variabel global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()

# #PROGRAM MENGGUNAKAN FUNGSI
# # fungsi untuk menampilkan semua data
# buku =[]
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])

# #FUNGSI UNTUK MENAMBAH DATA
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)

# # fungsi untuk edit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru

# # fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
# menu = input("PILIH MENU: ")
# print ("\n")

# if menu == "1":
#     show_data()
# elif menu == "2":
#     insert_data()
# elif menu == "3":
#     edit_data()
# elif menu == "4":
#     delete_data()
# elif menu == "5":
#     exit() 
# else:
#     print ("Salah pilih!")

#library
import math
angka = 49
print(math.sqrt(angka))
