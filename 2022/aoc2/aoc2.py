data = []
with open('aoc2data.txt') as f:
    data = f.readlines()

def convertLetterToScore(letter):
    if letter == 'A' or letter == 'X':
        return 1
    if letter == 'B' or letter == 'Y':
        return 2
    if letter == 'C' or letter == 'Z':
        return 3

# find score of round
def calcOutcomeScoreProb1(round):
    if round[0] == round[1]:
        # draw
        return 3
    if round[0] == 1 and round[1] == 3:
        # lose case 1
        return 0
    if round[0] == 3 and round[1] == 1:
        # win case 1
        return 6
    if round[0] > round[1]:
        # lose case 2
        return 0
    # else win
    return 6

# find score of my choice
def calcOutcomeScoreProb2(round):
    if round[1] == 2:
        # draw
        return round[0]
    if round[1] == 3:
        # win
        if round[0] == 3:
            return 1
        return round[0] + 1
    if round[1] == 1:
        # lose
        if round[0] == 1:
            return 3
        return round[0] - 1



data = list(map(lambda d : tuple(map(convertLetterToScore, d.strip('\n').split(' '))), data))

score = 0
for round in data:
    # score += calcOutcomeScoreProb1(round) + round[1]
    score += calcOutcomeScoreProb2(round) + ((round[1] - 1) * 3)

print(score)