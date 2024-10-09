biodata = {
    "NAMA": "nadia",
    "UMUR": 18,
    "NIM" : 2409106018,
    "JURUSAN" : "INFORMATIKA",
    "ANGKATAN" : 24
}
print(biodata)
print(biodata.get("JURUSAN"))
biodata.update({"UMUR": 19})
print(biodata)
del biodata ["ANGKATAN"]
print(biodata)

#create

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")