class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

#method aktivitas
    def berjalan(self):
        print(self.nama, "sedang berjalan santai.")

    def berlari(self, kecepatan):
        print(self.nama, "sedang berlari dengan kecepatan", kecepatan, "km/jam.")

# 5 objek Manusia
orang1 = Manusia("Zemmel", 25, "Jl. Merdeka No. 10, Bangkalan")
orang2 = Manusia("Zidan", 30, "Jl. Sudirman No. 45, Bandung")
orang3 = Manusia("Adit", 22, "Jl. Gatot Subroto No. 8, Surabaya")
orang4 = Manusia("Jarwo", 28, "Jl. Pahlawan No. 15, Sumenep")
orang5 = Manusia("Siti", 35, "Jl. Diponegoro No. 23, Medan")

# Menggunakan method pada beberapa objek
orang1.berjalan()
orang2.berlari(5)
orang3.berjalan()
orang4.berlari(10)
orang5.berjalan()

print("")
print("Informasi orang1:", orang1.nama, orang1.umur, "tahun, alamat:", orang1.alamat)
print("Informasi orang2:", orang2.nama, orang2.umur, "tahun, alamat:", orang2.alamat)