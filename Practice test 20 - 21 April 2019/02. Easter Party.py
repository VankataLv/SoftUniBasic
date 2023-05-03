guests = int(input())
price_per_guest = float(input())
budget = float(input())

total_cost_guest = price_per_guest * guests
if 10 <= guests <= 15:
    total_cost_guest *= 0.85
elif 15 < guests <= 20:
    total_cost_guest *= 0.8
elif guests > 20:
    total_cost_guest *= 0.75

total_cost = total_cost_guest + (budget * 0.1)

if budget >= total_cost:
    print(f"It is party time! {budget - total_cost:.2f} leva left.")
else:
    print(f"No party! {total_cost - budget:.2f} leva needed.")

