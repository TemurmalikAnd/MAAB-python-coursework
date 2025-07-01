#Remove Element: Given a set and an element, remove the element if it exists.
random_set = {17, "orange", 5, "moon", 23, "table", "sun", 8}
element = "banana"
try:
    print(random_set.remove(element))
except KeyError:
    print('element not in set')
