#Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
list_a = [2, 9, 14, 21, 30]
list_b = [5, 9, 17, 21, 33]
set_c = set(list_a + list_b)
print(set_c)
