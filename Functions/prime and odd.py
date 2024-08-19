def is_prime_and_odd(num):
    # Check if the number is odd
    if num % 2 == 0:
        return False, "The number is even, not odd."

    # Check if the number is prime
    if num < 2:
        return False, "The number is less than 2, not prime."

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False, "The number is not prime."

    return True, "The number is prime and odd."

n=97
print(is_prime_and_odd(n))