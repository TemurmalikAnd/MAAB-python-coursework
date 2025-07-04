"""
6. Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

    A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for number in range(1, 101):
    if is_prime(number):
        print(number)
