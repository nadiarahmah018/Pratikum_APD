#cara membuat list
# nama_mhs = ["celio", "afrizal", "farrel", "ghazali",]
# print(nama_mhs)

#list dengan tipe data berbeda
# tas = ["buku", 32, True, 3.14, ["IF", 24]]
# print(tas)

#memanggil indeks
# tas = ["buku", 32, True, 3.14, ["IF", 24]]
# print(tas[4])

#menambahkan elemen kedalam list
# matkul = ["kalkulus", "Fisika dasar", "Pengantar Teknologi Informasi"]
# print(matkul)
#menambahkan matkul logika informatika
# matkul.append("logika Informatika")
# print(matkul)

#menambahkan elemen baru ke indeks tertentu
# matkul = ["Kalkulus", "Fisika Dasar", "Pengantar Teknologi Informasi"]
# print(matkul)
#menambahkan elemen ke indek 1
# matkul.insert(1,"Logika Informatika")
# print(matkul)

#mengubah elemen list
# prodi = ["Informatika", "Sistem Informasi", "Arsitektur", "Teknik Lingkungan"]
# print(prodi)
# prodi[2]=("Teknik Arsitektur")
# print(prodi)

#menghapus elemen list
# prodi = ["informatika", "Sistem Informasi", "Arsitektur", "Teknik Lingkungan"]
# print(prodi)
# del prodi[2]
# print(prodi)

#pop 
# nama = ["celio", "sandi", "farrel","ghazali", "alvito", "yuyun", "andri", "rizal", "adi", "ifnu"]
# hapus = nama.pop(2)
# print(hapus)

#slicing
# print(nama[2:4])

#slicing (step)
# print(nama[1:9:2])

#slicing(memotong list)star,stop
# prodi = ["informatika", "Sistem Informasi", "Arsitektur", "Teknik Lingkungan", "Teknik Pertambangan", "Terknik Elektro","Teknik Industri","Teknik sipil""Teknik geologi","Teknik Kimia" ]
# print(prodi)
# print(prodi[0:6])

#slicing (star,stop,step)
# prodi = ["informatika", "Sistem Informasi", "Arsitektur", "Teknik Lingkungan", "Teknik Pertambangan", "Terknik Elektro","Teknik Industri","Teknik sipil", "Teknik geologi","Teknik Kimia" ] 
# print(prodi[::2],"\n")
# print(prodi[1:8:2])

#operasi list (+)
# bensin = ["avanza", "honda", "yamaha"]
# listrik = ["tesla", "SAIC"]
# semua = [bensin + listrik]
# print(semua)

# matkul = ["APD", "APL","BASDAT","STUKDAT",]

#operasi (*)
# bensin = ["avanza", "honda", "yamaha"]
# print(bensin*3)

# data =["farrel","celio",[1,2 ["halo", 23, 2.3,True]]]
# print(data[2][2][::-1])
# matkul = [1,2,3,4[5,6,7]]
# print(matkul[4][1::])

#perulangan
# matkul = [1,2,3,4,5,6,7,8,9]
# for i in matkul:
#     print (i, end='*')

#perulangan dalam nested list
matkul = [[1,2,3],[4,5,6,]]
for i in matkul:
    for j in i:
        print(j)
