drink_type = input()
sugar_choice = input()
qty_drink = int(input())
price_drink = total_cost = 0
if drink_type == "Espresso":
    if sugar_choice == "Without":
        price_drink = 0.9
    elif sugar_choice == "Normal":
        price_drink = 1
    elif sugar_choice == "Extra":
        price_drink = 1.2
elif drink_type == "Cappuccino":
    if sugar_choice == "Without":
        price_drink = 1
    elif sugar_choice == "Normal":
        price_drink = 1.2
    elif sugar_choice == "Extra":
        price_drink = 1.6
elif drink_type == "Tea":
    if sugar_choice == "Without":
        price_drink = 0.5
    elif sugar_choice == "Normal":
        price_drink = 0.6
    elif sugar_choice == "Extra":
        price_drink = 0.7

if sugar_choice == "Without":
    price_drink *= 0.65

if drink_type == "Espresso" and qty_drink >= 5:
    price_drink *= 0.75

total_cost = price_drink * qty_drink
if total_cost > 15:
    total_cost *= 0.8

print(f"You bought {qty_drink} cups of {drink_type} for {total_cost:.2f} lv.")