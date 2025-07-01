#Ask the user for a string and replace all the vowels with a symbol (e.g., *).
userInput = input('Input: ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for v in vowels:
    userInput = userInput.replace(v, "*")
print(f"Output: {userInput}")
