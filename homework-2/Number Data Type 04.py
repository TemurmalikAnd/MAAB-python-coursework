#Write a program that takes two numbers and prints out the result of integer division and the remainder.
user_input1 = int(input("Enter the first number: "))
user_input2 = int(input("Enter the second number: "))

if user_input2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    division = user_input1 // user_input2
    remainder = user_input1 % user_input2
    print("Result:", division)
    print("Remainder:", remainder)
