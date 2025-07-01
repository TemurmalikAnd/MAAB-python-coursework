#Write a program that checks if a number is positive and even.
def check_positive_even():
    while True:
        user_input = input('Enter a number (or "q" to quit): ').strip()

        # Allow user to quit
        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        # Check if input is a valid number
        try:
            number = int(user_input)
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue

        # Check if number is positive and even
        is_positive_even = number > 0 and number % 2 == 0

        # More descriptive output
        if is_positive_even:
            print(f"✅ {number} is positive and even!")
        else:
            # Explain why it doesn't meet criteria
            if number <= 0:
                print(f"❌ {number} is not positive.")
            else:
                print(f"❌ {number} is positive but odd.")


if __name__ == "__main__":
    check_positive_even()