#Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
given_tuple = ('cat', 7, 'mint', 3.14, 'mint', 7, 'cat')
checker = given_tuple == given_tuple[::-1]
print(checker)
