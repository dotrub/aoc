input = []
with open("aoc6data.txt") as f:
    input = [list(l.rstrip()) for l in f.readlines()]

initPos = []
initDir = ""
initPathSet = set()
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col == "<" or col == ">" or col == "^" or col == "v":
            initPos = [i, j]
            initDir = col
            initPathSet.add((i, j, initDir))


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


loops = 0
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col != ".":
            continue
        input[i][j] = "#"
        pathSet = initPathSet.copy()
        done = False
        pos = initPos.copy()
        dir = initDir
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
                if (nextPos[0], nextPos[1], dir) in pathSet:
                    loops += 1
                    break
                pathSet.add((nextPos[0], nextPos[1], dir))
                pos = nextPos
        input[i][j] = "."

print(loops)
