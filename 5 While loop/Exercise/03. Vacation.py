holiday_money_needed = float(input())
account_balance = float(input())
days_spend_counter = days_counter = 0

while holiday_money_needed > account_balance:
    type_action = input()
    action_amount = float(input())
    days_counter += 1
    if type_action == "spend":                      # case: spend
        if account_balance - action_amount < 0:     # case: spend + more money spent that balance
            account_balance = 0
        else:                                       # case: spend + enough money in balance
            account_balance -= action_amount
        days_spend_counter += 1
        if days_spend_counter == 5:                 # case: spend 5 consecutive days
            print("You can't save the money.")
            print(days_counter)
            quit()
    else:                                           # case = save
        account_balance += action_amount
        days_spend_counter = 0

else:
    print(f"You saved the money for {days_counter} days.")
