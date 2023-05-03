import math

pages_current_book = int(input())
pages_hr = int(input())
days_needed = int(input())

hr_needed_total = pages_current_book / pages_hr
hr_per_day_George = hr_needed_total / days_needed
print(math.floor(hr_per_day_George))
