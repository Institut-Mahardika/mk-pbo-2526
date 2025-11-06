# Contoh: Menulis data tiket ke file teks
with open("data_tiket.txt", "w") as file:
    file.write("Nama: Ahmad\n")
    file.write("Tujuan: Surabaya\n")
    file.write("Kelas: Bisnis\n")
    file.write("Harga: 400000\n")
print("Data tiket disimpan ke file data_tiket.txt")