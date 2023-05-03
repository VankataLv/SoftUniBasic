d = int(input())
m = int(input())
max_days_month = ()

if m == 4 or m == 6 or m == 9 or m == 11:
    max_days_month = 30
elif m == 2:
    max_days_month = 28
else:
    max_days_month = 31

d += 5

if d > max_days_month:
    m += 1
    d = d - max_days_month

if m > 12:
    m = 1

if 1 <= m <= 9:
    print(f'{d}.0{m}')
else:
    print(f'{d}.{m}')

# print('%d.%02d' % (d, m))
