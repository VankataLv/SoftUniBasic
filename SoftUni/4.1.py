h = int(input())
x = int(input())
y = int(input())

if x < 0 or y < 0:
    print("outside")
else:
    if x >= 0 and x <= 3*h and y >= 0 and y <= h:
        if x == 0 or x == 3*h or y == 0 or y == h:
            print("border")
        else:
            print("inside")
    elif (x >= h and x <= 2*h) and (y >= h and y <= 4*h):
        if (x == h or x == 2*h) or (y == 4*h or y == h):
            print("border")
        else:
            print("inside")
    else:
        print("outside")
