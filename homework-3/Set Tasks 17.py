#Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
integer_set = {4, 11, 18, 23, 37, 42, 56}
even_set = {i for i in integer_set if i % 2 != 0}
print(even_set)
