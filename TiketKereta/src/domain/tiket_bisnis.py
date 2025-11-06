# src/domain/tiket_bisnis.py
from .tiket_kereta import TiketKereta

class TiketBisnis(TiketKereta):
    """
    Kelas Bisnis: tambah snack fee per orang.
    """
    SNACK_FEE = 15000

    def hitung_total(self) -> float:
        return (self.harga_dasar + self.SNACK_FEE) * self.jumlah

    def deskripsi(self) -> str:
        per_orang = self.harga_dasar + self.SNACK_FEE
        return f"[BISNIS] {self.nama_kereta} - {self._format_rupiah(per_orang)}/orang + Snack"
