from math import ceil
pies_qty = int(input())
total_sugar = total_flour = 0
max_sugar = max_flour = current_sugar = current_flour = 0
sugar_per_packet = 950
flour_per_packet = 750

for pie in range(0, pies_qty):
    current_sugar = int(input())
    current_flour = int(input())
    total_sugar += current_sugar
    total_flour += current_flour

    if current_sugar > max_sugar:
        max_sugar = current_sugar
    if current_flour > max_flour:
        max_flour = current_flour

print(f'Sugar: {ceil(total_sugar / sugar_per_packet)}\n'
      f'Flour: {ceil(total_flour / flour_per_packet)}\n'
      f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')

