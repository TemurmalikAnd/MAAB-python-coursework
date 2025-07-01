#Find All Indices: Given a list and an element, find all the indices of that element in the list.
my_list = [1, 2, 3, 2, 4, 2]
element = 2
indices = [i for i, x in enumerate(my_list) if x == element]
print(indices)