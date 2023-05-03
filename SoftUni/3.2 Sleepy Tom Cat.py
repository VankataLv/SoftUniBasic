import math
days_off = int(input())
norm_per_year = 30000    # min
norm_per_year_hrs = int(norm_per_year / 60) # hrs
work_days = 365 - days_off
play_work = 63
play_day_off = 127
real_play = (work_days * play_work) + (days_off * play_day_off)
left_over_play_time = norm_per_year - real_play

if real_play > norm_per_year:
    print("Tom will run away")
    H = math.floor(real_play / 60)
    M = real_play % 60
    print(f'{abs(norm_per_year_hrs - H)} hours and {M} minutes more for play')
else:
    print("Tom sleeps well")
    H = math.floor(left_over_play_time / 60)
    M = left_over_play_time % 60
    print(f'{abs(H)} hours and {M} minutes less for play')
