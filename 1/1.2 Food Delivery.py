chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15
delivery_price = 2.50

chicken_needed = int(input())
fish_needed = int(input())
veggie_needed = int(input())

food_cost = (chicken_needed * chicken_price) + (fish_needed * fish_price) + (veggie_needed * veggie_price)
dessert_price = food_cost * 0.2
total_cost_all = food_cost + dessert_price + delivery_price
print("%.2f" % total_cost_all)
