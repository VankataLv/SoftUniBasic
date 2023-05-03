flower_type = input()
number_flower = int(input())
budget = int(input())
flower_price = 0

if flower_type == "Roses":
    if number_flower > 80:
        flower_price = 5 * 0.9
    else:
        flower_price = 5

if flower_type == "Dahlias":
    if number_flower > 90:
        flower_price = 3.8 * 0.85
    else:
        flower_price = 3.8

if flower_type == "Tulips":
    if number_flower > 80:
        flower_price = 2.8 * 0.85
    else:
        flower_price = 2.8

if flower_type == "Narcissus":
    if number_flower < 120:
        flower_price = 3 * 1.15
    else:
        flower_price = 3

if flower_type == "Gladiolus":
    if number_flower < 80:
        flower_price = 2.5 * 1.20
    else:
        flower_price = 2.5

if budget >= flower_price * number_flower:
    print(f'Hey, you have a great garden with {number_flower} {flower_type} and \
{budget - (flower_price * number_flower):.2f} leva left.')
else:
    print(f'Not enough money, you need {flower_price * number_flower - budget:.2f} leva more.')
