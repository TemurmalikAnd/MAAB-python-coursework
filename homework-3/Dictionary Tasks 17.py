#Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
nestedDict = {
    "name": "Alice",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    }
}
valueRetrieve = nestedDict["address"]["city"]
print(valueRetrieve)
