# UTS – Sistem Tiket Kereta Api
**Nama:** <NAMA ANDA>  
**NPM:** <NPM ANDA>

## Deskripsi
Aplikasi CLI untuk pemesanan tiket kereta dengan menu interaktif. Menerapkan 4 pilar OOP: Abstraksi, Pewarisan, Enkapsulasi, Polimorfisme.

## Struktur
```
src/
├─ domain/
│ ├─ tiket_kereta.py # ABC + property (enkapsulasi)
│ ├─ tiket_ekonomi.py # subclass 1 (override)
│ ├─ tiket_bisnis.py # subclass 2 (override)
│ ├─ tiket_eksekutif.py # subclass 3 (override)
│ └─ pelanggan.py # data class
└─ main.py # menu interaktif
```

## 4 Pilar OOP
- **Abstraksi:** `TiketKereta(ABC)` dengan `hitung_total()` & `deskripsi()` abstrak.  
- **Pewarisan:** `TiketEkonomi`, `TiketBisnis`, `TiketEksekutif` mewarisi `TiketKereta`.  
- **Enkapsulasi:** atribut privat `__harga_dasar`, `__kursi` + `@property` + validasi setter.  
- **Polimorfisme:** overriding method di tiap subclass; demo pada `menu_daftar_tiket()` yang mencetak `t.deskripsi()` dari list objek berbeda.

## Contoh Jalankan
```
python src/main.py
```

## Contoh Input/Output Singkat

=== SISTEM TIKET KERETA API ===
[1] Pesan Tiket
...
Nama Penumpang : Ahmad
Tujuan         : Surabaya
Kelas Kereta   : Bisnis
Jumlah Tiket   : 2
Total Harga    : Rp 830.000
