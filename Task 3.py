def is_happy_number(n):
    """Check if a number is a happy number."""
    def get_next(number):
        return sum(int(char) ** 2 for char in str(number))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Filter the happy numbers
happy_numbers = [num for num in numbers if is_happy_number(num)]

# Count the happy numbers
happy_count = len(happy_numbers)

print("Happy numbers:", happy_numbers)
print("Count of happy numbers:", happy_count)
