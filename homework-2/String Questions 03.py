"""
Write a Python program to:

    Take a string input from the user.
    Print the length of the string.
    Convert the string to uppercase and lowercase.
"""
while True:
    input_string = input("Enter a string (letters only, no numbers or symbols): ").strip()

    if not input_string:
        print("Error: Input cannot be empty. Try again.")
    elif not input_string.replace(" ", "").isalpha():  # Allows spaces but checks alphabetic chars
        print("Error: Only letters and spaces allowed. Try again.")
    else:
        break  # Valid input

# Print the length of the string
print(f"\nLength of the string: {len(input_string)}")

# Convert to uppercase and lowercase
uppercase_string = input_string.upper()
lowercase_string = input_string.lower()

print(f"Uppercase: {uppercase_string}")
print(f"Lowercase: {lowercase_string}")