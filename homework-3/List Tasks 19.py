#Replace Element: Given a list, replace the first occurrence of a specified element with another element.
dataList = main_list = ['apple', 'sun', 'moon', 'apple', 'star', 'moon', 'sun', 'cloud', 'apple']
print(dataList)
userReplace = input('Replace: ')
userWith = input('With: ')
x = dataList.index(userReplace)
dataList.insert(x, userWith)
dataList.remove(userReplace)
print(dataList)
