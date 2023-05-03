budget = float(input())
amount_video_cards = int(input())
amount_cpu = int(input())
amount_ram = int(input())

video_card_price = 250
cpu_price = (video_card_price * amount_video_cards) * 0.35
ram_price = (video_card_price * amount_video_cards) * 0.1

total_cost = (video_card_price * amount_video_cards) + (cpu_price * amount_cpu) + (ram_price * amount_ram)

if amount_video_cards > amount_cpu:
    total_cost *= 0.85

if budget >= total_cost:
    print(f'You have {(budget - total_cost):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_cost - budget):.2f} leva more!')
