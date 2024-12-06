input = []
with open("aoc6data.txt") as f:
    input = [list(l.rstrip()) for l in f.readlines()]

pos = []
dir = ""
visited = 1
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col == "<" or col == ">" or col == "^" or col == "v":
            pos = [i, j]
            dir = col
            input[i][j] = "X"


def getNextPos(pos, dir):
    if dir == "^":
        return [pos[0] - 1, pos[1]]
    if dir == "v":
        return [pos[0] + 1, pos[1]]
    if dir == ">":
        return [pos[0], pos[1] + 1]
    if dir == "<":
        return [pos[0], pos[1] - 1]


clockwise = ["^", ">", "v", "<"]


def turnRight(dir):
    return clockwise[(clockwise.index(dir) + 1) % 4]


while True:
    nextPos = getNextPos(pos, dir)
    if (
        nextPos[0] < 0
        or nextPos[0] >= len(input)
        or nextPos[1] < 0
        or nextPos[1] >= len(input[0])
    ):
        break
    nextChar = input[nextPos[0]][nextPos[1]]
    if nextChar == "#":
        dir = turnRight(dir)
    else:
        if nextChar == ".":
            input[nextPos[0]][nextPos[1]] = "X"
            visited += 1
        pos = nextPos

print(visited)
