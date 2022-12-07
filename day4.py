def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip() for line in file]
    assigments = [[tuple(map(int, x.split('-'))) for x in y.split(',')] for y in lines]
    return assigments


def IsSubSection(potentialSubSection, potentialSuperSection):
    return potentialSubSection[0] >= potentialSuperSection[0] and potentialSubSection[1] <= potentialSuperSection[1]


def IsOverlapping(sectionOne, sectionTwo):
    return sectionOne[0] in range(sectionTwo[0], sectionTwo[1] + 1) or sectionOne[1] in range(sectionTwo[0], sectionTwo[1] + 1)


def ProcessAssignments(assignments):
    fullyOverlappingAssignmentsCount = 0
    partiallyOverlappingAssignmentsCount = 0
    for assignment in assignments:
        isSectionOneSubSection = IsSubSection(assignment[0], assignment[1])
        isSectionTwoSubSection = IsSubSection(assignment[1], assignment[0])
        isPartiallyOverlapping = IsOverlapping(assignment[0], assignment[1])
        if isSectionOneSubSection or isSectionTwoSubSection:
            fullyOverlappingAssignmentsCount += 1
        if isPartiallyOverlapping or (isSectionOneSubSection or isSectionTwoSubSection):
            partiallyOverlappingAssignmentsCount += 1

    print(f'Total fully overlapping assignments = {fullyOverlappingAssignmentsCount}')

    print(f'Total partially overlapping assignments = {partiallyOverlappingAssignmentsCount}')


if __name__ == '__main__':

    # assignments = ReadInput(r'inputs\day4_example.txt')
    assignments = ReadInput(r'inputs\day4.txt')

    ProcessAssignments(assignments)

