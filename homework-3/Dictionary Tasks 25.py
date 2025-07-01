#Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
givenDict = {
    'apple': 1,
    'banana': 2,
    'cherry': 1,
    'date': 3,
    'elderberry': 2
}
firstPair = list(givenDict.items())[0]
print(firstPair)
