from datetime import datetime

def cek_tepat_waktu(estimasi_selesai, tanggal_target):
    # Mengubah string tanggal menjadi objek datetime
    estimasi_selesai = datetime.strptime(estimasi_selesai, "%Y-%m-%d")
    tanggal_target = datetime.strptime(tanggal_target, "%Y-%m-%d")

    # Membandingkan tanggal estimasi selesai dengan tanggal target
    if estimasi_selesai <= tanggal_target:
        return "Tepat waktu"
    else:
        return "Terlambat"

def main():
    estimasi_selesai = input("Masukkan estimasi waktu selesai proyek (format: YYYY-MM-DD): ")
    tanggal_target = input("Masukkan tanggal target selesai proyek (format: YYYY-MM-DD): ")

    hasil = cek_tepat_waktu(estimasi_selesai, tanggal_target)
    print(hasil)

if __name__ == "__main__":
    main()
