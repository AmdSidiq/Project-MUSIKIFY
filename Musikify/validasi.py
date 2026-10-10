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