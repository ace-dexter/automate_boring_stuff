def display_inventory(stuffs):
    num_items = 0
    print('Inventory:')
    for k,v in stuffs.items():
        num_items = num_items + v
        print(v, ' ', k)
    print('Total number of items: ', num_items)


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if (item in inventory) is False:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
