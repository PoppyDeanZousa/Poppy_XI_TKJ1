def tentukan_status_proyek(status_persiapan):
    if status_persiapan.lower() == "siap":
        return "Proyek diluncurkan."
    elif status_persiapan.lower() == "tunda":
        return "Proyek ditunda."
    else:
        return "Masukkan status persiapan yang valid (siap/tunda)."

def main():
    status_persiapan = input("Masukkan status persiapan proyek (siap/tunda): ")

    hasil = tentukan_status_proyek(status_persiapan)
    print(hasil)

if __name__ == "__main__":
    main()
