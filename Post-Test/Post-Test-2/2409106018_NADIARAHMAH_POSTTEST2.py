print ("BIODATA MAHASISWA")
namaLengkap = input("Masukkan Nama Lengkap Anda :")
namaPanggilan = input ("Masukkan Nama Panggilan Anda :")
nim = int(input("Masukkan NIM Anda :"))
prodi = input ("Masukkan Program Studi Anda :")
kelas = input ("Masukkan Kelas Anda :")
umur = int (input ("Masukkan Umur Anda :"))
tinggiBadan = float (input ("Masukkan Tinggi Badan Anda :"))
beratBadan = float (input ("Masukkan Berat Badan Anda :"))
tigaAngkaAkhir = nim % 1000
modulus = tigaAngkaAkhir % 6
print (f"Nama saya {namaLengkap}, biasa dipanggil {namaPanggilan} dengan NIM {nim}, Saya dari Program studi {prodi} kelas {kelas}. Saya berumur {umur}  tahun, tinggi badan saya {tinggiBadan} cm dan berat badan saya {beratBadan} Kg.")
print (f"Tiga angka NIM terakhir saya adalah {tigaAngkaAkhir} dimoduluskan dengan 6 sehingga modukusnya bernilai {modulus}")
