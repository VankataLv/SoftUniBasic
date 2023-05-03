from sys import maxsize
user_input = input()
current_num = 0
max_num = -maxsize
while user_input != "Stop":
    current_num = int(user_input)
    if max_num < current_num:
        max_num = current_num
    user_input = input()
print(max_num)


