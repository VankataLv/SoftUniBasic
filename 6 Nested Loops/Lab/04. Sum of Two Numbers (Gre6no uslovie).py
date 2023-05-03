first_num = int(input())
second_num = int(input())
magic_num = int(input())
combination_counter = 0
at_least_one_answer = False

for i in range(first_num, second_num + 1):
    for j in range(first_num, second_num + 1):
        combination_counter += 1
        if i + j == magic_num:
            print(f"Combination N:{combination_counter} ({i} + {j} = {magic_num})")
            quit()
if not at_least_one_answer:
    print(f"{combination_counter} combinations - neither equals {magic_num}")

# Никъде не е казано че трябва да печатиш само първата комбинация... Грешно условие