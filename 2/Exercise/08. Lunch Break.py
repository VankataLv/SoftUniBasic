from math import ceil


show_name = input()
length_episode = int(input())
brake_length = int(input())

time_needed = length_episode + (brake_length * (1/8)) + (brake_length * (1/4))

if time_needed <= brake_length:
    print(f'You have enough time to watch {show_name} and left with {ceil(brake_length - time_needed)} minutes free time.')
else:
    print(f"You don't have enough time to watch {show_name}, you need {ceil(time_needed - brake_length)} more minutes.")
