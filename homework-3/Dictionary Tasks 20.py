#Sort Dictionary by Key: Create a new dictionary sorted by keys.
givenDict = {
    'zebra': 5,
    'apple': 3,
    'monkey': 8,
    'banana': 1
}
newList = list(givenDict.keys())
newList.sort()
sortedDictionary = {i: givenDict[i] for i in newList}
print(sortedDictionary)
