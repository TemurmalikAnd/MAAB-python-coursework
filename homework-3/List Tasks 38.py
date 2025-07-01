#Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
check_palindrome = [1, 'a', True, 3.14, 'b', 3.14, True, 'a', 1]
if check_palindrome == check_palindrome[::-1]:
    print("is a palindrome")
else:
    print('is not a palindrome')