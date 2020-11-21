tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats',' moose', 'goose']]

def printTable(table):

    colLength = [0] * len(table)

    for itemList in range(len(table)):
        for item in table[itemList]:
            if len(item) > colLength[itemList]:
                colLength[itemList] = len(item)
            
    for lists in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][lists].rjust(colLength[item]), end=' ')
        print()


printTable(tableData)