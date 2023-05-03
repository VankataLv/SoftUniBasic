a = int(input())
b = int(input())
action = input()
even_odd = ()

if action == "+":
    if (a + b) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{a} {action} {b} = {a + b} - {even_odd}")
elif action == "-":
    if (a - b) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{a} {action} {b} = {a - b} - {even_odd}")
elif action == "*":
    if (a * b) % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{a} {action} {b} = {a * b} - {even_odd}")
elif action == "/":
    if b == 0:
        print(f'Cannot divide {a} by zero')
    else:
        print(f"{a} {action} {b} = {a / b:.2f}")
elif action == "%":
    if b == 0:
        print(f'Cannot divide {a} by zero')
    else:
        print(f"{a} {action} {b} = {a % b}")
