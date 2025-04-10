class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print("Informasi Mahasiswa:")
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Jurusan :", self.jurusan)
        print("Alamat  :", self.alamat)

# Fungsi input data mahasiswa
def input_mahasiswa():
    print("Masukkan data mahasiswa")
    nama = input("Nama    : ")
    nim = input("NIM     : ")
    jurusan = input("Jurusan : ")
    alamat = input("Alamat  : ")
    print("")
    return Mahasiswa(nama, nim, jurusan, alamat)

# 3 objek mahasiswa dari input pengguna
mahasiswas = []
for i in range(3):
    mahasiswa = input_mahasiswa()
    mahasiswas.append(mahasiswa)

# Menampilkan informasi semua mahasiswa
print("")
print("=== Daftar Mahasiswa ===")
for idx, mhs in enumerate(mahasiswas, 1):
    print("Mahasiswa", idx, ":")
    print("")
    mhs.tampilkan_info()