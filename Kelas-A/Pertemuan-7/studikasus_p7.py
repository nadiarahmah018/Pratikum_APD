#fungsi membuat luas segitiga (melalui input user)
def luas_segitiga ():
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas = 0.5 *alas*tinggi
    return luas
luas= luas_segitiga()
print(luas) 

# def persegi_panjang():
#     panjang = int(input("masukkan panjang: "))
#     lebar = int(input("masukkan lebar: "))
#     luas = panjang * lebar
#     return luas

# print(persegi_panjang())
