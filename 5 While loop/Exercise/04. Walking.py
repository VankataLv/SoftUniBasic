steps_walked = 0
total_steps = 0

while total_steps < 10000:
    steps_walked = input()
    if steps_walked == "Going home":
        steps_walked = int(input())
        total_steps += steps_walked
        if total_steps < 10000:
            print(f"{10000 - total_steps} more steps to reach goal.")
            break
        else:
            print("Goal reached! Good job!")
            print(f'{total_steps - 10000} steps over the goal!')
            break
    total_steps += int(steps_walked)
else:
    print("Goal reached! Good job!")
    print(f'{total_steps - 10000} steps over the goal!')
