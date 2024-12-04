input = []

with open("aoc4data.txt") as f:
    input = [l.rstrip() for l in f.readlines()]


def check(startx, starty, directionx, directiony):
    if (
        startx + 3 * directionx < 0
        or startx + 3 * directionx > len(input) - 1
        or starty + 3 * directiony < 0
        or starty + 3 * directiony > len(input) - 1
    ):
        return False

    return (
        input[startx][starty]
        + input[startx + 1 * directionx][starty + 1 * directiony]
        + input[startx + 2 * directionx][starty + 2 * directiony]
        + input[startx + 3 * directionx][starty + 3 * directiony]
    ) == "XMAS"


def searchMatches(x, y):
    return (
        check(x, y, 0, 1)
        + check(x, y, 1, 0)
        + check(x, y, 0, -1)
        + check(x, y, -1, 0)
        + check(x, y, 1, 1)
        + check(x, y, -1, 1)
        + check(x, y, -1, -1)
        + check(x, y, 1, -1)
    )


matches = 0
for i, row in enumerate(input):
    for j, col in enumerate(row):
        if col == "X":
            matches += searchMatches(i, j)

print(matches)
