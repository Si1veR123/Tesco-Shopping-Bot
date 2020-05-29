def edit_items(items):
    print('\n')
    for i in items:
        print(i)
    print('\n')

    while True:

        choice = input("Item to remove ('end'): ").lower()
        if choice == 'end':
            print('\n')
            return items
        else:
            try:
                items.remove(choice)
                print('Removed: ', choice)
            except ValueError:
                print(f'Item {choice} not in list')


def add_items():
    items = []

    while True:
        item = input("Item ('end', 'edit'): ").lower()
        if item == 'end':
            break
        elif item == 'edit':
            items = edit_items(items)
        else:
            items.append(item)
    return items
