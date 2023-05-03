qty_groups = int(input())
total_climbers = 0
musala = montblanc = kilimandjaro = k2 = everest = 0
for group_num in range(1, qty_groups + 1):
    climbers_current_group = int(input())
    total_climbers += climbers_current_group
    if climbers_current_group <= 5:
        musala += climbers_current_group
    elif 6 <= climbers_current_group <= 12:
        montblanc += climbers_current_group
    elif 13 <= climbers_current_group <= 25:
        kilimandjaro += climbers_current_group
    elif 26 <= climbers_current_group <= 40:
        k2 += climbers_current_group
    elif climbers_current_group > 40:
        everest += climbers_current_group

print(f"{(musala / total_climbers) * 100:.2f}%\n"
      f"{(montblanc / total_climbers) * 100:.2f}%\n"
      f"{(kilimandjaro / total_climbers) * 100:.2f}%\n"
      f"{(k2 / total_climbers) * 100:.2f}%\n"
      f"{(everest / total_climbers) * 100:.2f}%")
