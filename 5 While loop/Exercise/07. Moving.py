w = int(input())
l = int(input())
h = int(input())
amnt_packages_moved = 0
free_space = w * l * h

while amnt_packages_moved != "Done":
    free_space -= int(amnt_packages_moved)
    if free_space <= 0:
        print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
        quit()
    amnt_packages_moved = input()
else:
    print(f"{free_space} Cubic meters left.")
