import random, time

numberOfStreaks = 0

numberOfTailsStreaks = 0
numberOfHeadsStreaks = 0

throws = []

for experimentNumber in range(10000):
    if random.randint(0,1) == 0:
        throws.append('H')
    else:
        throws.append('T')

for i in range(len(throws) - 6):
    if throws[i] == throws[i + 1]:
        if throws[i] == throws[i + 2]:
            if throws[i] == throws[i + 3]:
                if throws[i] == throws[i + 4]:
                    if throws[i] == throws[i + 5]:
                        if throws[i] == 'T':
                            numberOfTailsStreaks += 1
                            i+=6
                        else:
                            numberOfHeadsStreaks += 1
                            i+=6
print('Tails streaks: ' + str(numberOfTailsStreaks) + '\n Heads streaks: ' + str(numberOfHeadsStreaks))

numberOfStreaks = numberOfHeadsStreaks + numberOfTailsStreaks

print('Chance of streak: %s%%' % (numberOfStreaks / 100))