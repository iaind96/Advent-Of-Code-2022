def ReadInput(filepath):
    with open(filepath) as file:
        lines = file.read()
    crates, instructions = [x.split('\n') for x in lines.split('\n\n')]
    crates = ProcessCrates(crates)
    instructions = ProcessInstructions(instructions)
    return crates, instructions


def ProcessCrates(crates):
    numberCrates = len(crates[-1].split())
    stacks = [[] for _ in range(numberCrates)]
    for row in crates[-2::-1]:
        for index in range(numberCrates):
            crate = row[index * 4 + 1]
            if not crate.isspace():
                stacks[index].append(crate)
    return stacks


def ProcessInstructions(instructions):
    instructionsProcessed = []
    for instruction in instructions:
        instructionsProcessed.append([int(x) for x in instruction.split()[1::2]])
    return instructionsProcessed


def ArrangeCrates(crates, instructions):
    for instruction in instructions:
        count = instruction[0]
        source = crates[instruction[1] - 1]
        destination = crates[instruction[2] - 1]
        for crateIndex in range(count):
            crate = source.pop(len(source) - 1)
            destination.append(crate)

    print(f'Bottom crates are: {"".join([crate[-1] for crate in crates])}')


def ArrangeCrates2(crates, instructions):
    for instruction in instructions:
        count = instruction[0]
        source = crates[instruction[1] - 1]
        destination = crates[instruction[2] - 1]
        stackToMove = []
        for crateIndex in range(count):
            crate = source.pop(len(source) - 1)
            stackToMove.append(crate)
        destination.extend(stackToMove[::-1])

    print(f'Bottom crates are: {"".join([crate[-1] for crate in crates])}')


if __name__ == '__main__':

    # crates, instructions = ReadInput(r'inputs\day5_example.txt')
    crates, instructions = ReadInput(r'inputs\day5.txt')

    # ArrangeCrates(crates, instructions)
    ArrangeCrates2(crates, instructions)