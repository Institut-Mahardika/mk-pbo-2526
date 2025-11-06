# src/domain/tiket_eksekutif.py
from .tiket_kereta import TiketKereta

class TiketEksekutif(TiketKereta):
    """
    Kelas Eksekutif: layanan premium fee flat per transaksi.
    """
    LAYANAN_FEE = 50000

    def hitung_total(self) -> float:
        return (self.harga_dasar * self.jumlah) + self.LAYANAN_FEE

    def deskripsi(self) -> str:
        return f"[EKSEKUTIF] {self.nama_kereta} - {self._format_rupiah(self.harga_dasar)}/orang + Layanan"
