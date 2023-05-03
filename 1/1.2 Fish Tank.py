l = int(input())
w = int(input())
h = int(input())
percentage = float(input()) / 100

v = l * w * h
v_litres = v * 0.001
water_needed = v_litres * (1 - percentage)
print(water_needed)
