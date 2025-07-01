#Create Default Dictionary: Create a dictionary that provides a default value for missing keys.
from collections import defaultdict
givenDict = defaultdict(lambda: "Not present")
givenDict["apple"] = '2'
givenDict["banana"] = '2'
print(givenDict["cherry"])
