from math import ceil


total_pax = int(input())
ticket_price = float(input())
bed_price = float(input())
umbrella_price = float(input())

entry_total = total_pax * ticket_price

umbrella_needed = ceil(total_pax / 2)
umbrella_total = umbrella_price * umbrella_needed

bed_needed = ceil(total_pax * 0.75)
bed_total = bed_needed * bed_price

total_cost = entry_total + umbrella_total + bed_total

print(f'{total_cost:.2f} lv.')
