"""5. Password Checker Task: Create a simple password checker.

    Ask the user to enter a password.
    If the password is shorter than 8 characters, print "Password is too short."
    If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.".
    If the password meets both criteria, print "Password is strong."

"""
def password_checker():
    while True:
        user_input = input('Enter a password: ')
        if user_input == '':
            print('Password cannot be empty')
        elif len(user_input) < 8:
            print('Password must be longer that 8 characters')
        elif  not any(char.isdigit() for char in user_input):
            print('Password must contain a digit')
        elif not any(char.isupper() for char in user_input):
            print('Password must contain an uppercase letter.')

        else:
            print('Password is strong')
            break

password_checker()