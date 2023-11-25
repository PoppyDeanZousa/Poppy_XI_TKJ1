def hitung_diskon(total_belanja):
    if total_belanja > 500000:
        diskon = 0.1  # 10%
    elif 300000 <= total_belanja <= 500000:
        diskon = 0.05  # 5%
    else:
        diskon = 0  # Tidak ada diskon

    return diskon

def main():
    total_belanja = float(input("Masukkan total belanjaan pelanggan: "))

    diskon = hitung_diskon(total_belanja)
    total_bayar = total_belanja - (total_belanja * diskon)

    print(f"Total belanjaan: Rp {total_belanja:,.2f}")
    print(f"Diskon: {diskon * 100}%")
    print(f"Total bayar setelah diskon: Rp {total_bayar:,.2f}")

if __name__ == "__main__":
    main()
