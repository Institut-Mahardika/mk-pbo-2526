# src/main.py
from domain.tiket_ekonomi import TiketEkonomi
from domain.tiket_bisnis import TiketBisnis
from domain.tiket_eksekutif import TiketEksekutif
from domain.pelanggan import Pelanggan
from repo.tiket_repository import TiketRepository

# ====== Data master tiket (template) ======
DAFTAR_TIKET = [
    ("KA Bengawan", "Yogyakarta", 120_000, "Ekonomi"),
    ("KA Argo Lawu", "Solo",       400_000, "Bisnis"),
    ("KA Argo Bromo", "Surabaya",  600_000, "Eksekutif"),
]

# List pembelian akan di-load dari file (jika ada)
pembelian: list[dict] = TiketRepository.load_pembelian()


def format_rp(n: float) -> str:
    return f"Rp {int(n):,}".replace(",", ".")


def generate_kursi(jumlah: int) -> list[str]:
    # Sederhana: A1, A2, ...
    return [f"A{idx+1}" for idx in range(jumlah)]


def buat_objek_tiket(kelas: str, nama_kereta: str, tujuan: str,
                     tanggal: str, jumlah: int, harga_dasar: float):
    kursi = generate_kursi(jumlah)
    if kelas == "1" or kelas.lower() == "ekonomi":
        return TiketEkonomi(nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi)
    if kelas == "2" or kelas.lower() == "bisnis":
        return TiketBisnis(nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi)
    if kelas == "3" or kelas.lower() == "eksekutif":
        return TiketEksekutif(nama_kereta, tujuan, tanggal, jumlah, harga_dasar, kursi)
    raise ValueError("Kelas tidak dikenali.")


def pilih_template_tiket(kode: str):
    idx = int(kode) - 1
    if not (0 <= idx < len(DAFTAR_TIKET)):
        raise ValueError("Pilihan tidak valid.")
    return DAFTAR_TIKET[idx]


# ====== Menu ======
def menu_pesan_tiket():
    print("\n=== PESAN TIKET ===")
    nama = input("Nama Penumpang : ").strip()
    if not nama:
        print("Nama wajib diisi.")
        return

    try:
        usia_raw = input("Usia (opsional, boleh kosong): ").strip()
        usia = int(usia_raw) if usia_raw else None
    except ValueError:
        print("Usia harus angka atau kosong.")
        return

    pelajar = input("Apakah pelajar? (y/n): ").strip().lower() == "y"

    print("\nPilih Template Tiket:")
    for i, (nker, tuj, harga, kelas) in enumerate(DAFTAR_TIKET, start=1):
        print(f"[{i}] {kelas} - {nker} ke {tuj} ({format_rp(harga)}/org)")

    pilih = input("Masukkan pilihan [1-3]: ").strip()
    try:
        nker, tuj_default, harga_dasar, kelas_label = pilih_template_tiket(pilih)
    except Exception as e:
        print(e)
        return

    tujuan = input(f"Tujuan [{tuj_default}]: ").strip() or tuj_default
    tanggal = input("Tanggal (YYYY-MM-DD): ").strip() or "2025-01-01"

    try:
        jumlah = int(input("Jumlah Tiket : ").strip())
        if jumlah <= 0:
            raise ValueError
    except Exception:
        print("Jumlah tiket harus angka > 0.")
        return

    # Buat objek kelas sesuai label
    kelas_kode = {"Ekonomi": "1", "Bisnis": "2", "Eksekutif": "3"}[kelas_label]
    tiket = buat_objek_tiket(kelas_kode, nker, tujuan, tanggal, jumlah, harga_dasar)

    # Bonus diskon sederhana (opsional)
    diskon = 0.0
    if usia is not None and usia < 12:
        diskon = 0.2  # 20% anak
    elif pelajar:
        diskon = 0.1  # 10% pelajar

    total = tiket.hitung_total()
    if diskon:
        total = total * (1 - diskon)

    pelanggan = Pelanggan(nama=nama, usia=usia, is_pelajar=pelajar)

    item = {
        "pelanggan": pelanggan,
        "tiket": tiket,
        "total": total,
        "diskon": diskon,
    }
    pembelian.append(item)
    # === SIMPAN KE FILE JSON lewat repository ===
    TiketRepository.save_pembelian(pembelian)

    print("\n=== TRANSAKSI BERHASIL ===")
    print(f"Nama Penumpang : {pelanggan.nama}")
    print(f"Tujuan         : {tiket.tujuan}")
    print(f"Kelas Kereta   : {tiket.__class__.__name__.replace('Tiket','')}")
    print(f"Jumlah Tiket   : {tiket.jumlah}  Kursi: {', '.join(tiket.kursi)}")
    if diskon:
        print(f"Diskon         : {int(diskon*100)}%")
    print(f"Total Harga    : {format_rp(total)}")

    # Cetak Tiket ke file teks (seperti versi awal Mas)
    with open("cetak_tiket.txt", "a", encoding="utf-8") as file:
        file.write(f"\n=== DETAIL TIKET KERETA API ===\n")
        file.write(f"Nama Penumpang: {pelanggan.nama}\n")
        file.write(f"Tujuan        : {tiket.tujuan}\n")
        file.write(f"Kelas Kereta  : {tiket.__class__.__name__.replace('Tiket','')}\n")
        file.write(f"Jumlah Tiket  : {tiket.jumlah}\n")
        file.write(f"Kursi         : {', '.join(tiket.kursi)}\n")
        if diskon:
            file.write(f"Diskon        : {int(diskon*100)}%\n")
        file.write(f"Total Harga   : {format_rp(total)}\n")
        file.write(f"=============================\n\n")
    print("Data tiket disimpan ke file cetak_tiket.txt")
    print("Terima kasih telah membeli tiket!\n")


