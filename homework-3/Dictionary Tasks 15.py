#Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
givenKey1 = ['apple', 'banana', 'cherry']
givenKey2 = [1, 2, 3]
newDictionary = dict(zip(givenKey1, givenKey2))
print(newDictionary)
