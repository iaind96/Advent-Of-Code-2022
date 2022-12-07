def ReadInput(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def ProcessInventory(inventoryUnprocessed):
    inventories = []
    currentInventory = 0
    for item in inventoryUnprocessed:
        if not item:
            inventories.append(currentInventory)
            currentInventory = 0
        else:
            currentInventory += int(item)
    inventories.append(currentInventory)

    print(f'Maximum calories = {max(inventories)}')

    inventoriesSorted = sorted(inventories)

    print(f'Top 3 total calories = {sum(inventoriesSorted[-3:])}')


# def ReadInput(filepath):
#     with open(filepath) as file:
#         lines = file.read()
#     return lines
#
#
# def ProcessInventory(inventoryUnprocessed):
#     inventories = inventoryUnprocessed.split('\n\n')
#     inventoriesTotal = []
#     for inventory in inventories:
#         items = inventory.split('\n')
#         inventoriesTotal.append(sum([int(x) for x in items]))
#
#     print(inventoriesTotal)
#
#     print(f'Maximum calories = {max(inventoriesTotal)}')
#
#     inventoriesSorted = sorted(inventoriesTotal)
#
#     print(f'Top 3 total calories = {sum(inventoriesSorted[-3:])}')


if __name__ == '__main__':

    invetoryUnprocessed = ReadInput(r'../inputs/day1_example.txt')
    # invetoryUnprocessed = ReadInput(r'inputs/day1.txt')

    ProcessInventory(invetoryUnprocessed)
