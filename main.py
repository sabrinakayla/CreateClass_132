from persegi_panjang import PersegiPanjangSederhana

try:
    panjang1 = int(input("Masukkan Panjang: "))
    lebar1 = int(input("Masukkan Lebar: "))
    
    if panjang1 <= 0 or lebar1 <= 0:
        print("Panjang dan lebar harus lebih dari 0.")
    else:
        persegi_panjang1 = PersegiPanjangSederhana(panjang1, lebar1)
        print(persegi_panjang1)
        print(f"Keliling Persegi Panjang: {persegi_panjang1.hitung_keliling()} cm")
        print(f"Luas Persegi Panjang: {persegi_panjang1.hitung_luas()} cm²")
except ValueError:
    print("Input harus berupa angka bulat (integer).")