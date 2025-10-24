from .tiket import Tiket

class Pelanggan:
  def __init__(self, nama: str, saldo: float):
    self.nama = nama
    self.saldo = saldo
    self.daftar_tiket: list[Tiket] = []

  def pesan_tiket(self, tiket: Tiket) -> None:
    total = tiket.hitung_total()
    if total > self.saldo:
      print(f"GAGAL Saldo {self.nama} tidak cukup untuk {tiket.judul_film}")
      return
    self.saldo -= total
    self.daftar_tiket.append(tiket)
    print(f"SUKSES {self.nama} berhasil membeli {tiket.judul_film}")

  def tampilkan_info(self) -> None:
    print(f"\nPelanggan: {self.nama}")
    print(f"Saldo tersisa: Rp {self.saldo:,.0f}")
    if not self.daftar_tiket:
      print("Belum ada tiket.")
    else:
      print("Tiket yang dimiliki:")
      for t in self.daftar_tiket:
        print(f"  - {t}")
