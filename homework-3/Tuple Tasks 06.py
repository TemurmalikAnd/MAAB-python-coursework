#Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
given_tuple = ('apple', 42, 'mint', -7, 'hello', 3.14, 'GPT', 999)
element = given_tuple[-1]
if given_tuple == '':
    print('Empty tuple')
else:
    print(element in given_tuple)
