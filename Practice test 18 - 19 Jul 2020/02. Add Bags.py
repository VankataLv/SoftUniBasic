price_add_luggage = float(input())
kg_luggage = float(input())
days = int(input())
qty_luggage = int(input())

if kg_luggage < 10:
    price_add_luggage *= 0.2
elif 10 <= kg_luggage <= 20:
    price_add_luggage *= 0.5

if days > 30:
    price_add_luggage *= 1.1
elif 7 <= days <= 30:
    price_add_luggage *= 1.15
elif days < 7:
    price_add_luggage *= 1.4

total_increase = price_add_luggage * qty_luggage

print(f"The total price of bags is: {total_increase:.2f} lv. ")
