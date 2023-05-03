min_day = int(input())
amnt_wals_day = int(input())
cal_eaten = int(input())

cal_burnt_day = (min_day * 5) * amnt_wals_day

if cal_burnt_day >= (cal_eaten / 2):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {cal_burnt_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {cal_burnt_day}.')
