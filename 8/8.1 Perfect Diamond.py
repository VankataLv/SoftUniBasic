n = int(input())
for i in range(1, n + 1):
    print(' ' * (n - i) + '*', end="")

    for j in range(0, i-1):
        print('-*', end="")

    print()        # one line/row down

for i in range(1, n):
    print((" " * i) + "*", end="")
    for j in reversed(range(1, n - i)):        # j is 2,1 if n is 4 because n-1 is excluded(non-inclusive)
        print('-*', end="")
    print()
