eggs_store = int(input())
order = input()
change_eggs = int(input())
eggs_sold = 0

while order != "Close":
    if order == "Buy":
        if change_eggs > eggs_store:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_store}.")
            quit()
        else:
            eggs_store -= change_eggs
            eggs_sold += change_eggs
    if order == "Fill":
        eggs_store += change_eggs
    order = input()
    if order == "Close":
        print(f"Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        quit()
    change_eggs = int(input())
