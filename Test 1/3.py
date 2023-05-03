nights = int(input()) - 1
type_room = str(input())
review = str(input())

price_per_night = 0

if type_room == "room for one person":
    if nights < 10:
        price_per_night = 18
    elif 10 <= nights <= 15:
        price_per_night = 18
    elif nights > 15:
        price_per_night = 18
elif type_room == "apartment":
    if nights < 10:
        price_per_night = 25 * 0.7
    elif 10 <= nights <= 15:
        price_per_night = 25 * 0.65
    elif nights > 15:
        price_per_night = 25 * 0.5
elif type_room == "president apartment":
    if nights < 10:
        price_per_night = 35 * 0.9
    elif 10 <= nights <= 15:
        price_per_night = 35 * 0.85
    elif nights > 15:
        price_per_night = 35 * 0.8

money_to_pay = price_per_night * nights

if review == "positive":
    money_to_pay *= 1.25
else:
    money_to_pay *= 0.9

print(f"{money_to_pay:.2f}")
