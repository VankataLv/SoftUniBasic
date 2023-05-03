first_eggs = int(input())
second_eggs = int(input())
combat_status = input()

while combat_status != "End":
    if combat_status == "one":
        second_eggs -= 1
    if combat_status == "two":
        first_eggs -= 1
    if first_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_eggs} eggs left.")
        quit()
    if second_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_eggs} eggs left.")
        quit()
    combat_status = input()

print(f"Player one has {first_eggs} eggs left.")
print(f"Player two has {second_eggs} eggs left.")
