commands = []
with open('aoc7data.txt') as f:
    commands = f.readlines()

commands = [c.strip('\n') for c in commands]

fs = { '/': { } }
current = ['/']

def getCurrent():
    res = fs
    for x in current:
        res = res.get(x)
    return res


mode = 'command'
for line in commands[1:]:
    parts = line.split(' ')
    if (parts[0] == '$'):
        mode = 'command'

    if mode == 'command':
        # command
        if (parts[1] == 'cd'):
            # change dir
            if (parts[2] == '..'):
                current.pop()
            else:
                current.append(parts[2])
        else:
            mode = 'data'
    elif mode == 'data':
        currentFs = getCurrent()
        # data entry
        if parts[0] == 'dir':
            currentFs[parts[1]] = {}
        else:
            currentFs[parts[1]] = int(parts[0])

# print(fs)


# problem 1
prob1Sum = 0
dirSums = []

def findSum(cfs):
    global prob1Sum
    global dirSums
    dirSum = 0
    for k in cfs.keys():
        if type(cfs[k]) == int:
            dirSum += cfs[k]
        else:
            dirSum += findSum(cfs[k])
    
    if dirSum <= 100000:
        prob1Sum += dirSum

    dirSums.append(dirSum)
    return dirSum

totalSum = findSum(fs)
# print(prob1Sum)

unusedSpace = 70000000 - totalSum
print(unusedSpace)


UNUSED_GOAL = 30000000
dirSums.sort()
print(dirSums)
for s in dirSums:
    if unusedSpace + s >= UNUSED_GOAL:
        print('answer! ' + str(s))
        break
