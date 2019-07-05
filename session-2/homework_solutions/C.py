# Pseudo code for the simple solution

# Tell user to think of a random number
# User have to press return to start the guessing
# Computer reveals guess, and ask if it is right
# if computer is right, print I won, else You won


# Simple solution
welcome_text = "Welcome! Please think of a number between 1 and 10."
print(welcome_text)
input("When ready press return")

computer_guess = 1

print("Are you thinking of the number",computer_guess,"[y/n]?")
answer = input()
if answer == "y":
    print("I won hahaha")
    print("GAME OVER!", end = "\n\n")
else:
    print("Bummer...")
    print("you won... For now", end = "\n\n")



# Pseudo for a new strategy

# Tell user to think of a random number
# User have to press return to start the guessing
# Initialize guess, and set a guess_again flag as True
# while the flag is true, keep guessing
# Computer reveals guess, and ask if it is right
# if computer is right, print I won and set flag as False, else You won and increment gues


# New stategy solution
print("ROUND 2")
welcome_text = "Welcome! Please think of a number between 1 and 10."
print(welcome_text)
input("When ready press return")

computer_guess = 1
guess_again = True

while guess_again:
    print("Are you thinking of the number",computer_guess,"[y/n]?")
    answer = input()
    if answer == "y":
        print("I won hahaha")
        print("GAME OVER!", end = "\n\n")
        guess_again = False
    else:
        print("Bummer...")
        print("you won... For now", end = "\n\n")
        computer_guess += 1



# Pseudo for a new strategy and with hints

# Tell user to think of a random number
# User have to press return to start the guessing
# Initialize guess as 5 this time
# and set a guess_again flag as True
# while the flag is true, keep guessing
# Computer reveals guess, and ask if it is right
# if computer is right, print I won and set flag as False, 
# else You won and ask if the guess is over or under
# If over then increment the guess, else decrease it


# Hint solution
print("ROUND 3")
welcome_text = "Welcome! Please think of a number between 1 and 10."
print(welcome_text)
input("When ready press return")

computer_guess = 5
guess_again = True

while guess_again:
    print("Are you thinking of the number",computer_guess,"[y/n]?")
    answer = input()
    if answer == "y":
        print("I won hahaha")
        print("GAME OVER!")
        guess_again = False
    else:
        print("Bummer...")
        hint = input("Is the number you're thinking of greater or smaller? [g/s]")
        if hint == "g":
            computer_guess += 1
        else:
            computer_guess -= 1
