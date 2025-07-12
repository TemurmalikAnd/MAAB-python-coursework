try:
    number = int(input('Enter a positive integer: '))
    if number <= 0:
        print('Please enter a positive integer (greater than 0)')
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                print(f"{i} is a factor of {number}")
except ValueError:
    print('Please enter a valid integer')