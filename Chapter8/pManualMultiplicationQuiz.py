import random, time, threading

response = None
correctAnswers = 0

for question in range(10):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    tries = 3
    start = time.time()
    while response != (num1*num2) :
        print(f'Q{question}: {num1} x {num2} =')
        while True:
            try:
                response = int(input())
                if str(response).isdecimal():
                    break
            except:
                print('Please enter a number: ')
                continue
        now = time.time()
        if (now - start) % 60 > 8:
            print("Time's up, buckarooo.")
            break
        if response != (num1*num2):
            if tries > 0: 
                print('Try again')
                tries -= 1
                continue
            else:
                print('No more tries for you, pal.')
                break
        else:
            print('Correct!')
            correctAnswers += 1
        time.sleep(1)

print("You've answered " + str(correctAnswers) + ' questions correctly!')