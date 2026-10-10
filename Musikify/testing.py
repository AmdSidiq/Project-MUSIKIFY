# ============================================================
# testing.py - Modul Pengujian Program (unittest)
# Berisi 1 class TestMusikify dengan minimal 5 fungsi pengujian
# ============================================================

import unittest
from musikify.processing import Lagu, KoleksiMusik
from musikify.validasi import validasi_durasi, validasi_tahun, validasi_teks


class TestMusikify(unittest.TestCase):
    """Class pengujian utama untuk program Musikify."""

    def setUp(self):
        # Persiapan data sampel sebelum setiap test
        self.koleksi = KoleksiMusik()
        self.koleksi.buat_record_lagu(judul="Bohemian Rhapsody", artis="Queen",
                                      genre="Rock", durasi=354, tahun=1975)
        self.koleksi.buat_record_lagu(judul="Shape of You", artis="Ed Sheeran",
                                      genre="Pop", durasi=234, tahun=2017)
        self.koleksi.buat_record_lagu(judul="Blinding Lights", artis="The Weeknd",
                                      genre="Pop", durasi=200, tahun=2020)

    # Test 1: validasi durasi valid dan invalid
    def test_validasi_durasi(self):
        self.assertEqual(validasi_durasi("234"), 234)
        with self.assertRaises(ValueError):
            validasi_durasi("-10")
        with self.assertRaises(ValueError):
            validasi_durasi("abc")

    # Test 2: validasi tahun valid dan invalid
    def test_validasi_tahun(self):
        self.assertEqual(validasi_tahun("2020"), 2020)
        with self.assertRaises(ValueError):
            validasi_tahun("1800")

    # Test 3: validasi teks kosong harus raise ValueError
    def test_validasi_teks(self):
        self.assertEqual(validasi_teks("  Hello  ", "test"), "Hello")
        with self.assertRaises(ValueError):
            validasi_teks("", "judul")

    # Test 4: pembuatan objek Lagu dan konversi to_line / from_line
    def test_lagu_objek(self):
        lagu = Lagu("Test", "Artist", "Pop", 180, 2023)
        self.assertEqual(lagu.to_line(), "Test|Artist|Pop|180|2023")
        lagu2 = Lagu.from_line("Test|Artist|Pop|180|2023")
        self.assertIsNotNone(lagu2)
        self.assertEqual(lagu2.judul, "Test")

    # Test 5: rata-rata durasi harus benar
    def test_rata_rata_durasi(self):
        # (354 + 234 + 200) / 3 = 262.67
        rata2 = self.koleksi.rata_rata_durasi()
        self.assertAlmostEqual(rata2, 262.67, places=1)

    # Test 6: urutkan lagu berdasarkan durasi (lambda + sorted)
    def test_urutkan_lagu(self):
        terurut = self.koleksi.urutkan_lagu(berdasarkan="durasi")
        self.assertEqual(terurut[0].judul, "Blinding Lights")
        self.assertEqual(terurut[-1].judul, "Bohemian Rhapsody")

    # Test 7: filter by genre menggunakan lambda + filter()
    def test_filter_genre(self):
        pop = self.koleksi.filter_by_genre("Pop")
        self.assertEqual(len(pop), 2)
        rock = self.koleksi.filter_by_genre("Rock")
        self.assertEqual(len(rock), 1)

    # Test 8: tambah banyak lagu dengan *args
    def test_tambah_banyak_args(self):
        k = KoleksiMusik()
        l1 = Lagu("A", "B", "Pop", 100, 2020)
        l2 = Lagu("C", "D", "Rock", 200, 2021)
        self.assertEqual(k.tambah_banyak_lagu(l1, l2), 2)

    # Test 9: hitung total durasi + *args tambahan
    def test_total_durasi(self):
        self.assertEqual(self.koleksi.hitung_total_durasi(), 788)
        self.assertEqual(self.koleksi.hitung_total_durasi(100), 888)

    # Test 10: cari lagu berdasarkan keyword
    def test_cari_lagu(self):
        hasil = self.koleksi.cari_lagu("Queen")
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0].judul, "Bohemian Rhapsody")


# Blok pengujian - hanya jalan saat file dieksekusi langsung
if __name__ == '__main__':
    # Assert sederhana sebelum unit test
    assert Lagu is not None, "Class Lagu harus bisa diakses"
    assert KoleksiMusik is not None, "Class KoleksiMusik harus bisa diakses"
    assert validasi_durasi("100") == 100, "validasi_durasi harus benar"
    print("[OK] Assert passed\n")

    unittest.main(verbosity=2)
