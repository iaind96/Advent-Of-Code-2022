def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip().split() for line in file]
    return lines


def FollowKnot(leaderLocation, followerLocation):

    isDifferentRow = leaderLocation[1] != followerLocation[1]
    isDifferentColumn = leaderLocation[0] != followerLocation[0]

    rowDifference = leaderLocation[1] - followerLocation[1]
    columnDifference = leaderLocation[0] - followerLocation[0]

    if isDifferentRow and isDifferentColumn:
        if abs(columnDifference) > 1 or abs(rowDifference) > 1:
            if columnDifference > 0 and rowDifference > 0:
                followerLocation = (followerLocation[0] + 1, followerLocation[1] + 1)
            elif columnDifference > 0 and rowDifference < 0:
                followerLocation = (followerLocation[0] + 1, followerLocation[1] - 1)
            elif columnDifference < 0 and rowDifference > 0:
                followerLocation = (followerLocation[0] - 1, followerLocation[1] + 1)
            elif columnDifference < 0 and rowDifference < 0:
                followerLocation = (followerLocation[0] - 1, followerLocation[1] - 1)

    elif isDifferentRow:
        if rowDifference > 1:
            followerLocation = (followerLocation[0], followerLocation[1] + 1)
        elif rowDifference < -1:
            followerLocation = (followerLocation[0], followerLocation[1] - 1)
    elif isDifferentColumn:
        if columnDifference > 1:
            followerLocation = (followerLocation[0] + 1, followerLocation[1])
        elif columnDifference < -1:
            followerLocation = (followerLocation[0] - 1, followerLocation[1])

    return followerLocation


def ProcessMovements(movements, numberKnots):

    knotLocations = [(0, 0)] * numberKnots
    locationsVisitedByTail = {knotLocations[-1]}

    for movement in movements:
        for step in range(int(movement[1])):

            # first move the head
            headLocation = knotLocations[0]

            match movement[0]:
                case 'R':
                    headLocation = (headLocation[0] + 1, headLocation[1])
                case 'L':
                    headLocation = (headLocation[0] - 1, headLocation[1])
                case 'U':
                    headLocation = (headLocation[0], headLocation[1] + 1)
                case 'D':
                    headLocation = (headLocation[0], headLocation[1] - 1)

            knotLocations[0] = headLocation

            for knotIndex in range(1, numberKnots):
                knotLocations[knotIndex] = FollowKnot(knotLocations[knotIndex - 1], knotLocations[knotIndex])

            locationsVisitedByTail.add(knotLocations[-1])

    print(f'Total square visited by tail = {len(locationsVisitedByTail)}')


if __name__ == '__main__':

    # movements = ReadInput(r'../inputs/day9_example.txt')
    # movements = ReadInput(r'../inputs/day9_example2.txt')
    movements = ReadInput(r'../inputs/day9.txt')

    ProcessMovements(movements, 10)