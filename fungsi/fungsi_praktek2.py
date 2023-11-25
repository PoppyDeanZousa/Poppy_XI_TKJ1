def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n-1)

def main():
    try:
        bilangan = int(input("Masukkan bilangan untuk menghitung faktorial: "))
        if bilangan >= 0:
            hasil = hitung_faktorial(bilangan)
            print(f"Faktorial dari {bilangan} adalah: {hasil}")
        else:
            print("Masukkan bilangan non-negatif.")
    except ValueError:
        print("Masukkan bilangan sebagai bilangan bulat.")

if __name__ == "__main__":
    main()
