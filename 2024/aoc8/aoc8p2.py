input = []

with open("aoc8data.txt") as f:
    input = [l.rstrip() for l in f.readlines()]

gridHeight = len(input)
gridWidth = len(input[0])

antennaLocations = {}
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col != ".":
            if col in antennaLocations:
                antennaLocations[col].append((i, j))
            else:
                antennaLocations[col] = [(i, j)]


antinodes = set()


def findAntinodes(a1, a2):
    dy = a2[0] - a1[0]
    dx = a2[1] - a1[1]
    testX = a1[1]
    testY = a1[0]
    while (
        testX >= 0 and testX <= gridWidth - 1 and testY >= 0 and testY <= gridHeight - 1
    ):
        antinodes.add((testX, testY))
        testX -= dx
        testY -= dy
    testX = a1[1] + dx
    testY = a1[0] + dy
    while (
        testX >= 0 and testX <= gridWidth - 1 and testY >= 0 and testY <= gridHeight - 1
    ):
        antinodes.add((testX, testY))
        testX += dx
        testY += dy


for antennas in antennaLocations.values():
    for m in range(len(antennas) - 1):
        for n in range(m + 1, len(antennas)):
            findAntinodes(antennas[m], antennas[n])

print(len(antinodes))
