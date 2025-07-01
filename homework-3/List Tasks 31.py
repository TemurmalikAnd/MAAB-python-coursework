#Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.
given_list = ['xenomorph', 'banana', 'cherry']
number = 3
new_list = []
for i in given_list:
    for x in range(number):
        new_list.append(i)
print(new_list)