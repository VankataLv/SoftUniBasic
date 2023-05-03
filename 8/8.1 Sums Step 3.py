n = int(input())
sum1 = sum2 = sum3 = 0

for i in range(1, n+1):
    current_num = int(input())
    left_over = (i % 3)
    if left_over == 1:
        sum1 += current_num
    elif left_over == 2:
        sum2 += current_num
    else:
        sum3 += current_num

print(f'''sum1 = {sum1}
sum2 = {sum2}
sum3 = {sum3}''')
