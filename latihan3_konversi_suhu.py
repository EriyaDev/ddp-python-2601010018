suhu_celsius = float(input("Masukkan suhu dalam Celcius (C): "))

fahrenheit = float(suhu_celsius * 9 / 5) + 32
kelvin = float(suhu_celsius + 273.15)

print(f"{fahrenheit} °F dan {kelvin} K")