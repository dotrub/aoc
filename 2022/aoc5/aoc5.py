STACK_COUNT = 9
COLUMN_WIDTH = 4

data = []
with open('aoc5data.txt') as f:
    data = f.readlines()

# put stacks in dictionary of lists, keyed by column number
def interpretDrawing(start):
    result = {}
    for i in range(STACK_COUNT):
        result[str(i + 1)] = []
    for line in start:
        for column in range(STACK_COUNT):
            if not line[column * COLUMN_WIDTH + 1] == ' ':
                result[str(column + 1)].append(line[column * COLUMN_WIDTH + 1])
            

    return result

splitIndex = data.index('\n')
drawing = [d.strip('\n') for d in data[:splitIndex]]
input = [d.strip('\n') for d in data[splitIndex+1:]]

stacks = interpretDrawing(drawing[:-1])

# input as tuples of relevant data
input = [(int(i[1]), i[3], i[5]) for i in [l.split(' ') for l in input]]

# problem 1
# for x in input:
#     for n in range(x[0]):
#         fromColumn = x[1]
#         toColumn = x[2]
#         valueToMove = stacks[fromColumn][0]
#         stacks[fromColumn] = stacks[fromColumn][1:]
#         stacks[toColumn] = [valueToMove] + stacks[toColumn]

# problem 2
for x in input:
    fromColumn = x[1]
    toColumn = x[2]
    valueToMove = stacks[fromColumn][:x[0]]
    stacks[fromColumn] = stacks[fromColumn][x[0]:]
    stacks[toColumn] = valueToMove + stacks[toColumn]

result = ''
for key in range(1, 10):
    result += stacks[str(key)][0]
print(result)


