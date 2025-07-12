def convert_far_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def convert_cel_to_far(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Main code handles input/output
temp_f = float(input('Enter a temperature in degrees F: '))
converted_c = convert_far_to_cel(temp_f)
print(f"{temp_f} degrees F = {converted_c:.2f} degrees C")

print()

temp_c = float(input('Enter a temperature in degrees C: '))
converted_f = convert_cel_to_far(temp_c)
print(f"{temp_c} degrees C = {converted_f:.2f} degrees F")