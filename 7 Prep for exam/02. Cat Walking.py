min_walk_day = int(input())
times_walk_day = int(input())
eaten_calories_day = int(input())

burned_calories_day = (min_walk_day * 5) * times_walk_day

if eaten_calories_day / 2 <= burned_calories_day:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories_day}.')
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories_day}.")
