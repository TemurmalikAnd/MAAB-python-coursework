# Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
given_tuple = ('banana', 23, 'sky', -11, 0, 'code', 76, 'open', 3)
given_number = 3
new_tuple = ()

for element in given_tuple:
    for i in range(given_number):
        new_tuple += (element,)

print(new_tuple)
