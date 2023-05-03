month_stay = input()
nights = int(input())
total_studio_price = total_app_price = 0

if month_stay == "May" or month_stay == "October":
    total_studio_price = 50 * nights
    total_app_price = 65 * nights
    if 7 < nights <= 14:
        total_studio_price *= 0.95
    elif nights > 14:
        total_studio_price *= 0.7
elif month_stay == "June" or month_stay == "September":
    total_studio_price = 75.2 * nights
    total_app_price = 68.7 * nights
    if nights > 14:
        total_studio_price *= 0.8
else:
    total_studio_price = 76 * nights
    total_app_price = 77 * nights

if nights > 14:
    total_app_price *= 0.9

print(f"Apartment: {total_app_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
