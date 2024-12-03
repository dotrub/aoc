import re

input = ""
with open("aoc3data.txt") as f:
    input = f.read()

searchExp = r"mul\(\d{1,3}?,\d{1,3}?\)"

print(re.findall(searchExp, input))
commands = [[int(n) for n in c[4:-1].split(",")] for c in re.findall(searchExp, input)]

answer = 0
for c in commands:
    answer += c[0] * c[1]

print(answer)

searchExp = r"mul\(\d{1,3}?,\d{1,3}?\)|do(?:n't)?\(\)"
commands = [str(c) for c in re.findall(searchExp, input)]
answer = 0
do = True
for c in commands:
    if c == "do()":
        do = True
    if c == "don't()":
        do = False
    if do and c.startswith("mul("):
        params = [int(n) for n in c[4:-1].split(",")]
        answer += params[0] * params[1]
print(answer)
