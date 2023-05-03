destination = input()
dates_reservation = input()
nights = int(input())

price_per_night = total_cost = 0

if destination == "France":
    if dates_reservation == "21-23":
        price_per_night = 30
    elif dates_reservation == "24-27":
        price_per_night = 35
    else:
        price_per_night = 40
elif destination == "Italy":
    if dates_reservation == "21-23":
        price_per_night = 28
    elif dates_reservation == "24-27":
        price_per_night = 32
    else:
        price_per_night = 39
elif destination == "Germany":
    if dates_reservation == "21-23":
        price_per_night = 32
    elif dates_reservation == "24-27":
        price_per_night = 37
    else:
        price_per_night = 43
total_cost = price_per_night * nights
print(f"Easter trip to {destination} : {total_cost:.2f} leva.")
