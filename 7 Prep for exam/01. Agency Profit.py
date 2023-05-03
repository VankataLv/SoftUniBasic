company_name = input()
qt_ticket_adult = int(input())
qt_ticket_child = int(input())
net_price_ticket_adult = float(input())
service_tax = float(input())
real_price_adult = net_price_ticket_adult + service_tax
real_price_child = (net_price_ticket_adult * 0.3) + service_tax
total_profit = ((real_price_adult * qt_ticket_adult) + (real_price_child * qt_ticket_child)) * 0.2

print(f"The profit of your agency from {company_name} tickets is {total_profit:.2f} lv.")
