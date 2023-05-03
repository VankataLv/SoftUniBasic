change = float(input())
coins = 0
change = change * 100

for x in (200, 100, 50, 20, 10, 5, 2):
    currCoins = int(change / x)
    change -= currCoins * x
    coins += currCoins

currCoins = int(change)
coins += currCoins

print(coins)
