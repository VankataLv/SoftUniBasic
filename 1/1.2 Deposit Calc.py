deposit_sum = float(input())
months = int(input())
int_rate_yearly = float(input()) / 100

total_sum_end = deposit_sum + months * ((deposit_sum * int_rate_yearly) / 12)

print(total_sum_end)
