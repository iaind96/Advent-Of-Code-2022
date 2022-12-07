
def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip() for line in file]
    return lines


def PrioritiseItem(item):
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96


def GroupRucksacks(rucksacks, groupSize):
    for index in range(0, len(rucksacks), groupSize):
        yield rucksacks[index:(index + groupSize)]


def ProcessRucksacks(rucksacks):
    priorityTotal = 0
    for rucksack in rucksacks:
        midPoint = int(len(rucksack) / 2)
        compartmentOne = rucksack[:midPoint]
        compartmentTwo = rucksack[midPoint:]
        commonItems = list(set(compartmentOne).intersection(set(compartmentTwo)))
        if len(commonItems) != 1:
            raise Exception(f'More than one common item: {commonItems}')
        priority = PrioritiseItem(commonItems[0])
        priorityTotal += priority

    print(f'Total priority = {priorityTotal}')


def ProcessGroups(rucksacks):
    priorityTotal = 0
    for group in GroupRucksacks(rucksacks, 3):
        rucksacks = [set(rucksack) for rucksack in group]
        commonItems = list(set.intersection(*rucksacks))
        if len(commonItems) != 1:
            raise Exception(f'More than one common item: {commonItems}')
        priority = PrioritiseItem(commonItems[0])
        priorityTotal += priority

    print(f'Total priority = {priorityTotal}')


if __name__ == '__main__':

    # rucksacks = ReadInput(r'inputs\day3_example.txt')
    rucksacks = ReadInput(r'../inputs/day3.txt')

    # ProcessRucksacks(rucksacks)
    ProcessGroups(rucksacks)