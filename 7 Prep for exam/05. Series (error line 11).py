budget = float(input())
actor_name = input()
actor_price = 0
budget_left = budget
money_spent_sofar = current_budget = 0

while actor_name != "ACTION":
    if len(actor_name) > 15:
        actor_price = 0.2 * budget_left
    else:
        actor_price = float(input())

    budget_left -= actor_price
    actor_price = 0

    if budget_left < 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        quit()

    else:
        actor_name = input()

if actor_name == "ACTION":
    print(f"We are left with {budget_left} leva.")
    quit()
else:
    print(f"We are left with {budget_left} leva.")