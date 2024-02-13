def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

max_sum = 0
max_num = None

while True:
    num = int(input("Введите целое число (для завершения введите 0): "))
    if num == 0:
        break

    current_sum = sum_of_digits(num)
    if current_sum > max_sum:
        max_sum = current_sum
        max_num = num

if max_num is not None:
    print(f"Число с максимальной суммой цифр: {max_num}")
else:
    print("Вы не ввели ни одного числа.")
