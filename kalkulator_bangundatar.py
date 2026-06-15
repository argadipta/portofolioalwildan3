#Function Persegi
def keliling_persegi (sisi):
    return 4 * sisi
def luas_persegi (sisi):
    return sisi * sisi

#Function Persegi Panjang 
def keliling_persegi_panjang (panjang, lebar):
    return 2 * (panjang + lebar)
def luas_persegi_panjang (panjang, lebar):
    return panjang * lebar

#Function Segitiga 
def keliling_segitiga (sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3
def luas_segitiga (alas, tinggi):
    return 0.5 * alas * tinggi

#Function Lingkaran
def keliling_lingkaran (radius):
    return 2 * 3.14 * radius
def luas_lingkaran (radius):
    return 3.14 * radius * radius

#Program utama
print("Kalkulator Bangun Datar")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")

option = int(input("Pilih Option Bangun Datar 1/2/3/4 = "))

if option == 1: #Menghitung Persegi
    sisi = float(input("Masukkan sisi persegi = "))
    print("Luas Persegi = ", luas_persegi(sisi))
    print("Keliling Persegi = ", keliling_persegi(sisi))
    
elif option == 2: #Menghitung Persegi Panjang
    panjang = float(input("Masukkan Panjang = "))
    lebar = float(input("Masukkan Lebar = "))
    print("Luas Persegi Panjang = ", luas_persegi_panjang(panjang, lebar))
    print("Keliling Persegi Panjang = ", keliling_persegi_panjang(panjang, lebar))
    
elif option == 3: #Menghitung Segitiga
    sisi1 = float(input("Masukkan sisi 1 = "))
    sisi2 = float(input("Masukkan sisi 2 = "))
    sisi3 = float(input("Masukkan sisi 3 = "))
    alas = float(input("Masukkan alas = "))
    tinggi = float(input("Masukkan tinggi = "))
    print("Luas Segitiga = ",luas_segitiga(alas, tinggi))
    print("Keliling Segitiga = ",keliling_segitiga(sisi1, sisi2, sisi3))
    
elif option == 4: #Menghitung Lingkaran
    radius = float(input("Masukkan radius = "))
    print("Luas Lingkaran = ", luas_lingkaran(radius))
    print("keliling Lingkaran = ", keliling_lingkaran(radius))
    
else:
    print("Pilihan Tidak Valid! Silakan Masukkan Ulang")