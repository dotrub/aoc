input = []

with open("aoc1data.txt") as f:
    input = [l.rstrip() for l in f.readlines()]

list1 = []
list2 = []
for i in input:
    splitRow = i.split()
    list1.append(int(splitRow[0]))
    list2.append(int(splitRow[1]))

list1.sort()
list2.sort()

sum = 0
for i in list1:
    occCount = 0
    for j in list2:
        if i == j:
            occCount += 1
    sum += i * occCount

print(sum)
