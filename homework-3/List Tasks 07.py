#Last Element: Access the last element of a list, considering what to return if the list is empty.
dataList = ['apple', 42, 3.14, True, 'dog', None, -7]
if dataList[-1] in dataList:
    print(f"The last element is {dataList[-1]}")
else:
    print('The list does not contain any values')
