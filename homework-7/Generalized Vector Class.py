import math
class Vector:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
    
    def __add__(self, other):
        addition = self.a + other.a, self.b + other.b, self.c + other.c
        return addition
    
    def __sub__(self, other):
        subtraction = self.a - other.a, self.b - other.b, self.c - other.c
        return subtraction

    def __mul__(self, other):
        dot_product = self.a * other.a + self.b * other.b + self.c * other.c
        return dot_product
    
    def __rmul__(self, other):
        return Vector(self.a * other, self.b * other, self.c * other)

    def magnitude(self):
        mag = (math.sqrt(self.a*self.a + self.b*self.b + self.c*self.c))
        return mag
    
    def normalize(self):
        mag = math.sqrt(self.a*self.a + self.b*self.b + self.c*self.c)
        a = math.floor(self.a/mag * 1000) / 1000
        b = math.floor(self.b/mag * 1000) / 1000
        c = math.floor(self.c/mag * 1000) / 1000
        return Vector(a, b, c)


# Create vectors
u1 = Vector(7, 8, 9)
u2 = Vector(1, 0, -1)

# Print the vector
print(u1)          # Output: Vector(7, 8, 9)

# Addition
u3 = u1 + u2
print(u3)          # Output: Vector(8, 8, 8)

# Subtraction
u4 = u1 - u2
print(u4)          # Output: Vector(6, 8, 10)

# Dot product
dot_u = u1 * u2
print(dot_u)       # Output: -2  (7*1 + 8*0 + 9*(-1) = 7 + 0 - 9)

# Scalar multiplication
u5 = 2 * u2
print(u5)          # Output: Vector(2, 0, -2)

# Magnitude
print(u2.magnitude())  # Output: 1.4142135623730951

# Normalization
u_unit = u2.normalize()
print(u_unit)      # Output: Vector(0.707, 0.0, -0.707)
