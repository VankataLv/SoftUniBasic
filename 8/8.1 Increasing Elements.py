n = int(input())
cur_num = prv_num = inc_count = inc_count_longest = 0

for i in range(1, n+1):
    cur_num = int(input())
    if cur_num > prv_num:
        inc_count += 1
    else:
        inc_count = 1
    prv_num = cur_num

    if inc_count > inc_count_longest:
        inc_count_longest = inc_count

print(f'{inc_count_longest}')
