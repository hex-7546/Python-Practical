#for creating a pyramid
n = int(input("Enter no of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

#for creating a reverse pyramid
n = int(input("Enter no of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
