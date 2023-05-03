num = int(input())
bonus_point, additional_bouns = 0 , 0

if num <= 100:
    bonus_point = 5
elif num <= 1000:
    bonus_point = num * 0.2
elif 1000 < num:
    bonus_point = num * 0.1

if num % 2 == 0:
    additional_bouns += 1

if num % 10 == 5:
    additional_bouns += 2

print(bonus_point + additional_bouns)
print(bonus_point + additional_bouns + num)
