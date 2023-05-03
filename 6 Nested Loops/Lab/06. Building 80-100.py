floors_in_bldg = int(input())
rooms_per_floor = int(input())

if floors_in_bldg == 1:
    for large_apartments_num in range(0, rooms_per_floor + 1):
        print(f"L1{large_apartments_num}", end=' ')
    quit()
highest_floor = floors_in_bldg

for large_apartments_num in range(0, rooms_per_floor):
    print(f"L{highest_floor}{large_apartments_num}", end=' ')
print("")
for cur_floor in range(floors_in_bldg - 1, 0, -1):
    if cur_floor % 2 == 0:
        for office in range(0, rooms_per_floor):
            print(f"O{cur_floor}{office}", end=' ')
    else:
        for apartment in range(0, rooms_per_floor):
            print(f"A{cur_floor}{apartment}", end=' ')
    print("")
