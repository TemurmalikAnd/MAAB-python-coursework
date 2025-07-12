def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

try:
    given_n = int(input('Enter a number to check if it is prime: '))
    if is_prime(given_n):
        print(f"{given_n} is a prime number")
    else:
        print(f"{given_n} is not a prime number")
except ValueError:
    print('Please enter a valid integer')