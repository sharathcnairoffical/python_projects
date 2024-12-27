import random

number = random.randint(1, 100)
def number_guessing_game(input):
    if input > number:
        print("Too High!!")
    elif input < number:
        print("Too Low!!")
    else:
        print("Congratulations! You guessed the number")
        return True
    return False


while True:
    try:
        guess = int(input('Guess the number between 1 and 100 :'))
        if number_guessing_game(guess):
            break
    except ValueError:
        print("Please Enter a valid Number..")


