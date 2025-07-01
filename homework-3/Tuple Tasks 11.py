#Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
given_tuple = ('mint', 88, 'sun', -42, 'alpha', 17, 'zebra', 5, 'alpha')

element = 'alpha'
indices = [i for i, x in enumerate(given_tuple) if x == element]
print(indices)
