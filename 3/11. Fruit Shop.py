days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fruit = input()
day = input()
quantity = float(input())
price = 0
error = bool

if day not in days_of_week:
    print("error")
    quit()

if fruit == "banana":
    if day == "Saturday" or day == "Sunday":
        price = 2.7
    else:
        price = 2.5
elif fruit == "apple":
    if day == "Saturday" or day == "Sunday":
        price = 1.25
    else:
        price = 1.2
elif fruit == "orange":
    if day == "Saturday" or day == "Sunday":
        price = 0.9
    else:
        price = 0.85
elif fruit == "grapefruit":
    if day == "Saturday" or day == "Sunday":
        price = 1.6
    else:
        price = 1.45
elif fruit == "kiwi":
    if day == "Saturday" or day == "Sunday":
        price = 3
    else:
        price = 2.7
elif fruit == "pineapple":
    if day == "Saturday" or day == "Sunday":
        price = 5.6
    else:
        price = 5.5
elif fruit == "grapes":
    if day == "Saturday" or day == "Sunday":
        price = 4.2
    else:
        price = 3.85
else:
    error = True

if error is True:
    print("error")
else:
    print(f'{price * quantity:.2f}')
