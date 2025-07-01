#Check for Common Keys: Given two dictionaries, check if they have any keys in common.
givenDict1 = {
    'zebra': 5,
    'apple': 3,
    'monkey': 8,
    'banana': 1
}

givenDict2 = {
    'dog': 4,
    'pear': 2,
    'ant': 9,
    'banana': 1
}

givenSet = set(givenDict1.keys()) & set(givenDict2.keys())
print(bool(givenSet))
