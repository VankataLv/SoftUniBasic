import math


length = float(input())  # daljina v metri
width = float(input())  # shirana v metri

length_cm = length * 100
width_cm = width * 100

rows_fit = math.floor((width_cm - 100) / 70)
columns_fit = math.floor(length_cm / (80 + 40))

desks_fit = (rows_fit * columns_fit) - 3
print(desks_fit)
