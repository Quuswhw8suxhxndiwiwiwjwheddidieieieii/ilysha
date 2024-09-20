def factorial(n):
    if n < 0:
        return None  # Факториал отрицательных чисел не определен
    elif n == 0 or n == 1:
        return 1  # Факториал 0 и 1 равен 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    number = int(input("Введите число для вычисления факториала: "))
    result = factorial(number)
    
    if result is not None:
        print(f"Факториал {number} равен {result}")
    else:
        print("Факториал отрицательного числа не определен.")

if __name__ == "__main__":
    main()