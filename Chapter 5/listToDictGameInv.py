inve = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inv):
    itemCount = 0
    print('Inventory: ')
    for item in inv.keys():
        print(str(inv[item]) + ' ' + item )
        itemCount += inv[item]
    print('Total number of items: ' + str(itemCount))
    


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)

        inventory[item] += 1
    return inventory

    
displayInventory(inve)

inve = addToInventory(inve, dragonLoot)

displayInventory(inve)