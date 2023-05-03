qty_joinery = int(input())
size_joinery = input()
type_delivery = input()
total_price = 0
price_for_one = 0
if qty_joinery <= 10:
    print("Invalid order")
    quit()

if size_joinery == "90X130":
    price_for_one = 110
    if 60 >= qty_joinery > 30:
        price_for_one *= 0.95
    if qty_joinery > 60:
        price_for_one *= 0.92
elif size_joinery == "100X150":
    price_for_one = 140
    if 80 >= qty_joinery > 40:
        price_for_one *= 0.94
    elif qty_joinery > 80:
        price_for_one *= 0.90
elif size_joinery == "130X180":
    price_for_one = 190
    if 50 >= qty_joinery > 20:
        price_for_one *= 0.93
    elif qty_joinery > 50:
        price_for_one *= 0.88
else:
    price_for_one = 250
    if 50 >= qty_joinery > 25:
        price_for_one *= 0.91
    elif qty_joinery > 50:
        price_for_one *= 0.86

total_price = price_for_one * qty_joinery
if type_delivery == "With delivery":
    total_price += 60
if qty_joinery > 99:
    total_price *= 0.96

print(f"{total_price:.2f} BGN")