capacity = float(input())
case_volume = input()
case_counter = current_load = 0

while case_volume != "End":
    case_volume = float(case_volume)

    if case_counter != 0:
        if case_counter % 3 == 0:
            case_volume = case_volume * 1.1

    current_load += case_volume

    if capacity > current_load:
        case_counter += 1
    else:
        print(f'No more space!')
        break
    case_volume = input()

if case_volume == "End":
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {case_counter} suitcases loaded.')
