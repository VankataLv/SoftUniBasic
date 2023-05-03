price_pens = 5.8
price_markers = 7.2
price_detergent = 1.2

pens_needed = int(input())
markers_needed = int(input())
detergent_needed = int(input())
discount = int(input()) / 100   # divided by 100 so to get %

total_cost = (price_pens * pens_needed) + (price_markers * markers_needed) + (price_detergent * detergent_needed)
money_needed = total_cost - (total_cost * discount)
print(money_needed)
