import math

figure_type = input()

if figure_type == "square":
    a = float(input())
    print(f'{a * a:.3f}')
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    print(f'{a * b:.3f}')
elif figure_type == "circle":
    a = float(input())
    print(f'{math.pi * (a**2):.3f}')
elif figure_type == "triangle":
    a = float(input())
    h = float(input())
    print(f'{(a * h) / 2:.3f}')
