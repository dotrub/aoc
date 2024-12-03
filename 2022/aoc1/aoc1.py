calories = []
with open('aoc1data.txt') as f:
    calories = f.readlines()

calSums = []
runSum = 0
for x in calories:
    if x == '\n':
        calSums.append(runSum)
        runSum = 0
    else:
        runSum += int(x)

largest = calSums[:3]
largest.sort()
for s in calSums[3:]:
    for idx, l in enumerate(largest):
        if s > l:
            largest.insert(idx, s)
            largest = largest[:3]
            break

print(sum(largest))