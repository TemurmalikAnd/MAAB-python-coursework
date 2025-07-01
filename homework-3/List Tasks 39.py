#Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input = int( input('Amount of sublist: '))
new_list = []
x = len(given_list)
for i in range(0, x, user_input):
    new_list.append(given_list[i: i+user_input])
print(new_list)