def menu_daftar_tiket():
    print("\n=== DAFTAR TIKET (Polimorfisme) ===")
    contoh_objs = [
        TiketEkonomi("KA Bengawan", "Yogyakarta", "2025-01-01", 1, 120_000, ["A1"]),
        TiketBisnis("KA Argo Lawu", "Solo", "2025-01-01", 1, 400_000, ["B1"]),
        TiketEksekutif("KA Argo Bromo", "Surabaya", "2025-01-01", 1, 600_000, ["C1"]),
    ]
    for t in contoh_objs:
        print(t.deskripsi())
    print()

def menu_ubah_pembelian():
    print("\n=== UBAH PEMBELIAN ===")
    if not pembelian:
        print("Belum ada pembelian.\n")
        return

    # tampilkan dulu ringkasan
    menu_ringkasan()
    try:
        idx = int(input("Pilih nomor pembelian yang akan diubah: ").strip()) - 1
    except ValueError:
        print("Input harus angka.\n")
        return

    if not (0 <= idx < len(pembelian)):
        print("Nomor tidak valid.\n")
        return

    item = pembelian[idx]
    p = item["pelanggan"]
    t = item["tiket"]

    print("Biarkan kosong jika tidak ingin mengubah.")
    nama_baru = input(f"Nama ({p.nama}) : ").strip() or p.nama
    tujuan_baru = input(f"Tujuan ({t.tujuan}) : ").strip() or t.tujuan
    tanggal_baru = input(f"Tanggal ({t.tanggal}) : ").strip() or t.tanggal

    jumlah_input = input(f"Jumlah ({t.jumlah}) : ").strip()
    jumlah_baru = t.jumlah if not jumlah_input else int(jumlah_input)

    # update objek
    p.nama = nama_baru
    t.tujuan = tujuan_baru
    t.tanggal = tanggal_baru
    t.jumlah = jumlah_baru

    # hitung ulang total
    total_baru = t.hitung_total()
    diskon = item["diskon"]
    if diskon:
        total_baru *= (1 - diskon)
    item["total"] = total_baru

    # simpan ke file
    TiketRepository.save_pembelian(pembelian)
    print("✅ Pembelian berhasil diubah.\n")


def menu_hapus_pembelian():
    print("\n=== HAPUS PEMBELIAN ===")
    if not pembelian:
        print("Belum ada pembelian.\n")
        return

    menu_ringkasan()
    try:
        idx = int(input("Pilih nomor pembelian yang akan dihapus: ").strip()) - 1
    except ValueError:
        print("Input harus angka.\n")
        return

    if not (0 <= idx < len(pembelian)):
        print("Nomor tidak valid.\n")
        return

    konfirmasi = input("Yakin ingin menghapus? (y/n): ").strip().lower()
    if konfirmasi != "y":
        print("Dibatalkan.\n")
        return

    pembelian.pop(idx)
    TiketRepository.save_pembelian(pembelian)
    print("🗑️ Pembelian berhasil dihapus.\n")


def menu_ringkasan():
    print("\n=== RINGKASAN PEMBELIAN ===")
    if not pembelian:
        print("Belum ada pembelian.\n")
        return

    grand_total = 0
    for i, item in enumerate(pembelian, start=1):
        p = item["pelanggan"]
        t = item["tiket"]
        total = item["total"]
        diskon = item["diskon"]
        print(f"{i}. {p.nama} - {t.__class__.__name__.replace('Tiket','')} {t.nama_kereta} ke {t.tujuan}")
        print(f"   Tgl {t.tanggal} | {t.jumlah} tiket | Kursi: {', '.join(t.kursi)}")
        if diskon:
            print(f"   Diskon: {int(diskon*100)}%")
        print(f"   Total: {format_rp(total)}\n")
        grand_total += total
    print(f"Grand Total: {format_rp(grand_total)}\n")


def menu_cetak_tiket():
    """
    Opsional: lihat isi file cetak_tiket.txt dari menu.
    """
    print("\n=== CETAK TIKET (LIHAT FILE) ===")
    try:
        with open("cetak_tiket.txt", "r", encoding="utf-8") as f:
            isi = f.read()
        if not isi.strip():
            print("File cetak_tiket.txt masih kosong.\n")
        else:
            print(isi)
    except FileNotFoundError:
        print("File cetak_tiket.txt belum ada.\n")

def main():
    while True:
        print("=== SISTEM TIKET KERETA API ===")
        print("[1] Pesan Tiket")
        print("[2] Lihat Daftar Tiket (Demo Polimorfisme)")
        print("[3] Lihat Ringkasan Pembelian")
        print("[4] Lihat File Cetak Tiket")
        print("[5] Ubah Pembelian")
        print("[6] Hapus Pembelian")
        print("[7] Keluar")
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            try:
                menu_pesan_tiket()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}\n")
        elif pilih == "2":
            menu_daftar_tiket()
        elif pilih == "3":
            menu_ringkasan()
        elif pilih == "4":
            menu_cetak_tiket()
        elif pilih == "5":
            menu_ubah_pembelian()
        elif pilih == "6":
            menu_hapus_pembelian()
        elif pilih == "7":
            print("Sampai jumpa!")
            break
        else:
            print("Menu tidak dikenal.\n")


if __name__ == "__main__":
    main()
