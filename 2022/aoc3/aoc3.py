data = []
priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('aoc3data.txt') as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]

# problem 1
# data = list(map(lambda d : (d[:int(len(d)/2)], d[int(len(d)/2):]), data))

# score = 0
# for x in data:
#     for c in x[0]:
#         if c in x[1]:
#             score += priority.find(c) + 1
#             break

# print(score)

# problem 2
score = 0
for i in range(0, len(data), 3):
    for c in data[i]:
        if c in data[i+1] and c in data[i+2]:
            score += priority.find(c) + 1
            break

print(score)