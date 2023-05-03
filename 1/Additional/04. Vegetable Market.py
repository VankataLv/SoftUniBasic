price_veg = float(input())
price_fruit = float(input())
veg_kg = int(input())
fruit_kg = int(input())

profit = ((price_veg * veg_kg) + (price_fruit * fruit_kg)) / 1.94

print("%.2f" % profit)
