a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)

print("GCD is:", gcd(a, b))
print("LCM is:", lcm(a, b))
