class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur
        self.jenis = "Kucing"

    def mengeong(self):
        print(self.nama + " si " + self.warna + " sedang mengeong: Meong!")

    def bermain(self, mainan):
        print(self.nama + " sedang bermain dengan " + mainan)

    def info(self):
        print("{} {}, warna {}, umur {} tahun".format(self.jenis, self.nama, self.warna, self.umur))

class Burung:
    def __init__(self, nama, jenis, bisa_berbicara):
        self.nama = nama
        self.jenis = jenis
        self.bisa_berbicara = bisa_berbicara

    def berkicau(self):
        print(self.nama + " si " + self.jenis + " sedang berkicau: Cit..cit..cit!")

    def berbicara(self, kata):
        if self.bisa_berbicara:
            print(self.nama + " mengatakan: " + kata)
        else:
            print(self.nama + " tidak bisa berbicara")

    def info(self):
        kemampuan = "bisa" if self.bisa_berbicara else "tidak bisa"
        print("Burung {} bernama {} ({} berbicara)".format(self.jenis, self.nama, kemampuan))

class Ikan:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat

    def berenang(self):
        print(self.nama + " si " + self.jenis + " sedang berenang di " + self.habitat)

    def makan(self, makanan):
        print(self.nama + " sedang makan " + makanan)

    def info(self):
        print("Ikan {} bernama {}, hidup di {}".format(self.jenis, self.nama, self.habitat))

# Data objek-objek hewan
data_hewan = [
    {"type": "Kucing", "nama": "Milo", "warna": "oren", "umur": 2},
    {"type": "Kucing", "nama": "Luna", "warna": "putih", "umur": 1},
    {"type": "Burung", "nama": "Ciko", "jenis": "Lovebird", "bisa_berbicara": False},
    {"type": "Burung", "nama": "Polly", "jenis": "Kakatua", "bisa_berbicara": True},
    {"type": "Ikan", "nama": "Nemo", "jenis": "Clownfish", "habitat": "akuarium"},
    {"type": "Ikan", "nama": "Dory", "jenis": "Blue Tang", "habitat": "laut"}
]

# objek-objek yang menggunakan looping
hewan_list = []

for data in data_hewan:
    if data["type"] == "Kucing":
        hewan = Kucing(data["nama"], data["warna"], data["umur"])
    elif data["type"] == "Burung":
        hewan = Burung(data["nama"], data["jenis"], data["bisa_berbicara"])
    elif data["type"] == "Ikan":
        hewan = Ikan(data["nama"], data["jenis"], data["habitat"])

    hewan_list.append(hewan)
    hewan.info()
    
# Memanggil method sesuai jenis hewan
    if data["type"] == "Kucing":
        hewan.mengeong()
        hewan.bermain("benang")
    elif data["type"] == "Burung":
        hewan.berkicau()
        hewan.berbicara("Halo!")
    elif data["type"] == "Ikan":
        hewan.berenang()
        hewan.makan("pelet")

    print()

