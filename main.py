from domain.pelanggan import Pelanggan
from domain.tiket_reguler import TiketReguler
from domain.tiket_vip import TiketVIP

def menu():
  print("\n--- MENU PEMESANAN ---")
  print("1. Pesan Tiket Reguler")
  print("2. Pesan Tiket VIP")
  print("3. Lihat Daftar Tiket")
  print("4. Keluar")

def main():
  print("🎬=== SISTEM PEMESANAN TIKET BIOSKOP ===")
  nama = input("Masukkan nama pelanggan: ")
  saldo = float(input("Masukkan saldo awal: Rp "))
  pelanggan = Pelanggan(nama, saldo)

  while True:
    menu()
    pilihan = input("Pilih (1-4): ").strip()

    if pilihan == "1":
      judul = input("Judul film: ")
      harga = float(input("Harga dasar: Rp "))
      kursi = input("Nomor kursi: ")
      tiket = TiketReguler(judul, harga, kursi)
      pelanggan.pesan_tiket(tiket)

    elif pilihan == "2":
      judul = input("Judul film: ")
      harga = float(input("Harga dasar: Rp "))
      kursi = input("Nomor kursi: ")
      bonus = input("Bonus snack: ")
      tiket = TiketVIP(judul, harga, kursi, bonus)
      pelanggan.pesan_tiket(tiket)

    elif pilihan == "3":
      pelanggan.tampilkan_info()

    elif pilihan == "4":
      print("\nTerima kasih! Berikut ringkasan belanja:")
      pelanggan.tampilkan_info()
      break

    else:
      print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
  main()
