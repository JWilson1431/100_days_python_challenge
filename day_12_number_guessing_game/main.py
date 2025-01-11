import random

#Get the random number for the user to guess
global NUMBER_TO_WIN
NUMBER_TO_WIN = random.randint(0, 100)

print("Welcome to the number guessing game!")
level = input("Would you like to play the game at an easy or hard level? Type easy or hard")
if level == "easy":
    lives = 10
    print(f"You have {lives} lives")
elif level == "hard":
    lives = 5
else:
    lives = 0
    print("You entered an invalid level. Please restart the game and choose either 'easy' or 'hard'.")

def make_guess(lives):
    guess = int(input("Enter your numeric guess."))
    if guess == NUMBER_TO_WIN:
        print(f"You guessed it correct! The number was {NUMBER_TO_WIN}")
        return -1
    if guess > NUMBER_TO_WIN:
        print("Your guess is too high.")
        lives -= 1
        print(f"You have {lives} lives left.")
        return lives
    if guess < NUMBER_TO_WIN:
        print("Your guess is too low.")
        lives -= 1
        print(f"You have {lives} lives left.")
        return lives


while lives > 0:
    lives = make_guess(lives)

if lives == 0:
    print(f"Sorry, you lost this round. Please try another game!")