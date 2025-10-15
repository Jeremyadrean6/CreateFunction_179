def konversi_suhu(value, suhu):
    if suhu == "C":
        # Mengonversi dari Celsius ke Fahrenheit
        return (value * 9/5) + 32
    elif suhu == "F":
        # Mengonversi dari Fahrenheit ke Celsius
        return (value - 32) * 5/9
    else:
        raise ValueError("Satuan suhu tidak valid. Gunakan " \
        "'C' untuk Celsius atau 'F' untuk Fahrenheit.")
print(konversi_suhu(200, "C")) 
print(konversi_suhu(38, 'F'))


#2
luas_lingkaran = lambda jari_jari: 3.14 * (jari_jari ** 2)

n = float(input("Masukkan nilai jari-jari lingkaran: "))

print("Luas lingkaran dengan jari-jari", n, "adalah", luas_lingkaran(n))
.