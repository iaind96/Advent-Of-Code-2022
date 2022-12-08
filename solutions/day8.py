import numpy as np


def ReadInput(filepath):
    with open(filepath) as file:
        lines = [list(map(int, line.strip())) for line in file]
    return lines


def ScanTreeLine(treeLine):
    isVisible = np.zeros(shape=treeLine.shape, dtype=bool)
    maxSeenTreeHeight = -1
    for treeIndex in range(len(treeLine)):
        isVisible[treeIndex] = treeLine[treeIndex] > maxSeenTreeHeight
        maxSeenTreeHeight = max(maxSeenTreeHeight, treeLine[treeIndex])
    return isVisible


def FindVisibleTrees(heightMapArray):
    rows = []
    for treeLine in heightMapArray:
        rows.append(ScanTreeLine(treeLine))
    return np.array(rows)


def CalculateViewingDistances(treeLine):
    viewingDistances = np.zeros(shape=treeLine.shape)
    for treeIndex in range(len(treeLine)):
        viewingDistance = 0
        for tree in treeLine[(treeIndex + 1):]:
            viewingDistance += 1
            if tree >= treeLine[treeIndex]:
                break
        viewingDistances[treeIndex] = viewingDistance
    return viewingDistances


def FindViewingDistances(heightMapArray):
    rows = []
    for treeLine in heightMapArray:
        rows.append(CalculateViewingDistances(treeLine))
    return np.array(rows)


def ProcessHeightMap(heightMap):

    heightMapArray = np.array(heightMap)

    isVisibleLeft = FindVisibleTrees(heightMapArray)
    isVisibleRight = FindVisibleTrees(heightMapArray[:, ::-1])[:, ::-1]
    isVisibleTop = FindVisibleTrees(heightMapArray.T).T
    isVisibleBottom = FindVisibleTrees(heightMapArray.T[:, ::-1])[:, ::-1].T

    isVisibleAll = isVisibleLeft + isVisibleRight + isVisibleTop + isVisibleBottom

    print(f'Total visible trees = {isVisibleAll.sum()}')

    viewingDistancesRight = FindViewingDistances(heightMapArray)
    viewingDistancesLeft = FindViewingDistances(heightMapArray[:, ::-1])[:, ::-1]
    viewingDistancesBottom = FindViewingDistances(heightMapArray.T).T
    viewingDistancesTop = FindViewingDistances(heightMapArray.T[:, ::-1])[:, ::-1].T

    scenicScores = viewingDistancesRight * viewingDistancesLeft * viewingDistancesBottom * viewingDistancesTop

    print(f'Heighest scenic score = {scenicScores.astype(int).max()}')


if __name__ == '__main__':

    # heightMap = ReadInput(r'..\inputs\day8_example.txt')
    heightMap = ReadInput(r'..\inputs\day8.txt')

    ProcessHeightMap(heightMap)
