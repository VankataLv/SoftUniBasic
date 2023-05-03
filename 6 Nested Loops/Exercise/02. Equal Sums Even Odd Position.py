first_num = int(input())
second_num = int(input())
even_pos_sum = odd_pos_sum = 0

for current_num in range(first_num, second_num + 1):
    reading_var = str(current_num)

    for index, digit in enumerate(reading_var):
        if index % 2 == 0:
            odd_pos_sum += int(digit)
        else:
            even_pos_sum += int(digit)

    if even_pos_sum == odd_pos_sum:
        print(current_num, end=" ")

