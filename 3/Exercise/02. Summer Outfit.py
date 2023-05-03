degrees = int(input())
time_day = input()
outfit = ()
shoes = ()

if 10 <= degrees <= 18 and time_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif 10 <= degrees <= 18 and time_day == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 10 <= degrees <= 18 and time_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < degrees <= 24 and time_day == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"
elif 18 < degrees <= 24 and time_day == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif 18 < degrees <= 24 and time_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif degrees >= 25 and time_day == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"
elif degrees >= 25 and time_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
else:
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

