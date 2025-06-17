a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)


x = int(input("\nEnter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))
print("Before circulation: x =", x, "y =", y, "z =", z)
x, y, z = z, x, y
print("After circulation: x =", x, "y =", y, "z =", z)


x1 = float(input("\nEnter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
import math
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points:", d)
