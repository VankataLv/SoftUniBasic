trip_price = float(input())
puzzle_amount = int(input())
doll_amount = int(input())
bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

money_earned = (puzzle_price * puzzle_amount) + (doll_price * doll_amount) + (bear_price * bear_amount) + (
            minion_price * minion_amount) + (truck_price * truck_amount)

if (puzzle_amount + doll_amount + bear_amount + minion_amount + truck_amount) >= 50:
    money_earned *= 0.75
money_earned *= 0.9

if money_earned >= trip_price:
    print(f'Yes! {(money_earned - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - money_earned):.2f} lv needed.')
