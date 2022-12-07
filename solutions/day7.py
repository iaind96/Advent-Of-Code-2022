
def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip() for line in file]
    return lines


def FindDirectoryStructure(terminalOutput):
    directoryStructure = {}
    while True:
        if len(terminalOutput) == 0:
            return directoryStructure
        currentLine = terminalOutput.pop(0)
        lineComponents = currentLine.split()
        if lineComponents[0] == '$':
            if lineComponents[1] == 'cd':
                if lineComponents[2] == '..':
                    return directoryStructure
                else:
                    directoryStructure[lineComponents[2]] = FindDirectoryStructure(terminalOutput)
            elif lineComponents[1] == 'ls':
                pass
        else:
            if lineComponents[0] == 'dir':
                pass
            else:
                directoryStructure[lineComponents[1]] = int(lineComponents[0])


def FindDirectorySizes(directoryStructure, directorySizes=None):
    if directorySizes is None:
        directorySizes = []
    currentSize = 0
    for item in directoryStructure:
        if isinstance(directoryStructure[item], int):
            currentSize += directoryStructure[item]
        else:
            subDirectorySize, directorySizes = FindDirectorySizes(directoryStructure[item], directorySizes)
            directorySizes.append(subDirectorySize)
            currentSize += subDirectorySize
    return currentSize, directorySizes


def ProcessTerminalOutput(terminalOutput):

    directoryStructure = FindDirectoryStructure(terminalOutput)

    directorySizeThreshold = 10000
    totalDiskSpace = 70000000
    updateDiskSapce = 30000000

    totalSize, directorySizes = FindDirectorySizes(directoryStructure)

    totalSizeBelowThreshold = 0

    for directorySize in directorySizes:
        if directorySize <= directorySizeThreshold:
            totalSizeBelowThreshold += directorySize

    print(f'Total directory size below {directorySizeThreshold} = {totalSizeBelowThreshold}')

    remainingDiskSpace = totalDiskSpace - totalSize
    requiredDiskSpace = updateDiskSapce - remainingDiskSpace

    directorySizesSorted = sorted(directorySizes)
    directoryIndex = 0
    while True:
        if directorySizesSorted[directoryIndex] >= requiredDiskSpace:
            directorySizeToDelete = directorySizesSorted[directoryIndex]
            break
        directoryIndex += 1

    print(f'Smallest directory to delete size = {directorySizeToDelete}')


if __name__ == '__main__':

    # terminalOutput = ReadInput(r'inputs\day7_example.txt')
    terminalOutput = ReadInput(r'../inputs/day7.txt')

    ProcessTerminalOutput(terminalOutput)

