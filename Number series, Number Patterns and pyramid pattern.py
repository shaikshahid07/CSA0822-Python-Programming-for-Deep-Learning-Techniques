# Fibonacci Series (Number Series)
n = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()

# Number Pattern (Increasing Numbers)
n = int(input("Enter number of rows for number pattern: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Pyramid Pattern (Star Pattern)
n = int(input("Enter number of rows for pyramid pattern: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
