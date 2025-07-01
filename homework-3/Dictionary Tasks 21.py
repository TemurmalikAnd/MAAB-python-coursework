#Sort Dictionary by Value: Create a new dictionary sorted by values.
givenDict = {
    'zebra': 5,
    'apple': 3,
    'monkey': 8,
    'banana': 1
}
sortedDictionary = {k: v for k, v in sorted(givenDict.items(), key = lambda item:item[1])}
print(sortedDictionary)
