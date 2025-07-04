"""

# For Loop vs While Loop - Complete Guide

A **for loop** and **while loop** are both used for repetition, but they serve different purposes and have distinct structures.

## For Loop
A for loop is best when you know how many times you want to repeat something or when iterating through a collection. It has a clear initialization, condition, and increment/decrement built into its structure.

**Structure:**
```python
for variable in range(start, stop, step):
    # code to execute
```

**Example:**
```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(f"Number: {i}")

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
```

## While Loop
A while loop continues executing as long as a condition remains true. It's ideal when you don't know exactly how many iterations you'll need, or when the loop should continue based on changing conditions.

**Structure:**
```python
while condition:
    # code to execute
    # usually includes something that changes the condition
```

**Example:**
```python
# Keep asking for input until user enters "quit"
user_input = ""
while user_input != "quit":
    user_input = input("Enter a word (or 'quit' to exit): ")
    if user_input != "quit":
        print(f"You entered: {user_input}")
```

## Key Differences

**When to use for loops:**
- Counting through a specific range
- Iterating through lists, strings, or other collections
- When you know the number of iterations in advance

**When to use while loops:**
- Repeating until a condition is met
- Reading input until a specific value
- Game loops that continue until the game ends
- When the number of iterations is unknown

## Comparison Example

```python
# Using for loop to sum numbers 1-10
total = 0
for i in range(1, 11):
    total += i
print(f"Sum using for loop: {total}")

# Using while loop to sum numbers 1-10
total = 0
i = 1
while i <= 10:
    total += i
    i += 1  # Important: increment to avoid infinite loop
print(f"Sum using while loop: {total}")
```

## Additional Examples

### For Loop Examples
```python
# Iterate through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterate through a string
word = "Python"
for letter in word:
    print(letter)

# Using enumerate to get index and value
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index + 1}. {name}")
```

### While Loop Examples
```python
# Countdown timer
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

# Finding a number in a list
numbers = [3, 7, 2, 9, 1, 5]
target = 9
index = 0
found = False

while index < len(numbers) and not found:
    if numbers[index] == target:
        found = True
        print(f"Found {target} at index {index}")
    else:
        index += 1

if not found:
    print(f"{target} not found in the list")
```

## Important Notes

**For While Loops:**
- Always ensure the condition eventually becomes false to avoid infinite loops
- Remember to update the variable that controls the condition
- Use when the number of iterations is unknown or depends on user input/external conditions

**For For Loops:**
- Python's for loops are actually "for-each" loops that iterate over collections
- Use `range()` function for numeric iterations
- More concise and less error-prone for known iterations

## Common Pitfalls

**Infinite While Loop (AVOID):**
```python
# This will run forever!
count = 1
while count > 0:
    print("This will never stop")
    # Missing: count -= 1 or similar condition change
```

**Correct While Loop:**
```python
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1  # This ensures the loop will eventually end
```
"""

numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)