#Function Penjumlahan
def penjumlahan (angka1, angka2):
    return angka1 + angka2

#Function Pengurangan 
def pengurangan (angka1, angka2):
    return angka1 - angka2

#Function Perkalian
def perkalian (angka1, angka2):
    return angka1 * angka2

#Function Pembagian
def pembagian (angka1, angka2):
    if angka2 == 0:
        return ("Error! Tidak bisa dibagi 0")
    else:
        return angka1 / angka2
    
#Program Kalkulator
print("Kalkulator Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

option = int(input("Pilih Option 1/2/3/4 = "))

angka1 = float(input("Masukkan angka pertama = "))
angka2 = float(input("Masukkan angka kedua = "))

if option == 1:
    hasil = penjumlahan(angka1, angka2)
    print("Hasil = ", hasil)
    
elif option == 2:
    hasil = pengurangan(angka1, angka2)
    print("Hasil = ", hasil)
    
elif option == 3:
    hasil = perkalian(angka1, angka2)
    print("Hasil = ", hasil)
    
elif option == 4:
    hasil = pembagian(angka1, angka2)
    print("Hasil = ", hasil)
    
else:
    print("Option tidak valid!")