#Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
given_list = ['apple', 42, 3.14, True, 'dog', None, -7]
new_list = []
new_list.extend(given_list[::-1])
print(new_list)