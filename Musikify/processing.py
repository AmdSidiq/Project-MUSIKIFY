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