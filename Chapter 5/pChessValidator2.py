
testChess = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3h': 'wking', '6d': 'bbishop'}

pieceLimits = {
    'pawn': 8, 'king': 1, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1
}

factions = ('b','w')

wPieces = {}
bPieces = {}

def isValidChessBoard(board):

    for x in board.keys():
        if int(x[0]) < 1 or int(x[0]) > 8:
            print('POSITIONING ERROR: Y OUT OF BOUNDS')
            return False

        if ord(x[1]) < 97 or ord(x[1]) > 104:
            
            print('POSITIONING ERROR: X OUT OF BOUNDS ' + x[1])
            return False

    for piece in board.values():
        
        if piece[1:] not in pieceLimits.keys():
            print('INVALID PIECE: ' + piece[1:])
            return False
            

        if piece[:1] not in factions:
            print('INVALID FACTION: ' + piece[:1])
            return False
        elif piece[:1] == 'w':
            wPieces.setdefault(piece[1:],0)
            wPieces[piece[1:]] += 1
            if wPieces[piece[1:]] > pieceLimits[piece[1:]]:
                print('EXCEEDED AMOUNT OF ' + piece[1:] +'s FOR WHITE')
                return False
        else:
            bPieces.setdefault(piece[1:],0)
            bPieces[piece[1:]] += 1
            if bPieces[piece[1:]] > pieceLimits[piece[1:]]:
                print('EXCEEDED AMOUNT OF ' + piece[1:] +'s FOR BLACK')
                return False
            
        

    return True


if not isValidChessBoard(testChess):
    print('IMPROPER CHESSBOARD NOTATION, CEASE YOUR HERESY')
else:
    print('Good chessing, carry on.')