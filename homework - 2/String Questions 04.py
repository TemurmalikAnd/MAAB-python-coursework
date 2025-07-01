#Write a Python program to check if a given string is palindrome or not.

def is_palindrome(input_string):
    # Remove all non-alphabetic characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalpha())

    # Check if cleaned string is a palindrome
    return cleaned_string == cleaned_string[::-1]


def main():
    print("Palindrome Checker")
    while True:
        input_string = input("\nEnter a string (or 'quit' to exit): ").strip()

        if not input_string:
            print("Error: Input cannot be empty. Try again.")
            continue
        if input_string.lower() == 'quit':
            break

        if is_palindrome(input_string):
            print("✅ It's a palindrome!")
        else:
            print("❌ It's not a palindrome.")


if __name__ == "__main__":
    main()