from musikify.validasi import validasi_baris_data

class Lagu:
    """Class representasi sebuah lagu."""

    def __init__(self, judul, artis, genre, durasi, tahun):
        self.judul = judul
        self.artis = artis
        self.genre = genre
        self.durasi = durasi  # dalam detik
        self.tahun = tahun

    # Menampilkan info lagu dengan format menit:detik
    def info_lengkap(self):
        menit = self.durasi // 60
        detik = self.durasi % 60
        return f"{self.judul} - {self.artis} [{self.genre}] ({menit}:{detik:02d}) ({self.tahun})"

    # Konversi ke format baris file (pipe-separated)
    def to_line(self):
        return f"{self.judul}|{self.artis}|{self.genre}|{self.durasi}|{self.tahun}"

    # Class method: buat objek Lagu dari baris file
    @classmethod
    def from_line(cls, baris):
        data = validasi_baris_data(baris)
        if data:
            return cls(judul=data["judul"], artis=data["artis"],
                       genre=data["genre"], durasi=data["durasi"],
                       tahun=data["tahun"])
        return None

class KoleksiMusik:
    """Class untuk mengelola koleksi lagu."""

    def __init__(self):
        self.daftar_lagu = []

    # Menggunakan *args - tambah banyak lagu sekaligus
    def tambah_banyak_lagu(self, *lagu):
        jumlah = 0
        for item in lagu:
            if isinstance(item, Lagu):
                self.daftar_lagu.append(item)
                jumlah += 1
        return jumlah

    # Menggunakan **kwargs - buat record lagu dengan atribut fleksibel
    def buat_record_lagu(self, **kwargs):
        lagu_baru = Lagu(
            kwargs.get("judul", "Unknown"),
            kwargs.get("artis", "Unknown"),
            kwargs.get("genre", "Other"),
            kwargs.get("durasi", 0),
            kwargs.get("tahun", 2000)
        )
        self.daftar_lagu.append(lagu_baru)
        return lagu_baru

    # Menggunakan *args - hitung total durasi + durasi tambahan
    def hitung_total_durasi(self, *durasi_tambahan):
        total = sum(l.durasi for l in self.daftar_lagu)
        for d in durasi_tambahan:
            total += d
        return total

    # Hitung rata-rata durasi semua lagu
    def rata_rata_durasi(self):
        if not self.daftar_lagu:
            return 0
        return sum(l.durasi for l in self.daftar_lagu) / len(self.daftar_lagu)

    # Hitung jumlah lagu per genre, return dictionary
    def lagu_per_genre(self):
        genre_count = {}
        for lagu in self.daftar_lagu:
            genre_count[lagu.genre] = genre_count.get(lagu.genre, 0) + 1
        return genre_count

    # Cari lagu berdasarkan keyword (case-insensitive)
    def cari_lagu(self, keyword):
        kw = keyword.lower()
        return [l for l in self.daftar_lagu
                if kw in l.judul.lower() or kw in l.artis.lower()]

    # Menggunakan lambda sebagai key pada sorted()
    def urutkan_lagu(self, berdasarkan="judul"):
        key_map = {
            "judul": lambda l: l.judul.lower(),
            "artis": lambda l: l.artis.lower(),
            "durasi": lambda l: l.durasi,
            "tahun": lambda l: l.tahun,
            "genre": lambda l: l.genre.lower()
        }
        key_func = key_map.get(berdasarkan, key_map["judul"])
        return sorted(self.daftar_lagu, key=key_func)

    # Menggunakan lambda dengan filter() bawaan Python
    def filter_by_genre(self, genre):
        return list(filter(lambda l: l.genre.lower() == genre.lower(),
                           self.daftar_lagu))