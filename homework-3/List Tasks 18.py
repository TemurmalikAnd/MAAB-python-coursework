#Find Sublist: Given a list and a sublist, check if the sublist exists within the list.
main_list = ['book', 3.14, ['pen', 'notebook', 42], 'lamp', -7]
sublist = ['pen', 'notebook', 42]
if sublist in main_list:
    print('Exists')
else:
    print('Does\'snt exist')