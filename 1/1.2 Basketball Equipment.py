tax_year = int(input())

shoe_price = tax_year - (tax_year * 0.4)
outfit_price = shoe_price - (shoe_price * 0.2)
ball_price = outfit_price * 0.25
acc_price = ball_price * 0.2

total_cost = shoe_price + outfit_price + ball_price + acc_price + tax_year
print(total_cost)
