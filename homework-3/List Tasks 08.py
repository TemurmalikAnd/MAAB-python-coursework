#Slice List: Create a new list that contains only the first three elements of the original list.
dataList = ['apple', 42, 3.14, True, 'dog', None, -7]
newList = []
newList.extend(dataList[0:3])
print(f"The first three elements are: {newList}")