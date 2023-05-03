destination = input()
min_budget = float(input())
new_command = 0

while destination != "End":
    new_command = float(input())
    min_budget -= new_command
    if min_budget <= 0:
        print(f"Going to {destination}!")
        destination = input()
        if destination == "End":
            quit()
        min_budget = float(input())
quit()
