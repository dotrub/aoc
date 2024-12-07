input = []

with open("aoc7data.txt") as f:
    input = [l.rstrip().split(": ") for l in f.readlines()]


validSum = 0
for i in input:
    testAnswer = int(i[0])
    exp = [int(x) for x in i[1].split(" ")]
    answerSet = [exp[0]]
    for e in exp[1:]:
        nextAnswerSet = []
        for a in answerSet:
            nextAnswerSet += [a * e, a + e, int(str(a) + str(e))]
        answerSet = nextAnswerSet
    if testAnswer in answerSet:
        validSum += testAnswer
print(validSum)
