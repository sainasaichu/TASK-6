def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Filter the prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Count the prime numbers
prime_count = len(prime_numbers)

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", prime_count)
