#Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.
dataList = ['apple', 'sun', 'moon', 'apple', 'star', 'moon', 'sun', 'cloud', 'apple']
newList = []
list(set(dataList))
newList.extend(dataList)
print(f"List without duplicates: {set(dataList)}")
