product = input()
city = input()
amount = float(input())
price = 0

if product == "coffee":
    if city == "Sofia":
        price = 0.5
    elif city == "Plovdiv":
        price = 0.4
    else:  # city == "Varna"
        price = 0.45
elif product == "water":
    if city == "Sofia":
        price = 0.8
    elif city == "Plovdiv":
        price = 0.7
    else:  # city == "Varna"
        price = 0.7
elif product == "beer":
    if city == "Sofia":
        price = 1.2
    elif city == "Plovdiv":
        price = 1.15
    else:  # city == "Varna"
        price = 1.1
elif product == "sweets":
    if city == "Sofia":
        price = 1.45
    elif city == "Plovdiv":
        price = 1.3
    else: # city == "Varna"
        price = 1.35
else:  # product == "peanuts"
    if city == "Sofia":
        price = 1.60
    elif city == "Plovdiv":
        price = 1.5
    else:  # city == "Varna"
        price = 1.55

print(f"{price * amount}")
