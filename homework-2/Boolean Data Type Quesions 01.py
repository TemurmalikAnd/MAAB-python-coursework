#Write a program that accepts a username and password and checks if both are not empty.
username = input('Please enter your username: ')
password = input('Please enter your password: ')
if username and password:
    print('True')
else:
    print('False')