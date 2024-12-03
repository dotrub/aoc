input = []
with open('aoc9data.txt') as f:
    input = [l.rstrip() for l in f.readlines()]

# print(input)
rope = [[0,0] for _ in range(10)]
headpos = [0, 0]
tailpos = [0, 0]
visited = set()

def recordTailPos():
    # visited.add(tuple(tailpos))
    visited.add(tuple(rope[-1]))

def updateRope():
    for i in range(1,10):
        prevSeg = rope[i-1]
        segment = rope[i]
        horizontalDiff = prevSeg[0]-segment[0]
        verticalDiff = prevSeg[1]-segment[1]
        touching = abs(horizontalDiff) <= 1 and abs(verticalDiff) <= 1
        if not touching:
            if not (horizontalDiff == 0 or verticalDiff == 0):
                # diagonal
                if horizontalDiff > 0:
                    rope[i][0] += 1
                else:
                    rope[i][0] -= 1

                if verticalDiff > 0:
                    rope[i][1] += 1
                else:
                    rope[i][1] -= 1
                
            else:
                # along row or column
                if verticalDiff == 0:
                    if horizontalDiff > 0:
                        rope[i][0] += 1
                    else:
                        rope[i][0] -= 1
                else:
                    if verticalDiff > 0:
                        rope[i][1] += 1
                    else:
                        rope[i][1] -= 1
    recordTailPos()


def moveHead(move):
    dis = int(move[1])
    dir = move[0]
    for _ in range(dis):
        if dir == 'R':
            # headpos[0] += 1
            rope[0][0] += 1
        if dir == 'L':
            # headpos[0] -= 1
            rope[0][0] -= 1
        if dir == 'D':
            # headpos[1] += 1
            rope[0][1] += 1
        if dir == 'U':
            # headpos[1] -= 1
            rope[0][1] -= 1
        # moveTail()
        updateRope()
    

def moveTail():
    horizontalDiff = headpos[0]-tailpos[0]
    verticalDiff = headpos[1]-tailpos[1]
    touching = abs(horizontalDiff) <= 1 and abs(verticalDiff) <= 1
    if not touching:
        if not (horizontalDiff == 0 or verticalDiff == 0):
            # diagonal
            if horizontalDiff > 0:
                tailpos[0] += 1
            else:
                tailpos[0] -= 1

            if verticalDiff > 0:
                tailpos[1] += 1
            else:
                tailpos[1] -= 1
            
        else:
            # along row or column
            if verticalDiff == 0:
                if horizontalDiff > 0:
                    tailpos[0] += 1
                else:
                    tailpos[0] -= 1
            else:
                if verticalDiff > 0:
                    tailpos[1] += 1
                else:
                    tailpos[1] -= 1
    recordTailPos()



for line in input:
    move = line.split(' ')
    moveHead(move)
    # moveTail()


# print(headpos)
# print(tailpos)
# print(visited)
print(len(visited))