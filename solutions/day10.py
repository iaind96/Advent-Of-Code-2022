def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip() for line in file]
    return lines


def ParseCycles(program):
    cycles = []
    for instruction in program:
        match instruction[:4]:
            case 'noop':
                cycles.append(0)
            case 'addx':
                cycles.append(0)
                cycles.append(int(instruction[5:]))
    return cycles


def SignalStrengths(cycles, cyclesOfInterest):
    X = 1
    cycleCount = 1
    for cycle in cycles:
        if cycleCount in cyclesOfInterest:
            yield X * cycleCount
        cycleCount += 1
        X += cycle


def RenderCRT(cycles):
    X = 1
    pixels = []
    for pixelIndex, cycle in enumerate(cycles):
        pixelX = pixelIndex % 40
        if abs(X - pixelX) <= 1:
            pixels.append('#')
        else:
            pixels.append('.')
        X += cycle

    for pixelIndex in range(0, 241, 40):
        print(*pixels[pixelIndex:(pixelIndex+40)])


def RunProgram(program):

    cycles = ParseCycles(program)

    print(f'Sum of signal strengths = {sum(SignalStrengths(cycles, [20, 60, 100, 140, 180, 220]))}')

    RenderCRT(cycles)


if __name__ == '__main__':

    # program = ReadInput(r'../inputs/day10_example.txt')
    program = ReadInput(r'../inputs/day10.txt')

    RunProgram(program)

