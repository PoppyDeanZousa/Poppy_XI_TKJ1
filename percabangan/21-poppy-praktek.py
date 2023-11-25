def tentukan_kategori_produk(penjualan):
    if penjualan > 1000:
        kategori = "Produk Terlaris"
    elif 500 <= penjualan <= 1000:
        kategori = "Produk Populer"
    else:
        kategori = "Produk Biasa"
    return kategori

def main():
    try:
        penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))
        if penjualan >= 0:
            kategori = tentukan_kategori_produk(penjualan)
            print(f"Jumlah penjualan: {penjualan} unit")
            print(f"Kategori produk: {kategori}")
        else:
            print("Jumlah penjualan tidak boleh negatif.")
    except ValueError:
        print("Masukkan jumlah penjualan dalam bentuk angka.")

if __name__ == "__main__":
    main()
