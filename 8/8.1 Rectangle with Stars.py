from math import floor
n = int(input())

print("%" * (n*2))

num_rows = n
if num_rows % 2 == 0:
    num_rows += -1

for i in range(0, num_rows):
    print("%", end='')
    if i == floor(num_rows)/2):
        print ????????????????
    print("%")

print("%" * (n*2))