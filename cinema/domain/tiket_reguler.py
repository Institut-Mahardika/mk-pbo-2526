from .tiket import Tiket

class TiketReguler(Tiket):
  def __init__(self, judul_film: str, harga_dasar: float, kursi: str):
    super().__init__(judul_film, harga_dasar)
    self.kursi = kursi
  
  def hitung_total(self) -> float:
    return self.harga_dasar
  
  def __str__(self):
    return f"[REGULER] {self.judul_film} - Kursi: {self.kursi} - Rp. {self.hitung_total():,.0f}"