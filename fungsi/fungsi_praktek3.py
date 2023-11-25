def hitung_pangkat(bilangan, eksponen):
    return bilangan ** eksponen

def main():
    try:
        bilangan = float(input("Masukkan bilangan: "))
        eksponen = int(input("Masukkan eksponen: "))
        
        hasil = hitung_pangkat(bilangan, eksponen)
        print(f"{bilangan}^{eksponen} = {hasil}")
    except ValueError:
        print("Masukkan bilangan sebagai angka dan eksponen sebagai bilangan bulat.")

if __name__ == "__main__":
    main()
