# My first Python program
name = input('What is your name? ')
print('Hello, ' + name + '. Time to play hangman!')
print('Start guessing...')

secret_word = 'secret'
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in secret_word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1

    if failed == 0:
        print('\nYou won!')
        break

    print()
    guess = input('Guess a character: ')

    if len(guess) > 1:
        print('Only one character at the time, please!')
        continue

    guesses += guess

    if guess not in secret_word:
        turns -= 1
        print('Wrong\n')
        print('You have', turns, 'more guesses')
        if turns == 0:
            print('You lose!')
