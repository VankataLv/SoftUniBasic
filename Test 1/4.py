amount_pc = int(input())
rating = 0
percent_sales = 0
total_sales_made = 0
current_sales = 0
possible_sales = 0
total_sum_ratings = 0

for pc_model in range(1, amount_pc + 1):
    special_num = int(input())
    rating = special_num % 10
    if rating == 2:
        percent_sales = 0
    elif rating == 3:
        percent_sales = 0.5
    elif rating == 4:
        percent_sales = 0.7
    elif rating == 5:
        percent_sales = 0.85
    elif rating == 6:
        percent_sales = 1

    special_num_str = str(special_num)
    possible_sales = int(str(special_num_str[:2]))
    current_sales = possible_sales * percent_sales
    total_sales_made += current_sales
    current_sales = 0
    total_sum_ratings += rating


print(f"{total_sales_made:.2f}")
print(f"{(total_sum_ratings / amount_pc):.2f}")
