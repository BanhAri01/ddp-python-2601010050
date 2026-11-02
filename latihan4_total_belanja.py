PPN = 0.11

print("===== TOTAL BELANJA =====")
nama_barang = input("Nama barang  : ")
harga = float(input("Harga satuan : "))
jumlah = int(input("Jumlah       : "))

subtotal = harga * jumlah
ppn = subtotal * PPN
total = subtotal + ppn

print(f"\nBarang   : {nama_barang} x {jumlah}")
print(f"Subtotal : Rp{subtotal:,.0f}")
print(f"PPN 11%  : Rp{ppn:,.0f}")
print(f"Total    : Rp{total:,.0f}")
