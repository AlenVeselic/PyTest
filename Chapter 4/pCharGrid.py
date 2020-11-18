

grid=[]

for y in range(9):
    row=[]
    if y == 0 or y == 8:
        for x in range(6):
            row.append('.')
    elif y == 1 or y == 7:
        row. append('.')
        for x in range(2):
            row.append('0')
        for x in range(3):
            row.append('.')
    elif y == 2 or y == 6:
        for x in range(4):
            row.append('0')
        for x in range(2):
            row.append('.')
    elif y == 3 or y == 5:
        for x in range(5):
            row.append('0')
        row.append('.')
    elif y == 4 :
        row.append('.')
        for x in range(5):
            row.append('0')
    
    grid.append(row)

for y in range(len(grid[y])):
    for x in range(len(grid)):
        print(grid[x][y],end='')
    print()