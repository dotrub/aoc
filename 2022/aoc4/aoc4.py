data = []

with open('aoc4data.txt') as f:
    data = f.readlines()

def readData(line):
    return (tuple(map(int, line[0].split('-'))), tuple(map(int, line[1].split('-'))))

data = [readData(d.strip('\n').split(',')) for d in data]

count1 = 0
count2 = 0
for x in data:
    print(x)
    # problem 1
    if (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (x[0][0] >= x[1][0] and x[0][1] <= x[1][1]):
        count1 += 1

    # problem 2
    if not(x[0][0] > x[1][1] or x[1][0] > x[0][1]):
        count2 += 1


print(count1)
print(count2)

