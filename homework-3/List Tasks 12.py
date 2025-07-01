#Insert Element: Given a list and an element, insert the element at a specified index.
dataList = ['apple', 'sun', 'moon', 'apple', 'star', 'moon', 'sun', 'cloud', 'apple']
element = "TREE"
print(f"The element is:{element}")
user_input = int(input("Index of insertion: "))
dataList.insert(user_input, element)
print(f"The new list is: {dataList}")