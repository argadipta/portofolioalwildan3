def celcius_to_farenheit(celcius) :
    return (celcius * 9/5) + 32

def farenheit_to_celcius(farenheit) :
    return (farenheit - 32) * 5/9

def celcius_to_kelvin(celcius) :
    return celcius + 273.15

def kelvin_to_celcius(kelvin) :
    return kelvin - 273.15

def reamur_to_celcius(reamur) :
    return reamur * 5/4

def celcius_to_reamur(celcius) :
    return celcius * 4/5

def main():
    print ("Program Konversi Suhu")
    print ("Pilih suhu yang ingin dikonversi = ")
    print ("1. Celcius ke Farenheit")
    print ("2. Farenheit ke Celcius")
    print ("3. Celcius ke Kelvin")
    print ("4. Kelvin ke Celcius")
    print ("5. Reamur ke Celcius")
    print ("6. Celcius ke Reamur")
    
    pilihan = int(input("Masukkan Pilihan 1/2/3/4/5/6 = "))
    
    if pilihan in [1, 2, 3, 4, 5, 6]:
        try:
            suhu = float(input("Masukkan suhu = "))
        except ValueError:
            print ("Input tidak valid. Silakan masukkan angka")
            return
        
        if pilihan == 1 :
            hasil = celcius_to_farenheit(suhu)
            print (f"{suhu} Celcius = {hasil} Farenheit")
        elif pilihan == 2 :
            hasil = farenheit_to_celcius(suhu)
            print (f"{suhu} Farenheit = {hasil} Celcius")
        elif pilihan == 3 :
            hasil = celcius_to_kelvin(suhu)
            print (f"{suhu} Celcius = {hasil} Kelvin")
        elif pilihan == 4 :
            hasil = kelvin_to_celcius(suhu)
            print (f"{suhu} Kelvin = {hasil} Celcius")
        elif pilihan == 5 :
            hasil =reamur_to_celcius(suhu)
            print (f"{suhu} Reamur = {hasil} Celcius")
        elif pilihan == 6 :
            hasil =celcius_to_reamur(suhu)
            print (f"{suhu} Celcius = {hasil} Reamur")
    else:
        print("Pilihan tidak valid")
        
if __name__ == "__main__":
    main()