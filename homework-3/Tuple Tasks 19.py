#Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
given_tuple = ('apple', 42, 'mint', -7, 'hello', 3.14, 'GPT', 999, 'apple')
element = 'apple'
x = list(given_tuple)
x.remove(element)
y = tuple(x)
print(y)
