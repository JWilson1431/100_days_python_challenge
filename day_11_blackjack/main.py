import random
import art

#Initialize set of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#function to draw cards
def draw_cards():
    """Draws the initial cards for both players"""
    return[random.choice(cards), random.choice(cards)]

#function to add all cards in hand
def sum_cards(cards_in_hand):
    """Gets the sum of all cards in hand"""
    return sum(cards_in_hand)

#function to determine if the user wants to draw another card
def prompt_user_draw_again():
    """Determines if user wants to draw another card"""
    draw_again = input("Type y to get another card. Type n to pass")
    if draw_again == "y":
        return True
    else:
        return False

#function to draw another card
def draw_another_card(card_hand):
    """Adds another random card to the hand"""
    card_hand.append(random.choice(cards))
    return card_hand

#function to print the final score
def print_final_score(user_hand, dealer_hand):
    """Prints the final hands and score"""
    print(f"Your final hand is {user_hand}. Your final score is {sum_cards(user_hand)}")
    print(f"The computer's final hand is {dealer_hand}. It's final score is {sum_cards(dealer_hand)}")

#function to check the score and determine winner
def check_score(user_hand, dealer_hand):
    """Checks the sum of the user hand and dealer hand and determines winner"""
    #Scores are equal, declare a tie
    if sum_cards(user_hand) == sum_cards(dealer_hand):
        print("This game was a tie! Even scores!")
    #User got blackjack
    elif sum_cards(user_hand) == 21 and sum_cards(dealer_hand) != 21:
        print("You win with a Blackjack!")
    #Dealer got blackjack
    elif sum_cards(user_hand) != 21 and sum_cards(dealer_hand) == 21:
        print("Dealer wins with a Blackjack!")
    #User went over 21 and dealer did not
    elif sum_cards(user_hand) > 21 and sum_cards(dealer_hand) < 21:
        print("You lose! Your total is over 21.")
    #Dealer went over 21 and user did not
    elif sum_cards(user_hand) < 21 and sum_cards(dealer_hand) > 21:
        print("You win! The dealer's total is over 21.")
    #Compare user and dealer hands to see whose total is greater
    else:
        if sum_cards(user_hand) > sum_cards(dealer_hand):
            print("You win!")
        else:
            print("You lose!")

#function to play a game of blackjack
def play_blackjack():
    """Core functionality to play the game"""
    play_game = True
    while play_game:
        #draw initial cards for user and dealer
        user_cards = draw_cards()
        dealer_cards = draw_cards()
        #display the blackjack logo
        print(art.logo)
        #Get the user score from the sum of the user's cards
        user_score = sum_cards(user_cards)
        #Print the initial score and hands
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card {dealer_cards[0]}")

        if user_score < 21:
            #determine if user wants to draw another card
            draw_again = prompt_user_draw_again()
            if draw_again:
                #user chose to draw again, add another card to hand
                user_cards = draw_another_card(user_cards)
            else:
                #user chose not to draw again, end game
                play_game = False

        #Draw another card for the dealer if their total is less than 17
        while sum_cards(dealer_cards) < 17:
            draw_another_card(dealer_cards)
            print(f"Dealer's current hand: {dealer_cards}, score: {sum_cards(dealer_cards)}")

        #Check and print the final results
        print_final_score(user_cards, dealer_cards)
        check_score(user_cards, dealer_cards)

#Determine if the user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 15)
    play_blackjack()