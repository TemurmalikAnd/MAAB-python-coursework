#Merge and Sort: Given two lists, create a new sorted list that merges both lists.
first_list = [-95, -42, -17, -4, 0, 3, 8, 15, 22, 37, 41, 59, 63, 74, 88, 92, 105]
second_list = [37, 15, 91, 3, 57, 75, 19, 11, 43, 69]

new_list = first_list + second_list
new_list.sort()
print(new_list)
