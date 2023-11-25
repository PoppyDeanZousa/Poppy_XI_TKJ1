def hitung_diskon(total_belanja, status_anggota):
    if status_anggota == "premium":
        if total_belanja > 500000:
            diskon = 0.15  # 15%
        else:
            diskon = 0.1  # 10%
    elif status_anggota == "biasa":
        if total_belanja > 300000:
            diskon = 0.07  # 7%
        else:
            diskon = 0  # Tidak ada diskon
    else:
        print("Status anggota tidak valid.")
        return None

    return diskon

def main():
    total_belanja = float(input("Masukkan total belanjaan pelanggan: "))
    status_anggota = input("Masukkan status anggota (premium atau biasa): ").lower()

    diskon = hitung_diskon(total_belanja, status_anggota)

    if diskon is not None:
        total_bayar = total_belanja - (total_belanja * diskon)
        print(f"Total belanjaan: Rp {total_belanja:,.2f}")
        print(f"Diskon: {diskon * 100}%")
        print(f"Total bayar setelah diskon: Rp {total_bayar:,.2f}")

if __name__ == "__main__":
    main()
