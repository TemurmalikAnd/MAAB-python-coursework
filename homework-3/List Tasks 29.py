#Remove Element by Index: Given a list and an index, remove the element at that index if it exists.
given_list = ['banana', 88, False, 3.1415, 'hello', None, -42, 'x', 0, True, 'GPT', 7.77, 'mint', 999, {}, [1, 2], 'end']
user_remove = int(input('Enter the index of the element you want to remove: '))

given_list.remove(given_list[user_remove])
print(given_list)
