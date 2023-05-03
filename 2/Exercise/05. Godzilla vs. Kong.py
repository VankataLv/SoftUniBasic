budget = float(input())
statists = int(input())
price_costume = float(input())
decor_price = budget * 0.1

if statists > 150:
    price_costume *= 0.9

total_costume = price_costume * statists
if budget < (total_costume + decor_price):
    print(f'Not enough money!')
    print(f'Wingard needs {((total_costume + decor_price) - budget):.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {(budget - (total_costume + decor_price)):.2f} leva left.')
