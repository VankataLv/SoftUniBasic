first = int(input())
second = int(input())
point = int(input())

left = min(first, second)
right = max(first, second)

a = abs(first - second)

dis_left = abs(left - point)
dis_right = abs(right - point)
min_dis = min(dis_left, dis_right)

if left <= point <= right:
    print("in")
else:
    print("out")

print(f'{min_dis}')
