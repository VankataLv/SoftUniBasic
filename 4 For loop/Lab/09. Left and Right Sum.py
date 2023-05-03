sequances = int(input())
left_sum = right_sum = 0
for i in range(1, (2 * sequances) + 1):
    user_input = int(input())
    if i <= (2 * sequances) / 2:
        left_sum += user_input
    if i > (2 * sequances) / 2:
        right_sum += user_input

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum-right_sum)}")

