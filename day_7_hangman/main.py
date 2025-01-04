import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    #Tell the user how many lives they have left
    print(f"****************************{lives} LIVES LEFT****************************")
    #Get user guess
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}.")
        continue

    display = ""

    #Display the letters guessed so far and _ where the letters haven't been guessed
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    #Guess was incorrect, subtract a life
    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            #User lost, notify them and tell them the correct word
            print(f"***********************YOU LOSE**********************")
            print(f"The word was {chosen_word}")

    #User won, notify them
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    #Display the stage depending on # lives left
    print(hangman_art.stages[lives])
