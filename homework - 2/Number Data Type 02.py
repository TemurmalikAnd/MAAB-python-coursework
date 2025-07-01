#Write a Python file that asks for three numbers and outputs the largest and smallest.
dataList = []
for i in range(3):
    user_input = int(input('Enter: '))
    dataList.append(user_input)

print(f"Max: {max(dataList)}")
print(f"Min: {min(dataList)}")
