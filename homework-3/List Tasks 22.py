#Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.
given_list = [7, 12, 3, 3, 9, 21, 7, 2]
only_even = []
only_even.extend(x for x in given_list if x % 2 == 0)
print(only_even)