from sys import maxsize
user_input = input()
current_num = 0
min_num = maxsize
while user_input != "Stop":
    current_num = int(user_input)
    if min_num > current_num:
        min_num = current_num
    user_input = input()
print(min_num)