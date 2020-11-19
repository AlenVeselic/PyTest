import pprint, sys
eChessBoard = {
}

# by mistake I made a chessboard setting up program instead of a validator

def printChessB(board):
    for x in range(7,-2,-1):
        print('-'*17, end='')
        print()
        
        if( x > -1):
            for y in range(8):
                print('|', end='')
                print(board[str(x + 1) + chr(97+y)], end='')
            print('| ',end='')    
            print(str(x + 1))
            
        else:
            for y in range(8):
                print(' ', end='')
                print(chr(97 + y), end='')

    print()

pieceLimits = {
    'pawn': 8, 'king': 1, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1
}



for x in range(8):
    for y in range(8):
         eChessBoard.setdefault(str(x + 1) + str(chr(97 + y)), ' ')

wPieces = {}
bPieces = {}


while True:

    
    piece = ' '

    print('Who are you positioning for? b/w')

    turn = input()

    if turn == 'w':
        while piece not in pieceLimits.keys():
            printChessB(eChessBoard)
            print(' What would you like to place?')

            piece = input()

            if piece == 'king' :
                wPieces.setdefault('king', 0)

                if wPieces['king'] < pieceLimits['king']:
                    wPieces['king'] += 1
                    
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'pawn':
                wPieces.setdefault('pawn', 0)

                if wPieces['pawn'] < pieceLimits['pawn']:
                    wPieces['pawn'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'bishop':
                wPieces.setdefault('bishop', 0)

                if wPieces['bishop'] < pieceLimits['bishop']:
                    wPieces['bishop'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'rook':
                wPieces.setdefault('rook', 0)

                if wPieces['rook'] < pieceLimits['rook']:
                    wPieces['rook'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'queen':
                wPieces.setdefault('queen', 0)

                if wPieces['queen'] < pieceLimits['queen']:
                    wPieces['queen'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'knight':
                wPieces.setdefault('knight', 0)

                if wPieces['knight'] < pieceLimits['knight']:
                    wPieces['knight'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue
            else:
                print('Input error: Not a piece')
        
        
        print('Where would you like to place your ' + piece + '?')

        pos = input()

        if eChessBoard[pos] == ' ':
            eChessBoard[pos] = 'w' + piece
            printChessB(eChessBoard)
        else:
            print('This position is already taken.')


    else:

        while piece not in pieceLimits.keys():

            printChessB(eChessBoard)
            print(' What would you like to place?')

            piece = input()

            if piece == 'king' :
                bPieces.setdefault('king', 0)

                if bPieces['king'] < pieceLimits['king']:
                    bPieces['king'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'pawn':
                bPieces.setdefault('pawn', 0)

                if bPieces['pawn'] < pieceLimits['pawn']:
                    bPieces['pawn'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'bishop':
                bPieces.setdefault('bishop', 0)

                if bPieces['bishop'] < pieceLimits['bishop']:
                    bPieces['bishop'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'rook':
                bPieces.setdefault('rook', 0)

                if bPieces['rook'] < pieceLimits['rook']:
                    bPieces['rook'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'queen':
                bPieces.setdefault('queen', 0)

                if bPieces['queen'] < pieceLimits['queen']:
                    bPieces['queen'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue

            elif piece == 'knight':
                bPieces.setdefault('knight', 0)

                if bPieces['knight'] < pieceLimits['knight']:
                    bPieces['knight'] += 1
                else:
                    print('You have reached your placement limit for this piece')
                    piece = ' '
                    continue
            else:
                print('Input error: Not a piece')
        
        
        print('Where would you like to place your ' + piece + '?')

        pos = input()
        try:
            if eChessBoard[pos] == ' ':
                eChessBoard[pos] = 'b' + piece
                printChessB(eChessBoard)
            else:
                print('This position is already taken.')
        except KeyError:
            print('Invalid move: Out of Bounds')

        print('Are you done? y/n')
        
        ex = input()

        if ex == 'y':
            printChessB(eChessBoard)
            print('Goodbye!')
            sys.exit()
        



    



