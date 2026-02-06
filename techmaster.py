from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0              
        self.__harga_dasar = harga_dasar  

   
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    @abstractmethod
    def tampilkan_detail(self, jumlah):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass
    
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        total = (self.get_harga_dasar() + pajak) * jumlah
        return pajak, total

    def tampilkan_detail(self, jumlah):
        pajak, subtotal = self.hitung_harga_total(jumlah)
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {int(pajak):,}")
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}")

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        total = (self.get_harga_dasar() + pajak) * jumlah
        return pajak, total

    def tampilkan_detail(self, jumlah):
        pajak, subtotal = self.hitung_harga_total(jumlah)
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {int(pajak):,}")
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}")

def proses_transaksi(daftar_barang):
    total_bayar = 0
    print("\n--- STRUK TRANSAKSI ---")

    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail(jumlah)
        _, subtotal = barang.hitung_harga_total(jumlah)
        total_bayar += subtotal

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total_bayar):,}")
    print("----------------------------------------")

print("--- SETUP DATA ---")
laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)
hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang)
