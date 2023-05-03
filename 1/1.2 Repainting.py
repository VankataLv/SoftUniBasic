nylon_price = 1.5
paint_price = 14.5
dissolver_price = 5.0

nylon_needed = int(input())
paint_needed = int(input())
dissolver_needed = int(input())
hrs_needed = int(input())

nylon_bought = (nylon_needed + 2)
paint_bought = (paint_needed + (paint_needed * 0.1))
total_cost_mat = (nylon_bought * nylon_price) + (paint_bought * paint_price) + (dissolver_price * dissolver_needed) + 0.4
worker_pay = (total_cost_mat * 0.3) * hrs_needed

total_price_everything = total_cost_mat + worker_pay
print(total_price_everything)
