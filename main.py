def calculate_digit_sum(number):
    return sum(int(digit) for digit in str(abs(number)))

max_sum = 0
number_with_max_sum = []

try:
    while True:
        user_input = input("Enter an integer (0 to stop): ")

        if not user_input.isdigit():
            raise ValueError("Please enter an integer.")

        number = int(user_input)

        if number == 0:
            break

        digit_sum = calculate_digit_sum(number)

        if digit_sum > max_sum:
            max_sum = digit_sum
            number_with_max_sum = [number]
        elif digit_sum == max_sum:
            number_with_max_sum.append(number)

    if number_with_max_sum:
        print(f"The number(s) with the maximum sum of digits is/are: {number_with_max_sum}")
    else:
        print("No valid numbers were entered.")

except ValueError as e:
    print(f"Error: {e}")
