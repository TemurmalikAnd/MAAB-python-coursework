"""

Write a program that checks if a string starts with one word and ends with another.
Example:

    Input: "Python is fun!"
    Starts with: "Python"
    Ends with: "fun!"

"""
userInput = input('Input: ')
userInput = userInput.split()
print(f"Starts with: {userInput[0]}")
print(f"Ends with: {userInput[-1]}")
