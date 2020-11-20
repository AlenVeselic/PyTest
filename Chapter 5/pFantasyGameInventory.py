inve = { 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }


def displayInventory(inv):
    itemCount = 0
    print('Inventory: ')
    for item in inv.keys():
        print(str(inv[item]) + ' ' + item )
        itemCount += inv[item]
    print('Total number of items: ' + str(itemCount))

displayInventory(inve)