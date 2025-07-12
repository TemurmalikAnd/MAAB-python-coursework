def check(funk):
    def wrapper(a, b):  # wrapper now accepts a and b
        if b == 0:
            print("Denominator can't be zero") # More descriptive message
            return None
        return funk(a, b) # Pass a and b to the original function
    return wrapper
@check
def div(a, b):
    return a / b
user_input = input('Input: ')
user_input = list(user_input.replace("div(", "").replace(")", "").replace(",", "").replace(" ", ""))

strip_results = list(map(int, user_input))
a = strip_results[0]
b = strip_results[1]
result1 = div(a, b)
print(result1)