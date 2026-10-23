# Menerima input suhu celsius dari user
suhu_celsius = float(input("Masukkan suhu dalam Celcius (C): "))

# Menghitung suhu dalam Fahrenheit dengan rumus ( Celcius * 9/5 ) + 32
fahrenheit = float(suhu_celsius * 9 / 5) + 32
# Menghitung suhu dalam Kelvin dengan rumus Celcius + 273.15
kelvin = float(suhu_celsius + 273.15)

# Menampilkan hasil perhitungan farenheit dan kelvin
print(f"{fahrenheit} °F dan {kelvin} K")