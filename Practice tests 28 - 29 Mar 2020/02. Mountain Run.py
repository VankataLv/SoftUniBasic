from math import floor

old_record_sec = float(input())
distance_m = float(input())
rate_climb_1m = float(input())

time_addition = floor(distance_m / 50) * 30
george_time_sec = (distance_m * rate_climb_1m) + time_addition
time_failed_by = george_time_sec - old_record_sec

if george_time_sec < old_record_sec:
    print(f'Yes! The new record is {george_time_sec:.2f} seconds.')
else:
    print(f'No! He was {time_failed_by:.2f} seconds slower.')
