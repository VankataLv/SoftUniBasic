w = int(input())
l = int(input())
pieces_available = w * l
pieces_taken = 0
while pieces_taken != "STOP":
    pieces_available -= int(pieces_taken)
    if pieces_available <= 0:
        print(f"No more cake left! You need {abs(pieces_available)} pieces more.")
        quit()
    pieces_taken = input()
else:
    print(f"{pieces_available} pieces are left.")