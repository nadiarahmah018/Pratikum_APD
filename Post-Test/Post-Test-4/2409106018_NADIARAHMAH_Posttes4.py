print("PROGRAM KALKULATOR KEBUTUHAN KALORI HARIAN(TDEE)")
print("------------------------------------------------")
print(">>> Buat username dan password baru")
print("------------------------------------")
nama = (input("masukkan Nama panggilan: "))
nim = (input("masukkan NIM: "))
kode = (int(nim[7:]))
print(">>> Login Kalkulator Kebutuhan Kalori Harian (TDEE)")
print("--------------------------------------------------")
print(f"username baru: {nama} dan password baru:{kode}")
# percobaan maksimal 3 kali
# kesempatan login pertama
kesempatan = 0


while True:
    username = input("masukkan username:")
    password = int(input("masukakan password:"))

    if username == nama and password == kode:
        print("login berhasil!")
        print("\nKalkulator TDEE")
        print("pilih jenis kelamin:")
        print("1. Pria")
        print("2. Wanita")
        pilihan_kelamin = int(input("Pilihan 1/2: "))

        berat_gr = float(input("masukkan berat badan dalam satuan gram (gr):"))
        tinggi_km  = float(input("masukkan tinggi badan dalam satuan kilometer (km):"))
        umur = int(input("masukkan umur: "))

        berat_kg = berat_gr / 1000
        tinggi_cm = tinggi_km * 100000
        if pilihan_kelamin == 1:
            bmr= (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * umur) + 5
            print("level aktivitas harian :")
            print("1. aktivitas minimal (jarang bergerak)")
            print("2. aktivitas sedang (olahraga 1-3 kali seminggu)")
            print("3. aktivitas tinggi (olahraga 3-7kali seminngu)")
            pilihan_aktivitas = int(input("pilihan 1/2/3: "))
            if pilihan_aktivitas == 1:
                aktivitas = 1.25
                tdee =float( bmr * aktivitas)
                print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
                pilih = input ("apakah ingin menghitung lagi? (ya/tidak):")
                if pilih == "tidak":
                    print("program berhenti! terima kasih.")
                    print("-----------------------------------")
                    break
                elif pilih == "ya":
                    continue
                else:
                    print ("invalid")
                    exit()
            elif pilihan_aktivitas == 2:
                aktivitas = 1.36
                tdee =float( bmr * aktivitas)
                print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
                pilih = input ("apakah ingin menghitung lagi? (ya/tidak):")
                if pilih == "tidak":
                    print("program berhenti! terima kasih.")
                    print("-----------------------------------")
                    break
                elif pilih == "ya":
                    continue
                else:
                    print ("invalid")
                    exit()
            elif pilihan_aktivitas == 3:
                aktivitas = 1.72
                tdee =float( bmr * aktivitas)
                print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
                pilih = input ("apakah ingin menghitung lagi? (ya/tidak):")
                if pilih == "tidak":
                    print("program berhenti! terima kasih.")
                    print("-----------------------------------")
                    break
                elif pilih == "ya":
                    continue
                else:
                    print ("invalid")
                    exit()
            else :
                print ("pilihan aktivitas tidak valid")
                exit()
        elif pilihan_kelamin == 2:
            bmr = (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * umur) - 161
            print("level aktivitas harian :")
            print("1. aktivitas minimal (jarang bergerak)")
            print("2. aktivitas sedang (olahraga 1-3 kali seminggu)")
            print("3. aktivitas tinggi (olahraga 3-7kali seminngu)")
            pilihan_aktivitas = int(input("pilihan 1/2/3: "))

            if pilihan_aktivitas == 1:
                aktivitas = 1.25
                tdee =float( bmr * aktivitas)
                print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
                pilih = input ("apakah ingin menghitung lagi? (ya/tidak):")
                if pilih == "tidak":
                    print("program berhenti! terima kasih.")
                    print("-----------------------------------")
                    break
                elif pilih == "ya":
                    continue
                else:
                    print ("invalid")
                    exit()
            elif pilihan_aktivitas == 2:
                aktivitas = 1.36
                tdee =float( bmr * aktivitas)
                print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
                pilih = input ("apakah ingin menghitung lagi? (ya/tidak):")
                if pilih == "tidak":
                    print("program berhenti! terima kasih.")
                    print("-----------------------------------")
                    break
                elif pilih == "ya":
                    continue
                else:
                    print ("invalid")
                    exit()
            elif pilihan_aktivitas == 3:
                aktivitas = 1.72
                tdee =float( bmr * aktivitas)
                print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
                pilih = input ("apakah ingin menghitung lagi? (ya/tidak):")
                if pilih == "tidak":
                    print("program berhenti! terima kasih.")
                    print("-----------------------------------")
                    break
                elif pilih == "ya":
                    continue
                else:
                    print ("invalid")
                    exit()
            else :
                print ("pilihan aktivitas tidak valid")
                exit()
        else:
            print ("pilihan tidak valid")           
    else:   
        print ("login gagal!")
        kesempatan += 1
        if kesempatan == 3:
            print ("login gagal 3 kali! percobaan habis.")
            break
    