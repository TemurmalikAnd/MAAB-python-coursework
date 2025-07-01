#Create a program to ask name and year of birth from user and tell them their age.
thisYear = 2025
userName = input("Enter your name: ")
userYear = int(input("Enter your year you were born: "))
print(f"You are {thisYear - userYear} years old, {userName}")