#First Element: Access the first element of a list, considering what to return if the list is empty.
dataList = ['apple', 42, 3.14, True, 'dog', None, -7]
if dataList[0] in dataList:
    print(f"The first element is {dataList[0]}")
else:
    print('The list does not contain any values')
