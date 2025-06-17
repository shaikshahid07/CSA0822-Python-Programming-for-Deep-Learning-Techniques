a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("\nBefore Swapping:")
print("a =", a, "b =", b)
temp = a
a = b
b = temp
print("\nAfter Swapping (using temp variable):")
print("a =", a, "b =", b)


x = int(input("\nEnter new value of x: "))
y = int(input("Enter new value of y: "))
print("\nBefore Swapping:")
print("x =", x, "y =", y)
x = x + y
y = x - y
x = x - y
print("\nAfter Swapping (without temp variable):")
print("x =", x, "y =", y)
