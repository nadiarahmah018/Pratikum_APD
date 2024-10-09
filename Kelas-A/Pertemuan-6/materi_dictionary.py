#dictionary(tipe data yg berfungsi menyimpan kumpulan data/nilai, bedanya sama list: kalau list terbatas cara ppemangggilannya)
#deklarasi dictionary
#contoh 1
# daftar_buku = {
#     "Buku1" : "Harry Potter", #ada komanya jika lebih dari 1 dictionary
#     "Buku2" : "Percy Jaction",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])
#contoh 2
# daftar_buku = {}

# daftar_buku["Buku1"] : "Harry Potter"
# daftar_buku["Buku2"] : "Percy Jaction"
# daftar_buku["Buku3"] : "Twillight"
# print(daftar_buku)


#sifat dictionary: unordered(tidakberurutan), changeeable(bisadiubah),unique(tidakmemilikikesamaan)
#contoh(maksudnya, jadinya outputnya yg keluar yg akhir krna sama)
# musik={
#     "judul" :"All Wee Know", #jgn lupa koma
#     "judul" :"Something Just Like This"
# }
# print(musik["judul"])

#membuat dictionary
#contoh satu item
# nama_dict = {
#     "key" : "value"
# }
#contoh multiple item
# nama_dict = {
#     "key1" : "value",
#     "key2" : "value",
#     "key3" : "value"
# }
#contoh 1
# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
#     }
# }
#contoh dengan konstruktor dict()
# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")
# print(games)

#mengakses item pada dictionary(kurung siku[ ] dan fungsi get())
#contoh []
# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"NIM Saya adalah {Biodata['NIM']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
#contoh get()
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key tersebut tidak ada"))

#perulangan pada python
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #tanpa menggunakan items
# for i in Nilai:
# print(i)
# print("")
#menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

#menambahkan item pada dictionary
#tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)

#mengubah item pada dictionary
# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# #Setelah diubah
# print(Film)

#menghapus item pada dictionary
#fungsi del.
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# #Setelah diubah
# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))

#contoh fungsi pop
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

#contoh fungsi clear
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# data.clear()
# #Setelah dihapus
# print(data)

#Mengetahui Panjang dari Dictionary
# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))

#Copy & Fromkeys
# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

#mengubah semua jadi satu
# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

#key and value
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i, end=" ")
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

#setdefault (menambahkan)
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

#list dan nastedlist pada dictionary
# Musik = {
#     "The Chainsmoker" : ["All we Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print(f"{key_a}: {value_a}")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# print(f"sebelum:{mahasiswa}")
# mahasiswa[101]["angkatan"]=2023
# print(f"sesudah:{mahasiswa}")

# #hapus umur
# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# print(f"sebelum:{mahasiswa}")
# del mahasiswa[101]["umur"]
# print(f"sesudah:{mahasiswa}")