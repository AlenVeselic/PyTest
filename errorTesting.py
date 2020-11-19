eChessBoard = {
}

for x in range(8):
    for y in range(8):
         eChessBoard.setdefault(str(x + 1) + str(chr(97 + y)), '0')

for x in range(7,-2,-1):
    print('-'*17, end='')
    print()
    
    if( x > -1):
        for y in range(8):
            print('|', end='')
            print(eChessBoard[str(x + 1) + chr(97+y)], end='')
        print('| ',end='')    
        print(str(x + 1))
        
    else:
        for y in range(8):
            print(' ', end='')
            print(chr(97 + y), end='')
        # print('|', end='')   


        