budget = float(input())
season = input()
destination = ()
lodging = ()
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = budget * 0.3
        lodging = "Camp"
    else:
        money_spent = budget * 0.7
        lodging = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = budget * 0.4
        lodging = "Camp"
    else:
        money_spent = budget * 0.8
        lodging = "Hotel"
else:
    destination = "Europe"
    money_spent = budget * 0.9
    lodging = "Hotel"

print(f'Somewhere in {destination}')
print(f'{lodging} - {money_spent:.2f}')