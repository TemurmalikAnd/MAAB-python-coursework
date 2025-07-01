#Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.
userInput = input('Enter a string: ')
userChar = input('Enter a character you want to remove: ')
result = userInput.replace(userChar, "")
print(f"Output: {result}")
