import game_data
import art
import random

def play_game():
    # Initialize score
    score = 0
    game_over = False
    while not game_over:
        #Get two random items from the game data
        item1, item2 = random.sample(game_data.data, 2)

        #Display the artwork
        print(art.logo)

        #If there is a score, display it
        if score != 0:
            print(f"Your current score is {score}")

        #Display item 1
        print(f"Compare A: {item1["name"]}, a {item1["description"]} from {item1["country"]}")

        #Display vs art
        print(art.vs)

        #Display item 2
        print(f"Against B: {item2["name"]}, a {item2["description"]} from {item2["country"]}")

        #Get the user's input for their choice
        user_choice = input("Who has more followers? Type A or B.").lower()

        #Get the appropriate item that corresponds with the user's choice
        #Compare the # followers
        if user_choice == "a":
            if item1["follower_count"] > item2["follower_count"]:
                #User was correct, increment score and notify them
                score += 1
                print(f"You're correct! Your current score is {score}.")
            else:
                #User was not correct, game over
                game_over = True
        elif user_choice == "b":
            if item2["follower_count"] > item1["follower_count"]:
                # User was correct, increment score and notify them
                score += 1
                print(f"You're correct! Your current score is {score}.")
            else:
                #User was not correct, game over
                game_over = True
        else:
            print("Sorry, that input is not valid. Your score is 0.")

    print(f"Sorry, you lose. Your final score was {score}")

#Call the function to play the game
play_game()