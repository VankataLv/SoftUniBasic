import math
x = int(input())
w = int(input())
m = int(input())

courses = x/(w*m)

print(f'{math.ceil(courses)}')
