"""
Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
Example:

    Input sentence: "I love apples."
    Replace: "apples"
    With: "oranges"
    Output: "I love oranges."
"""
userInput = input('Input sentence: ')
userReplace = input('Replace: ')
userWith = input('With: ')
data = userInput.split()
index = data.index(userReplace)
data.remove(userReplace)
data.insert(index, userWith)

print(f"Output: {' '.join(data)}")
