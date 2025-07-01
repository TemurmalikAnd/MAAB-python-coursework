# Write a program that counts the number of vowels and consonants in a given string.

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z'
]

user_input = 'nJkpeZtqWbLM'
vowel_count = 0
consonant_count = 0

for letter in user_input.lower():  # Convert to lowercase to handle uppercase letters
    if letter in vowels:
        vowel_count += 1
    elif letter in consonants:
        consonant_count += 1

# Always print the result (no need for the if-check)
print(f"There are {vowel_count} vowels and {consonant_count} consonants in your input")