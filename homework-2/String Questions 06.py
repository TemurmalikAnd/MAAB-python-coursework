#Write a Python program to check if one string contains another.

def check_string_containment():
    """Check if one string contains another, with proper input validation."""
    while True:
        main_string = input("Enter the main string (or 'quit' to exit): ").strip()

        # Exit condition
        if main_string.lower() == 'quit':
            print("Exiting program...")
            break

        # Input validation
        if not main_string:
            print("Error: Main string cannot be empty. Please try again.")
            continue

        search_string = input("Enter the string to search for: ").strip()
        if not search_string:
            print("Error: Search string cannot be empty. Please try again.")
            continue

        # Case-insensitive check with proper messaging
        if search_string.lower() in main_string.lower():
            print(f"✅ Found '{search_string}' in the main string!")
        else:
            print(f"❌ Did not find '{search_string}' in the main string.")

        # Offer to check another string
        another = input("Check another string? (y/n): ").lower()
        if another != 'y':
            break


if __name__ == "__main__":
    check_string_containment()