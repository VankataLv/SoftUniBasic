import math
a = int(input())
b = int(input())
c = int(input())

total_time = a + b + c
minutes = math.floor(total_time // 60)
seconds = total_time % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
