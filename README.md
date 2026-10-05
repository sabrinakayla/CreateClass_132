Penjelasan Struktur:

1. persegi_panjang.py 
File ini isinya kerangka utama atau cetak biru (blueprint) dari objek persegi panjang.
- class PersegiPanjangSederhana: Ini buat bikin wadah kelasnya.
- def __init__(self, panjang, lebar): Ini konstruktor buat ngenalin atribut panjang dan lebar pas objeknya dibuat.
- self.panjang & self.lebar: Buat nyimpen nilai dari inputan supaya nempel ke objeknya.
- hitung_keliling(self): Fungsi buat ngitung keliling pakai rumus matematika biasa.
- hitung_luas(self): Fungsi buat ngitung luas persegi panjang.
- __str__(self): Fungsi bawaan python biar nanti pas objeknya diprint, bentuknya langsung jadi kalimat yang rapi dan gampang dibaca.

2. main.py 
File ini yang dijalanin buat ngecek programnya dan tempat interaksi sama user.
- from persegi_panjang import ... : Perintah buat ngambil kelas dari file sebelah supaya bisa dipakai di sini.
- try dan except ValueError: Buat jaga-jaga kalau usernya malah ngetik huruf, jadi programnya nggak mendadak error atau menutup sendiri.
- input(): Buat nerima angka panjang dan lebar dari user.
- if / else: Pengecekan biar nggak ada angka 0 atau minus yang masuk.
- Terakhir, manggil fungsi hitung luas dan keliling terus nampilin hasilnya ke layar.