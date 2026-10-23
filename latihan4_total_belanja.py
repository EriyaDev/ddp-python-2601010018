nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan: Rp. "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah_barang
ppn_11 = subtotal * 0.11
total_bayar = subtotal + ppn_11

print(f"Subtotal: {subtotal}")
print(f"PPN (11%): {ppn_11}")
print(f"Total Bayar: {total_bayar}")
