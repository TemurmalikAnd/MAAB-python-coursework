#Make a program that converts a given Celsius temperature to Fahrenheit.
try:
    celsius = int(input("Enter a Celsius temperature: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
except ValueError:
    print("Please enter a valid number.")
