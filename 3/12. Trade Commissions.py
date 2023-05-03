city = str(input())
s = float(input())
commission = 0
if (city == "Sofia" or city == "Varna" or city == "Plovdiv") and s >= 0:
    if city == "Sofia":
        if 0 <= s <= 500:
            commission = 5
        elif 500 < s <= 1000:
            commission = 7
        elif 1000 < s <= 10000:
            commission = 8
        else:
            commission = 12
    elif city == "Varna":
        if 0 <= s <= 500:
            commission = 4.5
        elif 500 < s <= 1000:
            commission = 7.5
        elif 1000 < s <= 10000:
            commission = 10
        else:
            commission = 13
    else:
        if 0 <= s <= 500:
            commission = 5.5
        elif 500 < s <= 1000:
            commission = 8
        elif 1000 < s <= 10000:
            commission = 12
        else:
            commission = 14.5
else:
    print("error")
    quit()

commission /= 100
print(f"{commission * s:.2f}")
