import random
word_list = ["word","list","ice","fire"]
chosen_word = random.choice(word_list)


display = []

word_len = len(chosen_word)
for i in range(word_len):
    display += "_"

guess = input("guess the letter").lower()

for position in range(word_len):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter

print(display)

