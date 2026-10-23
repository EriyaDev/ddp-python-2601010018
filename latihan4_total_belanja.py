# Menerima input nama barang, harga satuan, dan jumlah barang
nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan: Rp. "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Menghitung subtotal dengan mengalikan harga satuan dengan jumlah barang
subtotal = harga_satuan * jumlah_barang

# Menghitung PPN 11% dengan mengalikan subtotal dengan 0.11
ppn_11 = subtotal * 0.11

# Menghitung total dengan menjumlahkan subtotal dan PPN 11%
total_bayar = subtotal + ppn_11

# Menampilkan hasil perhitungan subtotal, PPN 11%, dan total bayar
print(f"Subtotal: {subtotal}")
print(f"PPN (11%): {ppn_11}")
print(f"Total Bayar: {total_bayar}")
