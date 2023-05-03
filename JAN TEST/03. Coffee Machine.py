drink_type = input()
sugar_amount = input()
drink_amount = int(input())
total_cost = 0

if drink_type == "Espresso":
    if sugar_amount == "Without":
        total_cost = (drink_amount * 0.9)
    elif sugar_amount == "Normal":
        total_cost = (drink_amount * 1)
    else:
        total_cost = (drink_amount * 1.2)

if drink_type == "Cappuccino":
    if sugar_amount == "Without":
        total_cost = (drink_amount * 1)
    elif sugar_amount == "Normal":
        total_cost = (drink_amount * 1.2)
    else:
        total_cost = (drink_amount * 1.6)

if drink_type == "Tea":
    if sugar_amount == "Without":
        total_cost = (drink_amount * 0.5)
    elif sugar_amount == "Normal":
        total_cost = (drink_amount * 0.6)
    else:
        total_cost = (drink_amount * 0.7)

if sugar_amount == "Without":
    total_cost *= 0.65

if drink_type == "Espresso":
    if drink_amount >= 5:
        total_cost *= 0.75

if total_cost > 15:
    total_cost *= 0.8

print(f'You bought {drink_amount} cups of {drink_type} for {total_cost:.2f} lv.')
