def find_factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def find_largest(lst):
    big = lst[0]
    for num in lst:
        if num > big:
            big = num
    return big

def find_area(shape):
    if shape == "circle":
        r = float(input("Enter radius: "))
        return 3.14 * r * r
    elif shape == "rectangle":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        return l * w
    elif shape == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        return 0.5 * b * h
    else:
        return "Invalid shape"

num = int(input("Enter a number to find factorial: "))
print("Factorial is:", find_factorial(num))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number is:", find_largest(numbers))

shape = input("Enter shape (circle/rectangle/triangle): ")
print("Area is:", find_area(shape))
