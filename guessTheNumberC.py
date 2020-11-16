import random

print('I am thinking of a number between 1 and 20')
number=random.randint(1,20)
guess='0'
guesses=0

print('Take a guess.')

while(int(guess) != number):
    
    guess = input()
    if(int(guess) != number):
        print('WRONG! Try again.')
        guesses=guesses + 1

print('Congratulations! It was '+ str(number) + ' in ' + str(guesses) + ' guesses. But at what cost...')