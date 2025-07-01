#Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
given_list = ['banana', False, 3.1415, 'hello', None, -42, 'x', 0, True, 'GPT', 7.77, 'mint', 999, {}, [1, 2], 'end']
middle_list = []
length = len(given_list)
if length % 2 == 0 :
    middle_list.extend(given_list[length//2 - 1: length//2 + 1 ])
else:
    middle_list.append(given_list[length//2])
print(middle_list)
