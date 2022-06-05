import random
from hangman_words import list_of_words
from hangman_art import stages, logo


print(logo)
chosen_word = random.choice(list_of_words)
word_length = len(chosen_word)

end_of_game = False
lives = 6
display = []

for letter in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"{guess} has already been entered. You lose a life")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])