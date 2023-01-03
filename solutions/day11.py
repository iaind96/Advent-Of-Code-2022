from functools import reduce


def ReadInput(filepath):
    with open(filepath) as file:
        monkeys = file.read().split('\n\n')
    return monkeys


class Monkey:

    def __init__(self, monkeyString):
        monkeyStringParts = monkeyString.split('\n')

        self.items = list(map(int, monkeyStringParts[1].split(':')[1].split(', ')))

        match monkeyStringParts[2].split(':')[1].split()[3:]:
            case ['+', 'old']:
                self.operation = lambda x: x + x
            case ['*', 'old']:
                self.operation = lambda x: x * x
            case ['+', y]:
                self.operation = lambda x: x + int(y)
            case ['*', y]:
                self.operation = lambda x: x * int(y)

        self.testDivisor = int(monkeyStringParts[3].split(':')[1].split()[2])

        self.monkeyIndexIfTrue = int(monkeyStringParts[4].split()[-1])
        self.monkeyIndexIfFalse = int(monkeyStringParts[5].split()[-1])

        self.numberOfInspections = 0

    def HasItems(self):
        return len(self.items) != 0

    def ReceiveItem(self, item):
        self.items.append(item)

    def InspectFirstItemPartOne(self):
        if not self.HasItems():
            raise Exception('Monkey has no items to inspect!')

        item = self.items.pop(0)
        item = self.operation(item)
        item = int(item / 3)

        if item % self.testDivisor == 0:
            monkeyIndex =  self.monkeyIndexIfTrue
        else:
            monkeyIndex = self.monkeyIndexIfFalse

        self.numberOfInspections += 1

        return item, monkeyIndex

    def InspectFirstItemPartTwo(self, divisor):
        if not self.HasItems():
            raise Exception('Monkey has no items to inspect!')

        item = self.items.pop(0)
        remainder = item % divisor
        remainder = self.operation(remainder)

        if remainder % self.testDivisor == 0:
            monkeyIndex = self.monkeyIndexIfTrue
        else:
            monkeyIndex = self.monkeyIndexIfFalse

        self.numberOfInspections += 1

        return remainder, monkeyIndex


def PlayGame(monkeyStrings, numberOfRounds):

    monkeys = [Monkey(monkeyString) for monkeyString in monkeyStrings]

    divisorLCM = reduce(lambda x, y: x * y, map(lambda x: x.testDivisor, monkeys))

    for roundIndex in range(numberOfRounds):
        for monkey in monkeys:
            while monkey.HasItems():
                # item, receivingMonkeyIndex = monkey.InspectFirstItemPartOne()
                item, receivingMonkeyIndex = monkey.InspectFirstItemPartTwo(divisorLCM)
                monkeys[receivingMonkeyIndex].ReceiveItem(item)
        if roundIndex % 100 == 0:
            print(f'Round {roundIndex} complete')

    monkeyInspectionCounts = list(map(lambda x: x.numberOfInspections, monkeys))

    print(monkeyInspectionCounts)

    monkeyInspectionCountsSorted = sorted(monkeyInspectionCounts)

    print(f'Level of monkey business = {monkeyInspectionCountsSorted[-2] * monkeyInspectionCountsSorted[-1]}')



if __name__ == '__main__':

    # monkeyStrings = ReadInput(r'..\inputs\day11_example.txt')
    monkeyStrings = ReadInput(r'..\inputs\day11.txt')

    PlayGame(monkeyStrings, 10000)

