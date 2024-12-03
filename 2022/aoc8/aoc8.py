map = []
with open('aoc8data.txt') as f:
    map = [l.rstrip() for l in f.readlines()]

# assuming its square
length = len(map)

visibility = [[False for _ in range(length)] for _ in range(length)]

colMaxT = [-1 for _ in range(length)]
colMaxB = [-1 for _ in range(length)]
for i in range(length):
    rowMaxL = -1
    rowMaxR = -1
    for j in range(length):
        # from top-left
        topLeftValue = int(map[i][j])
        if topLeftValue > rowMaxL:
            visibility[i][j] = True
            rowMaxL = topLeftValue
        if topLeftValue > colMaxT[j]:
            visibility[i][j] = True
            colMaxT[j] = topLeftValue

        # from bottom-right
        flipRowInx = length - (i + 1)
        flipColInx = length - (j + 1)
        bottomRightValue = int(map[flipRowInx][flipColInx])
        if bottomRightValue > rowMaxR:
            visibility[flipRowInx][flipColInx] = True
            rowMaxR = bottomRightValue
        if bottomRightValue > colMaxB[flipColInx]:
            visibility[flipRowInx][flipColInx] = True
            colMaxB[flipColInx] = bottomRightValue

visibleCount = 0
for i in range(length):
    for j in range(length):
        if visibility[i][j] == True:
            visibleCount += 1
print(visibleCount)

maxScore = 0
maxI = 0
maxJ = 0
p = False
for i in range(length):
    for j in range(length):
        if i == 59 and j == 31:
            p = True
        else:
            p = False
        # up
        searching = not i == 0
        uScore = 0
        count = 1
        while searching:
            uScore += 1
            if i - count == 0 or int(map[i - count][j]) >= int(map[i][j]):
                searching = False
            count += 1

        # down
        searching = not i == length - 1
        dScore = 0
        count = 1
        while searching:
            dScore += 1
            if i + count == length - 1 or int(map[i + count][j]) >= int(map[i][j]):
                searching = False
            count += 1
        
        # left
        searching = not j == 0
        lScore = 0
        count = 1
        while searching:
            lScore += 1
            # if p == True:
            #     print(map[i][j-count])
            if j - count == 0 or int(map[i][j - count]) >= int(map[i][j]):
                searching = False
            count += 1
        
        # right
        searching = not j == length - 1
        rScore = 0
        count = 1
        while searching:
            rScore += 1
            if j + count == length - 1 or int(map[i][j + count]) >= int(map[i][j]):
                searching = False
            count += 1

        if p:
            print(f'uScore: {uScore}')
            print(f'dScore: {dScore}')
            print(f'lScore: {lScore}')
            print(f'rScore: {rScore}')
        score = uScore * dScore * lScore * rScore
        # print(f'[{i}][{j}]: {score}')
        if score > maxScore:
            maxScore = score
            maxI = i
            maxJ = j

print(map[maxI][maxJ])
print(map[59])
print(f'Max at [{maxI}][{maxJ}]: {maxScore}')