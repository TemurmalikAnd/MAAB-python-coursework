#Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.
given_list = [12, -45, -3, 78, -91, 6, -27, 33, -8, 59, -100, 24, -1]
new_list = []
new_list.extend(x for x in given_list if x < 0)
a = sum(new_list)
print(a)