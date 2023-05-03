tabs_opened = int(input())
wages = float(input())
website = ()

for i in range(1, tabs_opened + 1):

    website = input()
    if website == "Facebook":
        wages -= 150
    elif website == "Instagram":
        wages -= 100
    elif website == "Reddit":
        wages -= 50

    if wages <= 0:
        print(f"You have lost your salary.")
        quit()
print(int(wages))