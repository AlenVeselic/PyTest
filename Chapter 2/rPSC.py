import random

print('ROCK, PAPER SCISSORS')
wins=0
losses=0
ties=0
print('0 Wins, 0 Losses, 0 Ties')
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

userInput=''


while(userInput != 'q' ):

    pcMove=random.randint(1,3) # Computers move: 1 = rock, 2 = paper, 3 = scissors
    
    userInput = input() # Player's move

    if(userInput == 'r'):
        print('ROCK versus...')
        if(pcMove == 1):
            print('ROCK')
            print('It is a tie!')
            ties=ties+1
        elif(pcMove == 2):
            print('PAPER')
            print('You lose!')
            losses=losses+1
        elif(pcMove == 3):
            print('SCISSORS')
            print('You win!')
            wins=wins+1

    elif(userInput == 'p'):
        print('PAPER versus...')
        if(pcMove == 1):
            print('ROCK')
            print('You win!')
            wins=wins+1
            
        elif(pcMove == 2):
            print('PAPER')
            print('It is a tie!')
            ties=ties+1
            
        elif(pcMove == 3):
            print('SCISSORS')
            print('You lose!')
            losses=losses+1
            
    elif(userInput == 's'):
        print('SCISSORS versus...')
        if(pcMove == 1):
            print('ROCK')
            print('You lose!')
            losses=losses+1
            
            
        elif(pcMove == 2):
            print('PAPER')
            print('You win!')
            wins=wins+1
            
            
        elif(pcMove == 3):
            print('SCISSORS')
            print('It is a tie!')
            ties=ties+1
                
    elif(userInput == 'q'):
        break 
    else:
        print('Invalid input.')
        print(str(wins)+' Wins, '+ str(losses) + ' Losses, ' + str(ties) + ' Ties')
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        continue
    print(str(wins)+' Wins, '+ str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    
    

