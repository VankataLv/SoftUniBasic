fruit = input()
set_type = input()
amount_sets_ordered = int(input())

if fruit == "Watermelon":
    if set_type == "big":
        total_cost = (5 * 28.70) * amount_sets_ordered
    else:
        total_cost = (2 * 56.00) * amount_sets_ordered

elif fruit == "Mango":
    if set_type == "big":
        total_cost = (5 * 19.60) * amount_sets_ordered
    else:
        total_cost = (2 * 36.66) * amount_sets_ordered

elif fruit == "Pineapple":
    if set_type == "big":
        total_cost = (5 * 24.80) * amount_sets_ordered
    else:
        total_cost = (2 * 42.10) * amount_sets_ordered

else:
    if set_type == "big":
        total_cost = (5 * 15.20) * amount_sets_ordered
    else:
        total_cost = (2 * 20.00) * amount_sets_ordered


if 400 <= total_cost <= 1000:
    total_cost_discount = total_cost * 0.85
elif total_cost > 1000:
    total_cost_discount = total_cost * 0.5
else:
    total_cost_discount = total_cost

print(f'{total_cost_discount:.2f} lv.')
