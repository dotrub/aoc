input = []

with open("aoc5data.txt") as f:
    input = [l.rstrip() for l in f.readlines()]

breakChar = input.index("")
rules = [[int(y) for y in x.split("|")] for x in input[:breakChar]]
updates = [[int(y) for y in x.split(",")] for x in input[breakChar + 1 :]]
# print(rules)
# print(updates)


# PART 1
def rightOrder(u):
    isRight = True
    for r in rules:
        try:
            if u.index(r[0]) > u.index(r[1]):
                isRight = False
                break
        except ValueError:
            pass

    return isRight


answer = 0
wrongOrderUpdates = []
for u in updates:
    if rightOrder(u):
        answer += u[len(u) // 2]
    else:
        wrongOrderUpdates.append(u)

print(f"Part 1 Answer: {answer}")
# PART 2

answer2 = 0
for update in wrongOrderUpdates:
    fixedUpdate = [u for u in update]
    for page in update:
        for r in rules:
            try:
                if r[0] == page and fixedUpdate.index(r[1]) < fixedUpdate.index(r[0]):
                    fixedUpdate.remove(r[1])
                    sliceIndex = fixedUpdate.index(r[0])
                    fixedUpdate = (
                        fixedUpdate[: sliceIndex + 1]
                        + [r[1]]
                        + fixedUpdate[sliceIndex + 1 :]
                    )
                if r[1] == page and fixedUpdate.index(r[0]) > fixedUpdate.index(r[1]):
                    fixedUpdate.remove(r[0])
                    sliceIndex = fixedUpdate.index(r[1])
                    fixedUpdate = (
                        fixedUpdate[:sliceIndex] + [r[0]] + fixedUpdate[sliceIndex:]
                    )
            except ValueError:
                pass

    answer2 += fixedUpdate[len(fixedUpdate) // 2]

print(f"Part 2 Answer: {answer2}")
