import json

class TiketKereta:
    def __init__(self, nama, tujuan, kelas, harga):
        self.nama = nama
        self.tujuan = tujuan
        self.kelas = kelas
        self.harga = harga

    def to_dict(self):
        return {
            "nama": self.nama,
            "tujuan": self.tujuan,
            "kelas": self.kelas,
            "harga": self.harga
        }

# Simpan ke file JSON
tiket1 = TiketKereta("Ahmad", "Surabaya", "Bisnis", 400000)

with open("data_tiket.json", "w") as file:
    json.dump(tiket1.to_dict(), file, indent=2)

print("Data tiket disimpan ke file data_tiket.json")
