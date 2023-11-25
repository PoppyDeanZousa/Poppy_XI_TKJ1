def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2 * batas, 2):
        total += i
    return total

def main():
    try:
        batas = int(input("Masukkan batas deret bilangan ganjil: "))
        if batas >= 1:
            hasil = total_deret_ganjil(batas)
            print(f"Total deret bilangan ganjil hingga batas {batas} adalah: {hasil}")
        else:
            print("Masukkan batas yang lebih besar dari atau sama dengan 1.")
    except ValueError:
        print("Masukkan batas sebagai bilangan bulat.")

if __name__ == "__main__":
    main()
