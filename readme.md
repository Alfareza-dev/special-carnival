# Laporan Praktikum OOP Python

Dokumen ini berisi ringkasan hasil latihan Object Oriented Programming (OOP) menggunakan Python, meliputi konsep Class, Object, Inheritance, Encapsulation, Abstraction, Interface, dan Polymorphism.

---

## Latihan 1 – Class & Object

Pada latihan ini dibuat class `Hero` dengan atribut dan method dasar.  
Percobaan mengubah nilai `hp` setelah object dibuat menunjukkan bahwa atribut object dapat diubah secara langsung.

Bukti:
![Latihan 1](./Laporan/Latihan%201.png)

---

## Latihan 2 – Interaksi Antar Object

Object dapat saling berinteraksi menggunakan method.  
Parameter `lawan` harus berupa object agar bisa mengakses atribut dan method milik object lain.

Bukti:
![Latihan 2](./Laporan/Latihan%202.png)

---

## Latihan 3 – Inheritance (Pewarisan)

Class `Mage` mewarisi class `Hero`.  
Penggunaan `super()` penting agar atribut milik parent class ikut terbentuk.  
Jika `super()` dihapus, maka terjadi error karena atribut induk tidak dibuat.

Bukti:
![Latihan 3.1](./Laporan/Latihan%203.1.png))  
![Latihan 3.2](./Laporan/Latihan%203.2.png)

---

## Latihan 4 – Encapsulation

Atribut `hp` dibuat private menggunakan `__hp`.  
Akses data dilakukan melalui Getter dan Setter untuk menjaga validitas nilai HP.  
Meskipun Python masih mengizinkan akses lewat Name Mangling, cara tersebut tidak dianjurkan.

Bukti:
![Latihan 4.1](./Laporan/Latihan%204.1.png)  
![Latihan 4.2](./Laporan/Latihan%204.2.png)

---

## Latihan 5 – Abstraction & Interface

Class abstract `GameUnit` digunakan sebagai kontrak.  
Setiap class turunan wajib mengimplementasikan method yang didefinisikan.  
Jika method tidak dibuat, object tidak bisa diinstansiasi.

Bukti:
![Latihan 5.1](./Laporan/Latihan%205.1.png)  
![Latihan 5.2](./Laporan/Latihan%205.2.png)

---

## Latihan 6 – Polymorphism

Berbagai class turunan memiliki method `serang()` dengan perilaku berbeda.  
Penambahan class baru dapat dilakukan tanpa mengubah kode loop.  
Nama method harus konsisten agar polimorfisme berjalan dengan benar.

Bukti:
![Latihan 6.1](./Laporan/Latihan%206.1.png)  
![Latihan 6.2](./Laporan/Latihan%206.2.png)

---

## Kesimpulan

Dengan menerapkan OOP, program menjadi lebih terstruktur, mudah dikembangkan, aman dari kesalahan data, dan fleksibel saat menambah fitur baru. Konsep OOP sangat penting dalam pengembangan aplikasi dan game.

================================================================
PROYEK INTEGRASI OOP (CHALLENGE)
================================================================

# Sistem Manajemen Inventaris "TechMaster"

Bagian ini merupakan Proyek Integrasi OOP yang menggabungkan seluruh konsep Object Oriented Programming (OOP) yang telah dipelajari, yaitu Abstraction, Encapsulation, Inheritance, dan Polymorphism.

---

## Deskripsi Proyek

TechMaster adalah sistem backend sederhana untuk mengelola stok dan transaksi barang elektronik. Sistem ini dirancang agar data penting seperti stok dan harga tidak dapat diubah sembarangan serta mendukung perhitungan pajak yang berbeda untuk setiap jenis barang.

Jenis barang yang didukung:

- Laptop
- Smartphone

---

## Penerapan Konsep OOP

### Abstraction

Menggunakan abstract class `BarangElektronik` sebagai kerangka dasar yang tidak dapat diinstansiasi langsung dan berisi method abstrak yang wajib diimplementasikan oleh class turunan.

### Encapsulation

Atribut sensitif seperti stok dan harga dasar dibuat private dan hanya dapat diakses atau diubah melalui method tertentu dengan validasi.

### Inheritance

Class `Laptop` dan `Smartphone` mewarisi class `BarangElektronik` serta menambahkan atribut dan aturan pajak masing-masing.

### Polymorphism

Method yang sama memiliki perilaku berbeda tergantung jenis objek. Sistem transaksi dapat memproses berbagai jenis barang tanpa perlu mengetahui tipe objek secara spesifik.

---

## Alur Program

1. Admin membuat data produk.
2. Admin menambahkan stok (termasuk percobaan stok negatif).
3. User melakukan pembelian.
4. Sistem menampilkan detail transaksi dan total harga akhir termasuk pajak.

---

## Hasil Running Program

Berikut adalah dokumentasi hasil eksekusi program TechMaster:

![Hasil Run TechMaster](./Laporan/Screenshot%202026-02-06%20at%2009.29.05.png)

> Catatan: Gambar menunjukkan proses setup data, validasi stok, detail transaksi, dan total tagihan akhir.

---

## Kesimpulan

Proyek TechMaster membuktikan bahwa penerapan empat pilar OOP dapat menghasilkan sistem yang terstruktur, aman, fleksibel, dan mudah dikembangkan untuk kebutuhan aplikasi nyata.
