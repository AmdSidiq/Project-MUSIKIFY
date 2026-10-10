NAMA_FILE_DATA = "data_musik.txt"
NAMA_FILE_LAPORAN = "laporan_musik.txt"
HEADER_FILE = "judul|artis|genre|durasi|tahun"


# Mode 'x' - membuat file baru, tangani FileExistsError jika sudah ada
def inisialisasi_file(nama_file=NAMA_FILE_DATA):
    try:
        with open(nama_file, 'x') as file:
            file.write(HEADER_FILE + "\n")
        print(f"File '{nama_file}' berhasil dibuat!")
        return True
    except FileExistsError:
        return False 

# Mode 'a' - menambah data lagu baru di akhir file
def tambah_lagu(nama_file, baris_data):
    with open(nama_file, 'a') as file:
        file.write(baris_data + "\n")
    print(f"Lagu berhasil ditambahkan!")

# Mode 'r' - membaca semua data secara iteratif, tangani FileNotFoundError
def baca_semua_lagu(nama_file=NAMA_FILE_DATA):
    daftar_baris = []
    try:
        with open(nama_file, 'r') as file:
            for baris in file:  # pembacaan iteratif baris per baris
                baris_bersih = baris.strip()
                if baris_bersih and not baris_bersih.startswith("judul"):
                    daftar_baris.append(baris_bersih)
    except FileNotFoundError:
        print(f"File '{nama_file}' belum ada. Tambah lagu dulu.")
    return daftar_baris