"""
1. Return uncommon elements of lists. Order of elements does not matter.

input:
    list1 = [1, 1, 2]
    list2 = [2, 3, 4]
output: [1, 1, 3, 4]

input:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
output: [1, 2, 3, 4, 5, 6]

input:
    list1 = [1, 1, 2, 3, 4, 2]
    list2 = [1, 3, 4, 5]
output: [2, 2, 5]
"""
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result = []
for i in list1:
    if i not in list2:
        result.append(i)
for x in list2:
    if x not in list1:
        result.append(x)
print(result)