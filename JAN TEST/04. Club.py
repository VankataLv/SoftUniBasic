profit_wanted = float(input())
name_cocktail = input()
amount_cocktail = 0
total_earned = current_order = 0
price_cocktail = 0

while name_cocktail != "Party!":
    amount_cocktail = int(input())
    price_cocktail = len(name_cocktail)
    current_order = 0
    current_order += price_cocktail * amount_cocktail

    if current_order % 2 == 0:
        total_earned += current_order
    else:
        total_earned += current_order * 0.75

    if profit_wanted <= total_earned:
        print("Target acquired.")
        break

    name_cocktail = input()

    if name_cocktail == "Party!":
        print(f'We need {profit_wanted - total_earned:.2f} leva more.')
        break

print(f'Club income - {total_earned:.2f} leva.')
