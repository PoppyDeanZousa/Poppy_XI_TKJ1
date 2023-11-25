def hitung_bonus(performa, gaji_tahunan):
    bonus = (
        0.2 * gaji_tahunan if performa == 5 else
        0.1 * gaji_tahunan if performa == 4 else
        0.05 * gaji_tahunan if performa == 3 else
        0.02 * gaji_tahunan if performa == 2 else
        0  # Tidak ada bonus untuk performa 1
    )
    return bonus

def main():
    try:
        performa = int(input("Masukkan nilai performa karyawan (1-5): "))
        gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

        if 1 <= performa <= 5 and gaji_tahunan >= 0:
            bonus = hitung_bonus(performa, gaji_tahunan)
            print(f"Bonus tahunan: Rp {bonus:,.2f}")
        else:
            print("Masukkan nilai performa antara 1-5 dan gaji tahunan tidak boleh negatif.")
    except ValueError:
        print("Masukkan nilai performa sebagai bilangan bulat dan gaji tahunan sebagai bilangan.")

if __name__ == "__main__":
    main()
