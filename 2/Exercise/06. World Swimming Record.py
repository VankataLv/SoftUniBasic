from math import floor


current_record = float(input())
distance = float(input())
time_one_meter = float(input())

ivan_time = distance * time_one_meter
water_resistance_times = floor(distance / 15)
resistance_added_time = water_resistance_times * 12.5
ivan_time += resistance_added_time

if current_record > ivan_time:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(ivan_time - current_record):.2f} seconds slower.')
