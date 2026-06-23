menu = {
    "Soto Ayam " : 15000,
    "Soto Daging " : 20000,
    "Soto Lamongan " : 13000,
    "Soto Tauco " : 17000,
    "Nasi " : 5000
}

print ("Selamat datang di Kantin Soto")

nama_pelanggan = input("Masukkan nama pelanggan")

total_biaya = 0
uang_dibayarkan = 0

while True:
    print ("\n Menu:")
    for i, (item, harga) in enumerate(menu.items(), start=1):
        print(f"{i}. {item.capitalize()} Rp. {harga}")
        
    pilihan = input("\n Pilih menu dengan angka 1-5 atau ketik end untuk selesai")
    
    if pilihan == "end":
        break
    
    if pilihan.isdigit():
        index = int(pilihan) - 1
        
        if 0 <= index < len(menu):
            makanan = list(menu.keys())[index]
            harga = menu[makanan]
            jumlah = int(input(f"Masukkan jumlah {makanan()} yang ingin dipesan = "))
            total_harga = harga * jumlah
            total_biaya += total_harga
            print (f"Anda membeli {jumlah}{makanan()} dengan total biaya Rp.{total_harga}")
        else:
            print("Pilihan tidak valid! Silakan pilih menu kembali!")
    
    else:
        print("Input tidak Valid! Silakan pilih menu kembali!")
        
while True:
    try:
        uang_dibayarkan = float(input(f"Total biaya adalah Rp{total_biaya}. Masukkan uang anda = "))
        
        if uang_dibayarkan >= total_biaya:
            break
        else:
            print ("Uang anda kurang. Masukkan kembali uang anda")
    
    except ValueError:
        print("Masukkan angka yang valid untuk pembayaran")