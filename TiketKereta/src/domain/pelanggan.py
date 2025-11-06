# src/domain/pelanggan.py
from dataclasses import dataclass

@dataclass
class Pelanggan:
    nama: str
    usia: int | None = None
    is_pelajar: bool = False
