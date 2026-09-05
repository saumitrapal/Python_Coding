def is_prime(num):
    if num <= 1:
        return False
    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

prime_number = is_prime(75)
print(prime_number)
