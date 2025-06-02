def prime_generator(end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num

print("Прості числа до 10 включно:", list(prime_generator(15)))
