import random
import os
random_list = ["alligator", "rice", "university", "megalodon", "watchman"]
chosen = random.choice(random_list)
count = len(chosen)
print(chosen)
print("count : ", count)
life= 6
hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


guessed = []
for i in range(count):
    guessed.append("_")
print(" ".join(guessed))
end_of_game = False
while not end_of_game and life > 0:
    guessed_letter = input("Guess a letter: ").lower()
    os.system('cls')
    if guessed_letter in guessed:
        print("You have already guessed this letter")
    elif guessed_letter in chosen:
        for i in range(count):
            if guessed_letter == chosen[i]:
                guessed[i] = guessed_letter
        print(" ".join(guessed))
        if "_" not in guessed:
            end_of_game = True
    else:
        print("This letter is not in the word")
        print(hangman[-life])
        life -= 1

if end_of_game and life > 0:
    print("You guessed the word!")
else:
    print("You lost!")