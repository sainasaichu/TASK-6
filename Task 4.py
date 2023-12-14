number = int(int(input("enter a number : ")))

if number < 10:
    print("number is a single digit sum = ", number * 2)
else:
    last_digit = number % 10

    first_digit = number
    while first_digit > 9:
        first_digit = first_digit // 10
    result = last_digit + first_digit
    print(f"sum of first and last digit of a number {number} : {result}")
