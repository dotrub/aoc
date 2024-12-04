input = []

with open("aoc4data.txt") as f:
    input = [l.rstrip() for l in f.readlines()]


def isXmas(x, y):
    s1 = input[x - 1][y - 1] + input[x][y] + input[x + 1][y + 1]
    s2 = input[x + 1][y - 1] + input[x][y] + input[x - 1][y + 1]
    if (s1 == "MAS" or s1[::-1] == "MAS") and (s2 == "MAS" or s2[::-1] == "MAS"):
        return 1
    return 0


matches = 0
for i, row in enumerate(input[:-2], 1):
    for j, _ in enumerate(row[:-2], 1):
        if input[j][i] == "A":
            matches += isXmas(j, i)

print(matches)
