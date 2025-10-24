from .tiket import Tiket

class TiketVIP(Tiket):
  def __init__(self, judul_film: str, harga_dasar: float, kursi: str, bonus_snack: str):
    super().__init__(judul_film, harga_dasar)
    self.kursi = kursi
    self.bonus_snack = bonus_snack

  def hitung_total(self) -> float:
    return self.harga_dasar * 1.25  # +25%

  def __str__(self) -> str:
    return f"[VIP] {self.judul_film} - Kursi {self.kursi} - Rp {self.hitung_total():,.0f} (Bonus: {self.bonus_snack})"
