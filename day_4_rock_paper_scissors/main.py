import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

play_game = True

while play_game:
    #Get the user's choice by integer value
    user_choice= int(input("What do you choose? Enter 0 for rock, 1 for paper, or 2 for scissors."))
    #If user entered valid input, show the image corresponding to their choice
    if -1 < user_choice < 3:
        print(f"You chose {game_images[user_choice]}")
    #User did not enter valid input. Inform them and exit the game
    else:
        print(f"You entered an invalid choice. Please restart and try again")
        play_game = False
        break

    #Get the computer choice
    computer_choice = random.randint(0, 2)
    #Display the computer's choice
    print(f"Computer chose {game_images[computer_choice]}")

    if user_choice == computer_choice:
        print("This is a tie.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose! ")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")