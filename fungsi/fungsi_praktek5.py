def fibonacci(n):
    if n <= 0:
        return "Masukkan nilai n yang lebih besar dari 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def main():
    try:
        n = int(input("Masukkan nilai n untuk bilangan Fibonacci: "))
        hasil = fibonacci(n)
        print(f"Bilangan Fibonacci ke-{n} adalah: {hasil}")
    except ValueError:
        print("Masukkan nilai n sebagai bilangan bulat.")

if __name__ == "__main__":
    main()
