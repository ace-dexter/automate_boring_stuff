def print_picnic(item_dict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth, '-'))
    for k, v in item_dict.items():
        print(k.ljust(leftwidth, '.') + k.rjust(rightwidth, ' '))


picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 20)
