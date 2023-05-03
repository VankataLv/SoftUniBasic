painted_eggs = int(input())
max_eggs_color = ""
red_eggs = orange_eggs = blue_eggs = green_eggs = max_eggs = 0

for eggs in range(0, painted_eggs):
    current_egg_color = (input())
    if current_egg_color == "red":
        red_eggs += 1
    elif current_egg_color == "orange":
        orange_eggs += 1
    elif current_egg_color == "blue":
        blue_eggs += 1
    elif current_egg_color == "green":
        green_eggs += 1

max_eggs = max(red_eggs, orange_eggs, blue_eggs, green_eggs)
if red_eggs == max_eggs:
    max_eggs_color = "red"
elif orange_eggs == max_eggs:
    max_eggs_color = "orange"
elif blue_eggs == max_eggs:
    max_eggs_color = "blue"
elif green_eggs == max_eggs:
    max_eggs_color = "green"

print(f"Red eggs: {red_eggs}\n"
      f"Orange eggs: {orange_eggs}\n"
      f"Blue eggs: {blue_eggs}\n"
      f"Green eggs: {green_eggs}\n"
      f"Max eggs: {max_eggs} -> {max_eggs_color}")