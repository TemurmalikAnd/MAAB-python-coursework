#Write a program that asks the user for a sentence and prints the number of words in it.

userInput = input('Enter a sentence: ')
data = userInput.replace(" ", "")
print(f"The length is: {len(data)}")
