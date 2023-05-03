n = int(input())


def print_triangle(num):
    for i in range(1, num + 1):  # The first for cycle usually controls the number of rows
        for j in range(1, i+1):
            print(f'{j} ', end='')
        print()

    for i in range(num-1,0 , -1):
        for j in range(1, i+1):
            print(f'{j} ', end="")
        print()


print_triangle(n)
