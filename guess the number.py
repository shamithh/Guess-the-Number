import random
easy_lives = 10
hard_lives = 5
def logic(user_input , random_number , turns):
    if user_input > random_number:
        print("too high!")
        return turns - 1
    elif user_input < random_number:
        print("too low!")
        return turns - 1
    else:
        print(f"yay you guessed the number it was {random_number}!!")


def set_difficulty():
    difficulty = input("Do You want Hard mode or Easy mode :").lower()
    if difficulty == "hard":
        return hard_lives
    elif difficulty == "easy":
        return easy_lives


def game():
    print("Welcome to number guessing game")
    print("I'm thinking of a number between 0 to 100!")
    turns = set_difficulty()
    answer = random.randint(0,100)
    guess = 0
    while guess != answer:
        print(f"you have {turns} guesses left")
        guess = int(input("Make a guess : "))
        turns = logic(guess , answer , turns)
        if turns == 0:
            print("You have Run out of Guesses. You Lose!! ")
            return
game()







