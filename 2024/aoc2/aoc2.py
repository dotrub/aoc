input = []
with open("aoc2data.txt") as f:
    input = [[int(x) for x in l.rstrip().split(" ")] for l in f.readlines()]


def isNegative(x):
    if x < 0:
        return True
    return False


def xor(a, b):
    return (a and not b) or (not a and b)


def isSafe(report):
    firstDiff = report[1] - report[0]
    if abs(firstDiff) < 1 or abs(firstDiff) > 3:
        return False
    prevLevel = report[1]
    safe = True
    for level in report[2:]:
        diff = level - prevLevel
        if (
            abs(diff) < 1
            or abs(diff) > 3
            or xor(isNegative(diff), isNegative(firstDiff))
        ):
            safe = False
            break
        prevLevel = level
    return safe


safeCount = 0
for report in input:
    safe = False
    for x in range(len(report)):
        if isSafe(report[:x] + report[x + 1 :]):
            safe = True
            break

    if safe:
        safeCount += 1


print(safeCount)
