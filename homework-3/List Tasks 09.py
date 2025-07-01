#Reverse List: Create a new list that contains the elements of the original list in reverse order.
dataList = ['apple', 42, 3.14, True, 'dog', None, -7]
newList = []
newList.extend(dataList[::-1])
print(f"The reversed list: {newList}")
