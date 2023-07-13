#Imports
import random
from art import logo
import os

#functions

def num_pick():
    num_list = list(range(1,100))
    return int(random.choice(num_list))


def game():
    print("I'm thinking of a number between 1 and 100.")
    Difficuty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if Difficuty == "easy":
        attemps = 10
    elif Difficuty == "hard":
        attemps = 5
    number = num_pick()
    end = False
    while not end:
        guess = int(input("Make a guess:"))
        if guess == number:
            print(f"You got it right! The number was {number}")
            end = True
        elif guess > number:
            attemps -= 1
            print(f"Too High! {attemps} tries left.")
            if attemps == 0:
                end = True
                print(f"You have used all your attempts.You lose!\nThe number was {number}")
        elif guess < number:
            attemps -= 1
            print(f"Too Low! {attemps} tries left.")
            if attemps == 0:
                end = True
                print(f"You have used all your attempts.You lose!\nThe number was {number}")

#Gameplay Loop

while input("Do you want to play Guess The Number? y(yes) or n(no): ") == "y":
    os.system('cls||clear')
    print(logo)
    game()