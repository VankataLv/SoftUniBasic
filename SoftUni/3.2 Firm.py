import math
hrs_needed = int(input())
days_to_complete = int(input())
workers = int(input())

days_to_work = days_to_complete * 0.9
hrs_to_work = math.floor((days_to_work * 10) * workers)

if hrs_needed <= hrs_to_work:
    print(f'Yes!{hrs_to_work - hrs_needed} hours left.')
else:
    print(f'Not enough time!{hrs_needed - hrs_to_work} hours needed.')
