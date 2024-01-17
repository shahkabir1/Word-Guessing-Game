import random
from typing import TextIO

def intro():
    name = input("What is your name? ")
    print("Hello, " + name + "! I have a word in mind that I would like you to guess. I will give you 6 lives, and you must guess the letters in the word before you run out.")

intro()

def difficulty_input():
    difficulty = input("Please select a difficulty (Easy or Hard): ")
    if difficulty == "Easy" or difficulty == "Hard":
        return difficulty
    else:
        print("That is not a valid difficulty. Please try again.")
        difficulty_input()

diff = difficulty_input()

def choose_difficulty(diff: str):
    if diff == "Easy":
        return 1
    if diff == "Hard":
        return 2
    
def create_word_list(file: TextIO, diff: str) -> list[str]:
    word_lst = []
    with open(file) as f:
        if choose_difficulty(diff) == 1:
            for line in f:
                if len(line.strip()) > 3 and len(line.strip()) <= 6:
                    word_lst.append(line.lower().strip())
        if choose_difficulty(diff) == 2:
            for line in f:
                if len(line.strip()) > 6:
                    word_lst.append(line.lower().strip())
    return word_lst

word = random.choice(create_word_list('wordlist.10000.txt', diff))

valid_letters = "abcdefghijklmnopqrstuvwxyz"

def create_display(text: str) -> str:
    d = ""
    for char in text:
        if char.isalpha():
            d += "_"
        elif char == " ":
            d += " "
    return d

def show_menu(dis):
    print("Please choose an option from the menu:")
    print(dis)
    print("1. Guess a letter.")
    print("2. Guess entire word.")
    print("3. Quit.")

def change_char_at_index(dis: str, word: str, index: int, guess: str):
    if word[index] == guess:
        dis = dis[:index] + guess + dis[index + 1:]
    return dis[index]

def apply_guess_to_display(dis: str, word: str, guess: str):
    v = ""
    for index in range(len(word)):
        v += change_char_at_index(dis, word, index, guess)
    return v

def selection():
    user_input = ""
    lives = 6
    correct_guesses = 0
    dis = create_display(word)
    while user_input != "3" and lives > 0 and dis != word:
        show_menu(dis)
        user_input = input("Enter your turn selection: ")
        if user_input == "1":
            guess = input("Please enter your single, lowercase letter guess: ")
            if guess in valid_letters and len(guess) == 1:
                if guess not in word:
                    lives -= 1
                    print("You have " + str(lives) + " guesses left, with " + str(correct_guesses) + " letters guessed correctly.")
                elif guess in word:
                    correct_guesses += 1
                    dis = apply_guess_to_display(dis, word, guess)
                    if dis != word:
                        print("You have " + str(lives) + " guesses left, with " + str(correct_guesses) + " letters guessed correctly.")
            else:
                print("That guess is an invalid entry. Please try again.")
        elif user_input == "2":
            guess = input("Please enter your word guess: ")
            if len(guess) == len(word) and guess.replace(" ", "").isalpha():
                if guess != word:
                    lives -= 1
                    print("You have " + str(lives) + " guesses left, with " + str(correct_guesses) + " letters guessed correctly.")
                elif guess == word:
                    print("Congratulations, you win! The word was: " + word)
                    break
            else:
                print("That guess is an invalid entry. Please try again.")    
        elif user_input == "3":
             print("Thank you for playing. I would wave goodbye if I could, but I am just a program written by Shah.")
        else:
            print("That is not a valid selection. Please try again.")
    if lives == 0:
        print("You lose! The word was: " + word + ".")
    elif dis == word:
        print("Congratulations, you win! The word was: " + word + ".")

selection()