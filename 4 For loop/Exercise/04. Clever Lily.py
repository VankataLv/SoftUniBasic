age = int(input())
laundry_machine_price = float(input())
toy_price = float(input())
toy_count = sum_saved = even_year_count = 0
for year in range(1, age + 1):
    if year % 2 == 1:
        toy_count += 1
    if year % 2 == 0:
        even_year_count += 1
        sum_saved += 10 * even_year_count

sum_saved += toy_count * toy_price
sum_saved -= 1 * even_year_count

if sum_saved >= laundry_machine_price:
    print(f'Yes! {sum_saved - laundry_machine_price:.2f}')
else:
    print(f'No! {laundry_machine_price - sum_saved:.2f}')
