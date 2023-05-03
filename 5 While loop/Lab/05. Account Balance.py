account_balance = 0
current_input = input()
while current_input != "NoMoreMoney":
    amount = float(current_input)
    if amount < 0:
        print("Invalid operation!")
        break
    account_balance += amount
    print(f"Increase: {amount:.2f}")
    current_input = input()
print(f"Total: {account_balance:.2f}")
