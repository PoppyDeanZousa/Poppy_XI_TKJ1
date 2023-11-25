def tentukan_restart(pembaruan_perangkat lunak):
    if pembaruan_perangkat_lunak.lower() == "ya":
        return "Sistem perlu di-restart."
    elif pembaruan_perangkat_lunak.lower() == "tidak":
        return "Sistem tidak perlu di-restart."
    else:
        return "Masukkan jawaban yang valid (ya/tidak)."

def main():
    pembaruan_perangkat_lunak = input("Apakah ada pembaruan perangkat lunak? (ya/tidak): ")

    hasil = tentukan_restart(pembaruan_perangkat_lunak)
    print(hasil)

if __name__ == "__main__":
    main()
