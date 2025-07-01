#Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
non_unique = ('apple', 42, 'banana', 'apple', 3.14, 42, 'banana')
unique = tuple(set(non_unique))
print(unique)
