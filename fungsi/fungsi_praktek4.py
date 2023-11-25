def hitung_jumlah_digit(n):
    return sum(int(digit) for digit in str(abs(n)))

def main():
    try:
        bilangan = int(input("Masukkan bilangan: "))
        hasil = hitung_jumlah_digit(bilangan)
        print(f"Jumlah digit dari {bilangan} adalah: {hasil}")
    except ValueError:
        print("Masukkan bilangan sebagai angka.")

if __name__ == "__main__":
    main()
