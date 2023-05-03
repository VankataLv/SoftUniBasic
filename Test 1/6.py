user_input = int(input())

user_input_str = str(user_input)
first_num_max = int(user_input_str[2])
second_num_max = int(user_input_str[1])
third_num_max = int(user_input_str[0])

for first_num in range(1, first_num_max + 1):
    for second_num in range(1, second_num_max + 1):
        for third_num in range(1, third_num_max + 1):
            print(f"{first_num} * {second_num} * {third_num} = {first_num * second_num * third_num};")
