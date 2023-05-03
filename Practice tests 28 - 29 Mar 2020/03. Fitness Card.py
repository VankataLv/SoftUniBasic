money_wallet = float(input())
sex = input()
age = int(input())
sport = input()
money_needed = 0

if sex == "m":
    if sport == "Gym":
        money_needed = 42
    elif sport == "Boxing":
        money_needed = 41
    elif sport == "Yoga":
        money_needed = 45
    elif sport == "Zumba":
        money_needed = 34
    elif sport == "Dances":
        money_needed = 51
    elif sport == "Pilates":
        money_needed = 39
else:
    if sport == "Gym":
        money_needed = 35
    elif sport == "Boxing":
        money_needed = 37
    elif sport == "Yoga":
        money_needed = 42
    elif sport == "Zumba":
        money_needed = 31
    elif sport == "Dances":
        money_needed = 53
    elif sport == "Pilates":
        money_needed = 37

if age <= 19:
    money_needed = money_needed * 0.8

if money_needed <= money_wallet:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f"You don't have enough money! You need ${(money_needed - money_wallet):.2f} more.")