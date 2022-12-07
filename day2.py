
shapeScores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

resultScores = {
    'win': 6,
    'tie': 3,
    'loss': 0,
    'X': 0,
    'Y': 3,
    'Z': 6
}

resultMapping = {
    'X': {'A': 'tie', 'B': 'loss', 'C': 'win'},
    'Y': {'A': 'win', 'B': 'tie', 'C': 'loss'},
    'Z': {'A': 'loss', 'B': 'win', 'C': 'tie'}
}

strategyMapping = {
    'X': {'A': 'Z', 'B': 'X', 'C': 'Y'}, # loss
    'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'}, # draw
    'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'} # win
}


def ReadInput(filepath):
    with open(filepath) as file:
        lines = [line.strip().split() for line in file]
    return lines


def ScoreGame(strategy):
    score = 0

    for round in strategy:
        shapeScore = shapeScores[round[1]]

        result = resultMapping[round[1]][round[0]]
        resultScore = resultScores[result]

        score += shapeScore + resultScore

    print(f'Final score = {score}')


def ScoreGame2(strategy):
    score = 0

    for round in strategy:
        shape = strategyMapping[round[1]][round[0]]

        shapeScore = shapeScores[shape]

        resultScore = resultScores[round[1]]

        score += shapeScore + resultScore

    print(f'Final score = {score}')


if __name__ == '__main__':

    # strategy = ReadInput(r'inputs/day2_example.txt')
    strategy = ReadInput(r'inputs/day2.txt')

    # ScoreGame(strategy)
    ScoreGame2(strategy)