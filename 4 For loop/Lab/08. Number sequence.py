import sys
from sys import maxsize
n = int(input())
max_n = -maxsize
min_n = maxsize
user_input = 0
for i in range(0, n):
    user_input = int(input())
    if user_input > max_n:
        max_n = user_input
    if user_input < min_n:
        min_n = user_input

print(f"Max number: {max_n}")
print(f"Min number: {min_n}")
