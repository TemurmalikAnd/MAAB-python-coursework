#Ask the user for a string and print the reversed version of it.
userInput = input()
new = userInput.split()[::-1]
news = ' '.join(new)
print(news)