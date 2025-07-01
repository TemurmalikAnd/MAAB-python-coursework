#Count Even Numbers: Given a list of integers, count how many of them are even.
dataList = [12, -45, -3, 78, -91, 6, -27, 33, -8, 59, -100, 24, -1]
counter = 0
for i in dataList:
    if i%2==0:
        counter += 1
print(f"{counter} number(s) are even in the list")
