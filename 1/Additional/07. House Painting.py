x = float(input())
y = float(input())
h = float(input())
paint_green = 3.4
paint_red = 4.3

s_ceil_triangle = 2 * ((x * h) / 2)
s_ceil_rect = 2 * (x * y)
s_ceil = s_ceil_triangle + s_ceil_rect

s_front = (x * x) - (1.2 * 2)
s_back = x * x
s_side = 2 * ((x * y) - (1.5 * 1.5))
s_floor = s_front + s_back + s_side

green_need = s_floor / paint_green
red_need = s_ceil / paint_red

print("%.2f" % green_need)
print("%.2f" % red_need)
