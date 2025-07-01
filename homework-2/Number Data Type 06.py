#Create a program that accepts a number and returns the last digit of that number.
try:
    number = int(input("Enter a number: "))
    print(f"The last digit is: {abs(number) % 10}")
except ValueError:
    print("Please enter a valid integer.")
