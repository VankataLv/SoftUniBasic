lower_limit = int(input())
higher_limit = int(input())
even_status = False
for barcode_num in range(lower_limit, higher_limit + 1):
    for char in range(0, 4):
        if int(str(barcode_num)[char]) % 2 == 0:
            even_status = True
    if not even_status:
        print(barcode_num, end=" ")
    else:
        even_status = False
