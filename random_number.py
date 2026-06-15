import random

#Function untuk memilih level
def pilih_level():
    print("\n Pilih Level: ")
    print("1. Mudah (1-10)")
    print("2. Sedang (1-20)")
    print("3. Sulit (1-50)")
    while True:
        level = input("Masukkan Level (1/2/3) : ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Input tidak valid! Coba lagi!")
            
#Function untuk menentukan range angka dan kesempatan
def set_level(level):
    if level == 1:
        return 10, 5 #range nya sampai 10 dengan 5x kesempatan
    elif level == 2:
        return 20, 4 #range nya sampai 20 dengan 4x kesempatan
    else:
        return 50, 3 #range nya sampai 50 dengan 3x kesempatan
    
#Function Game
def main_game():
    score = 100
    level = pilih_level()
    batas, kesempatan = set_level(level)
    angka_rahasia = random.randint(1, batas) #angka yg akan ditebak
    
    print(f"Tebak angka 1 sampai {batas}")
    print(f"Kesempatan: {kesempatan}")
    print(f"Score awal: {score}")
    
    for i in range(kesempatan):
        try:
            tebakan = int(input(f"Percobaan ke {i+1} : "))
            
            if tebakan < 1 or tebakan > batas:
                print("Angka diluar batas")
            elif tebakan == angka_rahasia:
                score += 20
                print("Tebakan Benar!")
                break
            elif tebakan < angka_rahasia:
                score -= 10
                print("Angka terlalu kecil")
            else:
                score -= 10
                print("Angka terlalu besar")
            print("Score sementara ", score)
            
        except ValueError:
            print("Harus Masukkan Angka!")
            score -= 10
            
    else:
        print("Kamu Kalah!")
        print("Angka rahasia adalah : ",angka_rahasia)
        print("Score akhir : ",score)
        
#Menjalankan programnya
while True:
    main_game()
    ulang = input("Ingin bermain lagi? (yes / no): ")
    if ulang.lower != "yes":
        print("Terima kasih sudah bermain!")
        break
    