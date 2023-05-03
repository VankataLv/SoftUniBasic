a = int(input())
b = int(input())
c = int(input())

highest = max(a, b, c)

if a+b == highest:
    lowest = min(a, b)
    middle = max(a, b)
    print(f'{lowest} + {middle} = {highest}')
elif a+c == highest:
    lowest = min(a, c)
    middle = max(a, c)
    print(f'{lowest} + {middle} = {highest}')
elif c+b == highest:
    lowest = min(c, b)
    middle = max(c, b)
    print(f'{lowest} + {middle} = {highest}')
else:
    print("No")
