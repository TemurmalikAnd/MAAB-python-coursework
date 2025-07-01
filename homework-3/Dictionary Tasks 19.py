#Count Unique Values: Given a dictionary, determine the number of unique values it contains.
givenDict = {
    'apple': 1,
    'banana': 2,
    'cherry': 1,
    'date': 3,
    'elderberry': 2
}

givenSet = set(givenDict.values())
print(len(givenSet))
