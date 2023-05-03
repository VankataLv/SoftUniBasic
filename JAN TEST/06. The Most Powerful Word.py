from math import floor
word = input()
current_score = highest_score = 0
strongest_word = ""
while word != "End of words":
    for letter in range(0, len(word)):
        current_score += ord(word[letter])
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" or word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        current_score *= len(word)
    else:
        current_score = floor(current_score / len(word))
    if current_score > highest_score:
        highest_score = current_score
        strongest_word = word

    current_score = 0
    word = input()

print(f'The most powerful word is {strongest_word} - {highest_score}')
