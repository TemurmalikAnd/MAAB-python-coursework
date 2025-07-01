#Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
# Second (nested) dictionary

def hasNested(inputDict):
    for value in inputDict.values():
        if isinstance(value, dict):
            return True
    return False

main_dict = {
    'name': 'Alice',
    'age': 17,
    'grades': {
        'math': 90,
        'science': 85
    }   # nested here
}

if hasNested(main_dict):
    print('Contains nested dictionary')
else:
    print('No nested dictionary')
