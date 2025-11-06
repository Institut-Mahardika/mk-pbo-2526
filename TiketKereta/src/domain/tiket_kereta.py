# src/domain/tiket_kereta.py
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

class TiketKereta(ABC):
    """
    Abstraksi tiket kereta.
    Enkapsulasi: __harga_dasar, __kursi (private) + property dgn validasi.
    """
    def __init__(self, nama_kereta: str, tujuan: str, tanggal: str,
                 jumlah: int, harga_dasar: float, kursi: list[str]):
        self.nama_kereta = nama_kereta
        self.tujuan = tujuan
        self.tanggal = self._validasi_tanggal(tanggal)
        self.jumlah = self._validasi_jumlah(jumlah)
        self.__harga_dasar = None
        self.harga_dasar = harga_dasar    # via setter
        self.__kursi = None
        self.kursi = kursi                # via setter

    # ===== Encapsulation: harga_dasar =====
    @property
    def harga_dasar(self) -> float:
        return self.__harga_dasar

    @harga_dasar.setter
    def harga_dasar(self, value: float):
        if value is None or float(value) < 0:
            raise ValueError("Harga dasar tidak boleh negatif/kosong.")
        self.__harga_dasar = float(value)

    # ===== Encapsulation: kursi =====
    @property
    def kursi(self) -> list[str]:
        return self.__kursi

    @kursi.setter
    def kursi(self, value: list[str]):
        if not value or not all(isinstance(k, str) and k.strip() for k in value):
            raise ValueError("Kursi wajib diisi dan berupa list string non-kosong.")
        self.__kursi = value

    # ===== Validasi util =====
    @staticmethod
    def _validasi_jumlah(jml: int) -> int:
        jml = int(jml)
        if jml <= 0:
            raise ValueError("Jumlah tiket harus > 0.")
        return jml

    @staticmethod
    def _validasi_tanggal(s: str) -> str:
        # Terima format YYYY-MM-DD; jika gagal tetap simpan string apa adanya agar fleksibel
        try:
            datetime.strptime(s, "%Y-%m-%d")
        except Exception:
            pass
        return s

    # ===== Abstraksi / Polimorfisme =====
    @abstractmethod
    def hitung_total(self) -> float:
        """Mengembalikan total harga setelah biaya/komponen kelas."""
        ...

    @abstractmethod
    def deskripsi(self) -> str:
        """Deskripsi ringkas tiket (untuk demo polimorfisme)."""
        ...

    # Helper umum
    def _format_rupiah(self, n: float) -> str:
        return f"Rp {int(n):,}".replace(",", ".")
