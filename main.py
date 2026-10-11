# ============================================================
# main.py - Program Utama Musikify
# Program manajemen koleksi musik berbasis CLI
# Mengimpor package musikify dan menjalankan menu interaktif
# ============================================================

from musikify import (inisialisasi_file, tambah_lagu, baca_semua_lagu,
                      tulis_laporan, Lagu, KoleksiMusik,
                      validasi_durasi, validasi_tahun, validasi_teks,
                      validasi_pilihan_menu,
                      NAMA_FILE_DATA, NAMA_FILE_LAPORAN)


# Menampilkan menu utama
def tampilkan_menu():
    print("\n========== MUSIKIFY ==========")
    print("  1. Tambah Lagu")
    print("  2. Lihat Semua Lagu")
    print("  3. Cari Lagu")
    print("  4. Urutkan Lagu")
    print("  5. Filter by Genre")
    print("  6. Statistik & Laporan")
    print("  7. Jalankan Unit Test")
    print("  0. Keluar")
    print("==============================")


# Memuat data lagu dari file ke KoleksiMusik
def muat_koleksi():
    koleksi = KoleksiMusik()
    daftar_baris = baca_semua_lagu(NAMA_FILE_DATA)
    if daftar_baris:
        jumlah = koleksi.muat_dari_baris(daftar_baris)
        print(f"  [{jumlah} lagu dimuat dari file]")
    return koleksi


# Menu 1: Tambah lagu baru (validasi + simpan ke file)
def menu_tambah_lagu():
    print("\n--- Tambah Lagu Baru ---")
    try:
        judul = validasi_teks(input("  Judul   : "), "judul")
        artis = validasi_teks(input("  Artis   : "), "artis")
        genre = validasi_teks(input("  Genre   : "), "genre")
        durasi = validasi_durasi(input("  Durasi (detik): "))
        tahun = validasi_tahun(input("  Tahun   : "))

        lagu = Lagu(judul, artis, genre, durasi, tahun)
        inisialisasi_file(NAMA_FILE_DATA)  # buat file jika belum ada (mode 'x')
        tambah_lagu(NAMA_FILE_DATA, lagu.to_line())  # simpan ke file (mode 'a')
        print(f"  -> {lagu.info_lengkap()}")
    except ValueError as e:
        print(f"  [!] Gagal: {e}")


# Menu 2: Lihat semua lagu
def menu_lihat(koleksi):
    print("\n--- Daftar Lagu ---")
    if not koleksi.daftar_lagu:
        print("  Koleksi kosong.")
        return
    for i, l in enumerate(koleksi.daftar_lagu, 1):
        print(f"  {i}. {l.info_lengkap()}")
    print(f"  Total: {len(koleksi.daftar_lagu)} lagu")


# Menu 3: Cari lagu berdasarkan keyword
def menu_cari(koleksi):
    print("\n--- Cari Lagu ---")
    if not koleksi.daftar_lagu:
        print("  Koleksi kosong.")
        return
    keyword = input("  Keyword (judul/artis): ").strip()
    if not keyword:
        print("  [!] Keyword kosong.")
        return
    hasil = koleksi.cari_lagu(keyword)
    if hasil:
        for i, l in enumerate(hasil, 1):
            print(f"  {i}. {l.info_lengkap()}")
    else:
        print(f"  Tidak ditemukan '{keyword}'.")


# Menu 4: Urutkan lagu (menggunakan keyword argument + lambda)
def menu_urutkan(koleksi):
    print("\n--- Urutkan Lagu ---")
    if not koleksi.daftar_lagu:
        print("  Koleksi kosong.")
        return
    print("  1.Judul  2.Artis  3.Durasi  4.Tahun  5.Genre")
    pilihan = input("  Pilihan: ")
    kriteria = {"1": "judul", "2": "artis", "3": "durasi",
            "4": "tahun", "5": "genre"}.get(pilihan, "judul")

    # Menggunakan keyword argument saat pemanggilan fungsi
    for i, l in enumerate(koleksi.urutkan_lagu(berdasarkan = kriteria), 1):
        print(f"  {i}. {l.info_lengkap()}")


# Menu 5: Filter lagu by genre (lambda + filter)
def menu_filter(koleksi):
    print("\n--- Filter by Genre ---")
    if not koleksi.daftar_lagu:
        print("  Koleksi kosong.")
        return
    # Tampilkan genre yang ada
    for genre, jumlah in sorted(koleksi.lagu_per_genre().items()):
        print(f"  - {genre} ({jumlah})")
    genre = input("  Genre: ").strip()
    if not genre:
        return
    hasil = koleksi.filter_by_genre(genre)
    if hasil:
        for i, l in enumerate(hasil, 1):
            print(f"  {i}. {l.info_lengkap()}")
    else:
        print(f"  Genre '{genre}' tidak ditemukan.")


# Menu 6: Statistik + generate laporan ke file
def menu_statistik_laporan(koleksi):
    print("\n--- Statistik & Laporan ---")
    if not koleksi.daftar_lagu:
        print("  Koleksi kosong.")
        return

    # Tampilkan statistik
    total = koleksi.hitung_total_durasi()
    rata2 = koleksi.rata_rata_durasi()
    print(f"  Total Lagu    : {len(koleksi.daftar_lagu)}")
    print(f"  Total Durasi  : {total // 60}m {total % 60}d")
    print(f"  Rata-rata     : {int(rata2) // 60}:{int(rata2) % 60:02d}")
    for genre, jumlah in sorted(koleksi.lagu_per_genre().items()):
        print(f"  {genre:<12}: {'#' * jumlah} ({jumlah})")

    # Generate dan tulis laporan ke file (mode 'w')
    laporan = koleksi.generate_laporan()
    tulis_laporan(NAMA_FILE_LAPORAN, laporan)


# Menu 7: Jalankan unit test
def menu_test():
    print("\n--- Jalankan Unit Test ---")
    import unittest
    from musikify.testing import TestMusikify
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMusikify)
    hasil = unittest.TextTestRunner(verbosity=2).run(suite)
    if hasil.wasSuccessful():
        print("\n  Semua test BERHASIL!")
    else:
        print(f"\n  {len(hasil.failures)} test GAGAL.")


# Fungsi utama - loop menu
def main():
    print("\n  Selamat datang di MUSIKIFY!")
    inisialisasi_file(NAMA_FILE_DATA)

    while True:
        koleksi = muat_koleksi()  # muat ulang dari file
        tampilkan_menu()
        pil = validasi_pilihan_menu(input("\n  Pilih (0-7): "))

        if pil == 0:
            print("\n  Terima kasih! Sampai jumpa.\n")
            break
        elif pil == 1:
            menu_tambah_lagu()
        elif pil == 2:
            menu_lihat(koleksi)
        elif pil == 3:
            menu_cari(koleksi)
        elif pil == 4:
            menu_urutkan(koleksi)
        elif pil == 5:
            menu_filter(koleksi)
        elif pil == 6:
            menu_statistik_laporan(koleksi)
        elif pil == 7:
            menu_test()
        else:
            continue

        input("\nTekan enter untuk lanjut")


if __name__ == '__main__':
    main()
