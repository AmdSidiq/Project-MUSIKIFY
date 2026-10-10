# Validasi durasi lagu (detik), raise ValueError jika tidak valid
def validasi_durasi(durasi_str):
    try:
        durasi = int(durasi_str)
    except ValueError:
        raise ValueError(f"Durasi '{durasi_str}' bukan angka yang valid.")
    if durasi <= 0:
        raise ValueError(f"Durasi harus lebih dari 0 detik, diberikan: {durasi}")
    if durasi > 3600:
        raise ValueError(f"Durasi maks 3600 detik, diberikan: {durasi}")
    return durasi

# Validasi tahun rilis, raise ValueError jika di luar range
def validasi_tahun(tahun_str):
    try:
        tahun = int(tahun_str)
    except ValueError:
        raise ValueError(f"Tahun '{tahun_str}' bukan angka yang valid.")
    if tahun < 1900 or tahun > 2030:
        raise ValueError(f"Tahun harus 1900-2030, diberikan: {tahun}")
    return tahun

# Validasi teks tidak boleh kosong, raise ValueError jika kosong
def validasi_teks(teks, nama_field):
    if not teks or not teks.strip():
        raise ValueError(f"Field '{nama_field}' tidak boleh kosong!")
    return teks.strip()

# Parsing dan validasi satu baris data file (format: judul|artis|genre|durasi|tahun)
# Mengembalikan dict jika valid, None jika baris rusak (skip, tidak crash)
def validasi_baris_data(baris):
    try:
        baris = baris.strip()
        if not baris or baris.startswith("judul"):
            return None
        bagian = baris.split("|")
        if len(bagian) != 5:
            print(f"Baris dilewati (field tidak lengkap): {baris}")
            return None
        judul, artis, genre, durasi_str, tahun_str = bagian
        return {
            "judul": validasi_teks(judul, "judul"),
            "artis": validasi_teks(artis, "artis"),
            "genre": validasi_teks(genre, "genre"),
            "durasi": validasi_durasi(durasi_str.strip()),
            "tahun": validasi_tahun(tahun_str.strip())
        }
    except (ValueError, IndexError) as e:
        print(f"Baris dilewati ({e}): {baris}")
        return None

# Validasi pilihan menu, return -1 jika tidak valid
def validasi_pilihan_menu(pilihan_str):
    try:
        pilihan = int(pilihan_str)
        if pilihan < 0 or pilihan > 7:
            print(f"Pilihan tidak valid")
            return -1
        return pilihan
    except ValueError:
        print(f"Pilihan '{pilihan_str}' bukan angka valid.")
        return -1