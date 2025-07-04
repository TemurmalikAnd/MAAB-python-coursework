"""Print the square of each number which is less than n on a separate line.

input: n = 5
output:
    1
    4
    9
    16

"""
number = 5
for i in range(1, number):
    print("   ", i**2)