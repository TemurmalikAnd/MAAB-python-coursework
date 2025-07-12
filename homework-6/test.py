dict = {'Top': 1, 'Amazing': 3, "Superb": 2, "Disgustint": 5, "Alas": 4}
sorted_val = {k: v for k, v in sorted(dict.items(), key = lambda v: v[1], reverse=True)}
for key, value in sorted_val.items():
    print(f"{key} - {str(value)}")
print(key, value)