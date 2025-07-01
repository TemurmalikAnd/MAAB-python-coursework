#Write a program that takes three numbers and checks if all of them are different.
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))
print(len({number1, number2, number3}) == 3)
