"""
Ask the user for a sentence and create an acronym from the first letters of each word.
Example:

    Input: "World Health Organization"
    Output: "WHO"
"""
userInput = input('Input: ')
dataset = userInput.split()
space = ""
for i in dataset:
    space = space + i[0]
print(f"Output: {space}")
