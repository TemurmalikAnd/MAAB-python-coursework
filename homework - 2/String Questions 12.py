#Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).

userInput = input('Input: ')
new = userInput.split()
newer = '-'.join(new)
print(newer)