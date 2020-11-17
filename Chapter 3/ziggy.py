import time

def starLine():
    stars='*'*8
    return stars

def zig(compi):
    if compi == 'greater':
        for i in range(20,0,-1):
            time.sleep(0.01)
            print(' ' * i,starLine(),sep='')
        return 0
    elif compi == 'lesser':
        for i in range(20):
            time.sleep(0.01)
            print(' ' * i,starLine(),sep='')
        return 21


def zigZoog():
    spaces = 0

    while True:
        

        if spaces < 20:
            spaces = zig('lesser')
        elif spaces > 20:
            spaces = zig('greater')


        

while(True):
    zigZoog()