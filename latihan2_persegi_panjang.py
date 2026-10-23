# Menerima input panjang dan lebar, dengan nilai berupa float(bisa menerima desimal berisi koma)
panjang = float(input("Masukkan nilai panjang (m): "))
lebar = float(input("Masukkan nilai lebar (m): "))

# hitung nilai luas dengan mengalikan panjang dan lebar
luas = panjang * lebar
# hitung nilai keliling dengan menjumlahkan panjang dan lebar lalu dikalikan 2
keliling = 2 * (panjang + lebar)

# menampilkan hasil perhitungan luas dan keliling
print(f"Luas : {luas} m2")
print(f"Keliling : {keliling} m")

# Trace Table:

# nilai awal panjang = 0, lebar = 0

# setelah input panjang = 8
# setelah input lebar = 5

# setelah menghitung luas = 8 * 5 = 40

# setelah menghitung keliling = 2 * (8 + 5) = 2 * 13 = 26

# output Luas = 40 m2
# output keliling = 26 m