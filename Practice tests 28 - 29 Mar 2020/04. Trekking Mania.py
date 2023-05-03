group_total = int(input())
Musala_count = Monblan_count = Kilimandjaro_count = K2_count = Everest_count = all_count = 0
for i in range(1, group_total + 1):
    current_people_in_group = int(input())
    all_count += current_people_in_group
    if current_people_in_group <= 5:
        Musala_count += current_people_in_group
    elif 6 <= current_people_in_group <= 12:
        Monblan_count += current_people_in_group
    elif 13 <= current_people_in_group <= 25:
        Kilimandjaro_count += current_people_in_group
    elif 26 <= current_people_in_group <= 40:
        K2_count += current_people_in_group
    elif current_people_in_group >= 41:
        Everest_count += current_people_in_group

percent_Musala = (Musala_count / all_count) * 100
percent_Monblan = (Monblan_count / all_count) * 100
percent_Kilimandjaro = (Kilimandjaro_count / all_count) * 100
percent_K2 = (K2_count / all_count) * 100
percent_Everest = (Everest_count / all_count) * 100

print(f"{percent_Musala:.2f}%")
print(f"{percent_Monblan:.2f}%")
print(f"{percent_Kilimandjaro:.2f}%")
print(f"{percent_K2:.2f}%")
print(f"{percent_Everest:.2f}%")
