# src/repo/tiket_repository.py
from __future__ import annotations
import json
import os
from typing import List, Dict, Any

from domain.pelanggan import Pelanggan
from domain.tiket_kereta import TiketKereta
from domain.tiket_ekonomi import TiketEkonomi
from domain.tiket_bisnis import TiketBisnis
from domain.tiket_eksekutif import TiketEksekutif


class TiketRepository:
    """
    Repository untuk menyimpan & memuat data pembelian tiket
    dalam bentuk JSON, tapi di sisi aplikasi tetap pakai objek:
      - Pelanggan
      - TiketKereta (TiketEkonomi/Bisnis/Eksekutif)
    """
    FILE_PATH = "data_pembelian.json"

    # ==========================
    # PUBLIC API
    # ==========================
    @staticmethod
    def load_pembelian() -> List[Dict[str, Any]]:
        """
        Mengembalikan list pembelian:
        [
          {
            "pelanggan": Pelanggan,
            "tiket": TiketKereta subclass,
            "total": float,
            "diskon": float
          },
          ...
        ]
        """
        if not os.path.exists(TiketRepository.FILE_PATH):
            return []

        with open(TiketRepository.FILE_PATH, "r", encoding="utf-8") as f:
            raw_list = json.load(f)

        result: List[Dict[str, Any]] = []
        for rec in raw_list:
            pelanggan = TiketRepository._dict_to_pelanggan(rec["pelanggan"])
            tiket = TiketRepository._dict_to_tiket(rec["tiket"])
            total = rec.get("total", 0.0)
            diskon = rec.get("diskon", 0.0)
            result.append(
                {
                    "pelanggan": pelanggan,
                    "tiket": tiket,
                    "total": total,
                    "diskon": diskon,
                }
            )
        return result

    @staticmethod
    def save_pembelian(pembelian: List[Dict[str, Any]]) -> None:
        """
        Menerima list pembelian (dengan objek),
        menyimpannya ke file JSON dalam bentuk dict biasa.
        """
        raw_list: List[Dict[str, Any]] = []

        for item in pembelian:
            pelanggan: Pelanggan = item["pelanggan"]
            tiket: TiketKereta = item["tiket"]
            total = item["total"]
            diskon = item.get("diskon", 0.0)

            raw_list.append(
                {
                    "pelanggan": TiketRepository._pelanggan_to_dict(pelanggan),
                    "tiket": TiketRepository._tiket_to_dict(tiket),
                    "total": total,
                    "diskon": diskon,
                }
            )

        with open(TiketRepository.FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(raw_list, f, indent=4, ensure_ascii=False)

    # Opsional: kalau mau langsung tambah satu pembelian
    @staticmethod
    def tambah_pembelian(item: Dict[str, Any]) -> None:
        data = TiketRepository.load_pembelian()
        data.append(item)
        TiketRepository.save_pembelian(data)

    @staticmethod
    def update_pembelian(index: int, item_baru: dict) -> bool:
        data = TiketRepository.load_pembelian()
        if 0 <= index < len(data):
            data[index] = item_baru
            TiketRepository.save_pembelian(data)
            return True
        return False

    @staticmethod
    def hapus_pembelian(index: int) -> bool:
        data = TiketRepository.load_pembelian()
        if 0 <= index < len(data):
            data.pop(index)
            TiketRepository.save_pembelian(data)
            return True
        return False
    
    # ==========================
    # HELPER: Pelanggan <-> dict
    # ==========================
    @staticmethod
    def _pelanggan_to_dict(p: Pelanggan) -> Dict[str, Any]:
        return {
            "nama": p.nama,
            "usia": p.usia,
            "is_pelajar": p.is_pelajar,
        }

    @staticmethod
    def _dict_to_pelanggan(d: Dict[str, Any]) -> Pelanggan:
        return Pelanggan(
            nama=d.get("nama", ""),
            usia=d.get("usia", None),
            is_pelajar=d.get("is_pelajar", False),
        )

    # ==========================
    # HELPER: Tiket <-> dict
    # ==========================
    @staticmethod
    def _tiket_to_dict(t: TiketKereta) -> Dict[str, Any]:
        """
        Simpan informasi cukup untuk bisa bikin ulang objek tiket.
        """
        return {
            "jenis_class": t.__class__.__name__,  # "TiketEkonomi", "TiketBisnis", ...
            "nama_kereta": t.nama_kereta,
            "tujuan": t.tujuan,
            "tanggal": t.tanggal,
            "jumlah": t.jumlah,
            "harga_dasar": t.harga_dasar,
            "kursi": t.kursi,
        }

    @staticmethod
    def _dict_to_tiket(d: Dict[str, Any]) -> TiketKereta:
        """
        Buat ulang objek tiket dari data dict.
        """
        jenis = d.get("jenis_class", "TiketEkonomi")
        cls_map = {
            "TiketEkonomi": TiketEkonomi,
            "TiketBisnis": TiketBisnis,
            "TiketEksekutif": TiketEksekutif,
        }
        cls = cls_map.get(jenis)
        if cls is None:
            # fallback kalau jenis tidak dikenal
            cls = TiketEkonomi

        return cls(
            d.get("nama_kereta", ""),
            d.get("tujuan", ""),
            d.get("tanggal", "2025-01-01"),
            d.get("jumlah", 1),
            d.get("harga_dasar", 0),
            d.get("kursi", ["A1"]),
        )
