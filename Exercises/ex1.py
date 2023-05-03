def problem_1 (num_1,num_2):
    product = num_1*num_2
    if product > 1000:
        return num_1+num_2
    else:
        return product

result = problem_1(20,30)
print(f'The result is {result}')

result = problem_1(30,40)
print(f'The result is {result}')
