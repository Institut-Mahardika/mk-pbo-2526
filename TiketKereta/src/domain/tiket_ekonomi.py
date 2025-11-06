# src/domain/tiket_ekonomi.py
from .tiket_kereta import TiketKereta

class TiketEkonomi(TiketKereta):
    """Kelas Ekonomi: harga_dasar per orang, tanpa biaya tambahan."""
    def hitung_total(self) -> float:
        return self.harga_dasar * self.jumlah

    def deskripsi(self) -> str:
        per_orang = self._format_rupiah(self.harga_dasar)
        return f"[EKONOMI] {self.nama_kereta} - {per_orang}/orang"
