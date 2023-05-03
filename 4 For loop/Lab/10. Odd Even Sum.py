sequance = int(input())
even_sum = odd_sum = 0

for i in range(1, sequance + 1):
    user_input = int(input())
    if i % 2 == 0:
        even_sum += user_input
    else:
        odd_sum += user_input

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(odd_sum - even_sum)}')

