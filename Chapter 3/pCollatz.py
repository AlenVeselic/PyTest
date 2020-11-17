import sys, time

def collatz(number):

    if number % 2 == 0:
        print(str(number // 2))
        return number // 2
    elif number % 2 == 1:
        print(str(3 * number + 1))
        return 3 * number + 1



try:

    print('Give me a number, any number!')
    time.sleep(1)
    print("and I'll Collatz it, I swear I will")
    time.sleep(1)
    print('You mark my words, sir!')
    time.sleep(1)
    print('just, uh, just give me a number, ok?')
    time.sleep(2)
    print('[Enter number]')
    number=int(input())

    while number != 1:
        number=collatz(number)

    print('GET COLLATZED, FOOL! HAHAHAHAHA HA uhm, bye now')
except ValueError:
    print("That's not a number, buzz off. I just wanna Collatz...not start a meaningful conversation that could lead to a fruitful friendship to span years! Smell you later, square!")
    sys.exit()
except:
    print('Ya goofed it!')
    sys.exit()