budget = float(input())
nights = int(input())
price_night = float(input())
additional_expenses = (int(input())) / 100

if nights > 7:
    price_night *= 0.95

total_cost = (nights * price_night) + (budget * additional_expenses)

if budget >= total_cost:
    print(f'Ivanovi will be left with {(budget - total_cost):.2f} leva after vacation.')
else:
    print(f'{total_cost - budget:.2f} leva needed.')
