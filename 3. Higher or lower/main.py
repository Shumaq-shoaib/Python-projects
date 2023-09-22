import asscii
import Game_Data
import random
import os
import time

global score
score=0
gameOver = False
def clear():
    os.system('cls')
#random number generator (1-50) and selects two entries from the list as options

def print_screen():
    """
    Prints information about two options from Game_Data.data list.
    """
    global option1, option2
    print(asscii.logo)
    option1, option2 = random.sample(Game_Data.data, 2)
    print(f"A. {option1['name']}, a {option1['description']} from {option1['country']}")
    print(asscii.vs)
    print(f"B. {option2['name']}, a {option2['description']} from {option2['country']}")

def process_data():
    """ Compares both selections and made and processes user input to check if the guessed answer is correct or not"""
    global winner,looser, choice, guess
    if option1['follower_count']> option2['follower_count']:
        winner=option1
        looser= option2
    elif option2['follower_count']> option1['follower_count']:
        winner = option2
        looser= option1
    choice= input("Select which of the above has higher follower count in millions? (Enter 'A' or 'B')")
    choice=choice.lower()
    match choice:
        case "a":
            global score
            guess = option1
        case "b":
            guess = option2
        case default:
            clear()
            print("Invalid input!")
            exit()
    if guess == winner:
        clear()
        print(f"You guessed it right! {winner['name']} has more followers {winner['follower_count']}M,  whereas {looser['name']} has {looser['follower_count']}M followers")
        score+=1
        if score != 0:
            print(f"Your current score is {score}")
    else:
        clear()
        print(f"Wrong! {winner['name']} has more followers having {winner['follower_count']}M than {guess['name']} having {guess['follower_count']}M")
        print(f"GAME OVER, your final score was {score}")
        gameOver = True
        exit()
def play_game():
    """Runs the game by running print_screen() and process_data() functions in loop until Game is not over"""
    global score
    global gameOver
    while not gameOver== True:
        print_screen()
        process_data()
    print(f"Game Over! Your final score is: {score}")
    
play_game()

