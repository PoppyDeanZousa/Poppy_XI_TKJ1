def tentukan_hasil(nila_tugas, nilai_ujian):
    if nilai_tugas > 70 and nilai_ujian > 60:
        hasil = "Lulus"
    else:
        hasil = "Gagal"
    return hasil

def main():
    nilai_tugas = float(input("Masukkan nilai tugas siswa (skala 0-100): "))
    nilai_ujian = float(input("Masukkan nilai ujian siswa (skala 0-100): "))

    if 0 <= nilai_tugas <= 100 and 0 <= nilai_ujian <= 100:
        hasil = tentukan_hasil(nilai_tugas, nilai_ujian)
        print(f"Nilai tugas: {nilai_tugas}")
        print(f"Nilai ujian: {nilai_ujian}")
        print(f"Hasil: {hasil}")
    else:
        print("Nilai tugas dan nilai ujian harus dalam rentang 0-100.")

if __name__ == "__main__":
    main()
