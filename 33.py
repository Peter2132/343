def sum_digits(number):
    number_str = str(number)
    total = 0
    for digit in number_str:
        total += int(digit)

    return total
number = int(input("Введите положительное целое число: "))

if number <= 0:
    print("Пожалуйста, введите положительное целое число.")
else:
    result = sum_digits(number)
    print(f"Сумма цифр числа {number} равна {result}.")