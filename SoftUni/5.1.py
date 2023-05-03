text = (input().lower())
a = 1
e = 2
i = 3
o = 4
u = 5
sum_letters = 0

for letter_pos in range(0, len(text)):
    if text[letter_pos] == 'a':
        sum_letters += a
    elif text[letter_pos] == 'e':
        sum_letters += e
    elif text[letter_pos] == 'i':
        sum_letters += i
    elif text[letter_pos] == 'o':
        sum_letters += o
    elif text[letter_pos] == 'u':
        sum_letters += u
    else:
        pass
print(sum_letters)
