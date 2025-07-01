#Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
d1 = {'x': 5, 'y': 8, 'z': 5, 'w': 3, 'v': 8}
swap_machine = {v: k for k, v in d1.items()}
print(swap_machine)
