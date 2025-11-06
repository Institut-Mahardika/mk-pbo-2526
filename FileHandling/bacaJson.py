import json

with open("data_tiket.json", "r") as file:
    data = json.load(file)

print(f"Nama: {data['nama']}")
print(f"Tujuan: {data['tujuan']}")
print(f"Kelas: {data['kelas']}")
print(f"Harga: Rp {data['harga']:,}")
