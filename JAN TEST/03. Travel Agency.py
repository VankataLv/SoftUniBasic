price_day = 0
city = input()
package_type = input()
vip_status = input()
days = int(input())

if city == "Bansko" or city == "Borovets":
    if package_type == "withEquipment":
        if vip_status == "yes":
            price_day = 100 * 0.9
        else:
            price_day = 100
    elif package_type == "noEquipment":
        if vip_status == "yes":
            price_day = 80 * 0.95
        else:
            price_day = 80
    else:
        print(f'Invalid input!')

elif city == "Varna" or city == "Burgas":
    if package_type == "withBreakfast":
        if vip_status == "yes":
            price_day = 130 * 0.88
        else:
            price_day = 130
    elif package_type == "noBreakfast":
        if vip_status == "yes":
            price_day = 100 * 0.93
        else:
            price_day = 100
    else:
        print(f'Invalid input!')
else:
    print(f'Invalid input!')
    quit()

if days < 1:
    print(f'Days must be positive number!')
    quit()
if days > 7:
    days -= 1

total_price = days * price_day

print(f"The price is {total_price:.2f}lv! Have a nice time!")
