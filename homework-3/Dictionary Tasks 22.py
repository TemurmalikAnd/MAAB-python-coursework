#Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
def filter_dict(original_dict):
    filtered_dict = {}
    for key, value in original_dict.items():
        # Skip if the value is a string
        if isinstance(value, str):
            continue
        # Check if the value is numeric and >= 5
        if isinstance(value, (int, float)) and value >= 5:
            filtered_dict[key] = value
    return filtered_dict

# Test the function
original_dict = {'a': 5, 'b': 12, 'c': 3, 'd': 8, 'e': 'hello', 'f': 4.5}
print(filter_dict(original_dict))
