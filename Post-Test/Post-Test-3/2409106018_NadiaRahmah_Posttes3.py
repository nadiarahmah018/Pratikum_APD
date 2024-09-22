print("pilih jenis kelamin:")
print("1. Pria")
print("2. Wanita")
pilihan_kelamin = int(input("Pilihan 1/2: "))

berat_gr = float(input("masukkan berat badan dalam satuan gram (gr):"))
tinggi_km  = float(input("masukkan tinggi badan dalam satuan kilometer (km):"))
umur = int(input("masukkan umur: "))

berat_kg = berat_gr / 1000
tinggi_cm = tinggi_km / 100000

if pilihan_kelamin == 1:
    bmr = (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * umur) + 5
elif pilihan_kelamin == 2:
    bmr = (10 * berat_kg) + (6.25 * tinggi_cm) - (5 * umur) - 161
else:
    print ("pilihan tidak valid")

print("level aktivitas harian :")
print("1. aktivitas minimal (jarang bergerak)")
print("2. aktivitas sedang (olahraga 1-3 kali seminggu)")
print("3. aktivitas tinggi (olahraga 3-7kali seminngu)")
pilihan_aktivitas = int(input("pilihan 1/2/3: "))

if pilihan_aktivitas == 1:
    aktivitas = 1.25
elif pilihan_aktivitas == 2:
    aktivitas = 1.36
elif pilihan_aktivitas == 3:
    aktivitas = 1.72
else :
    print ("pilihan aktivitas tidak valid")

tdee = bmr * aktivitas
print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {tdee} kalori ")
