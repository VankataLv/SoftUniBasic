n = int(input())  # total amount of numbers [1 : 1000]
c1 = c2 = c3 = c4 = c5 = 0  # count of numbers in each of the 5 categories
p1 = p2 = p3 = p4 = p5 = 0

for i in range(0, n):
    current_num = int(input())
    if current_num < 200:
        c1 += 1
    elif 200 <= current_num <= 399:
        c2 += 1
    elif 400 <= current_num <= 599:
        c3 += 1
    elif 600 <= current_num <= 799:
        c4 += 1
    else:  # current_num >= 800
        c5 += 1

p1 = c1/n * 100
print("%.2f" % p1 + "%")
p2 = c2/n * 100
print("%.2f" % p2 + "%")
p3 = c3/n * 100
print("%.2f" % p3 + "%")
p4 = c4/n * 100
print("%.2f" % p4 + "%")
p5 = c5/n * 100
print("%.2f" % p5 + "%")
