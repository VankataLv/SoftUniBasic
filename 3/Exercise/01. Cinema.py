type_film = input()
r = int(input())
c = int(input())
capacity = r * c
price = 0

if type_film == "Premiere":
    price = 12
elif type_film == "Normal":
    price = 7.5
else:
    price = 5

print(f'{capacity * price:.2f} leva')
