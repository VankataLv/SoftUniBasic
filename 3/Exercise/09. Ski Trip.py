nights = int(input()) - 1
type_room = input()
grade = input()
price_room = total_price = 0

if nights < 10:
    if type_room == "room for one person":
        price_room = 18
    elif type_room == "apartment":
        price_room = 25 * 0.7
    else:
        price_room = 35 * 0.9
elif 10 <= nights <= 15:
    if type_room == "room for one person":
        price_room = 18
    elif type_room == "apartment":
        price_room = 25 * 0.65
    else:
        price_room = 35 * 0.85
else:
    if type_room == "room for one person":
        price_room = 18
    elif type_room == "apartment":
        price_room = 25 * 0.5
    else:
        price_room = 35 * 0.8

total_price = price_room * nights
if grade == "positive":
    total_price *= 1.25
else:
    total_price *= 0.9

print(f"{total_price:.2f}")
