#Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.
given_list = [7, 12, 3, 3, 9, 21, 7, 2]
only_odd = []
only_odd.extend(x for x in given_list if x % 2 != 0)
print(only_odd)
