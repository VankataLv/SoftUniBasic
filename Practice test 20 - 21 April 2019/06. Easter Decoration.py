price_basket = 1.5
price_wreath = 3.8
price_bunny = 7
customer_count = int(input())
current_client_bill = total_bill_store = 0
purchase = ""
purchase_count = 0

for customer in range(1, customer_count + 1):
    purchase = input()
    while purchase != "Finish":
        if purchase == "basket":
            current_client_bill += price_basket
            purchase_count += 1
        elif purchase == "wreath":
            current_client_bill += price_wreath
            purchase_count += 1
        elif purchase == "chocolate bunny":
            current_client_bill += price_bunny
            purchase_count += 1
        purchase = input()
    else:
        if purchase_count % 2 == 0:
            current_client_bill *= 0.8
        total_bill_store += current_client_bill
        print(f'You purchased {purchase_count} items for {current_client_bill:.2f} leva.')
        purchase_count = 0
        current_client_bill = 0

print(f"Average bill per client is: {total_bill_store / customer_count:.2f} leva.")
