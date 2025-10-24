from abc import ABC, abstractmethod

class Tiket(ABC):
  def __init__(self, judul_film: str, harga_dasar: float):
    self.judul_film = judul_film
    self.harga_dasar = harga_dasar
  
  @abstractmethod
  def hitung_total(self) -> float:
    pass
  
  def __str__(self):
    return f"{self.judul_film} - Rp. {self.hitung_total():,.0f}"