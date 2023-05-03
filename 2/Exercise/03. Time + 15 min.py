h = int(input())
m = int(input())

m += 15

if m > 59:
    m -= 60
    h += 1
    if h > 23:
        h -= 24
    if m >= 10:
        print(f'{h}:{m}')
    else:
        print(f'{h}:0{m}')
elif m == 60:
    h += 1
    m = 0
    if h > 23:
        h -= 24
        print(f'{h}:{m}')
    else:
        print(f'{h}:0{m}')
else:
    print(f'{h}:{m}')
