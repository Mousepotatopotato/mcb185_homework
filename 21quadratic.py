import math
def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

print(quadratic(1, 2, 1))
print(quadratic(1, 6, 1))
print(quadratic(2, 4, 1))
print(quadratic(1, 6, 8))
print(quadratic(5, 18, 4))