import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

chosen = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    counter = 10
elif difficulty == "hard":
    counter = 5

guess = 0

while guess != chosen:
    while counter > 0:
        print(f"You have {counter} attempts remaining to guess a number.")
        guess = int(input("Make a guess: "))
        if guess > chosen:
            print("Too high.")
        elif guess < chosen:
            print("Too low.")
        else:
            print(f"You got it right. The answer was {guess}. You win.")
            break
        counter -= 1
        if counter == 0:
            print("You are out of chances. You lose")
            break
        print("Guess again.")
        