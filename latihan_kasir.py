# Function untuk menghitung diskon
def hitung_diskon(total):
    if total >= 100000:
        return 0.10
    elif total >= 50000:
        return 0.05
    else:
        return 0

# Function untuk menampilkan struk
def tampilkan_struk(daftar_belanja, total, diskon):
    print("\n===== STRUK PEMBELIAN =====")
    for item, harga, qty, subtotal in daftar_belanja:
        print(f"- {item} (x{qty}) : Rp{harga} => Subtotal: Rp{subtotal}")
    
    potongan = total * diskon
    total_bayar = total - potongan
    
    print(f"\nTotal Belanja : Rp{total}")
    print(f"Diskon ({diskon*100}%) : Rp{potongan}")
    print(f"Total Bayar   : Rp{total_bayar}")
    print("============================\n")

# Program utama
daftar_belanja = []
total = 0
print("=== Program Kasir Sederhana ===")

while True:
    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga satuan: "))
    qty = int(input("Masukkan jumlah barang: "))
    
    subtotal = harga * qty
    daftar_belanja.append((nama, harga, qty, subtotal))
    total += subtotal
    
    lanjut = input("Tambah barang? (yes/no): ").lower()
    if lanjut == "no":
        break

# Hitung diskon & tampilkan struk
diskon = hitung_diskon(total)
tampilkan_struk(daftar_belanja, total, diskon)