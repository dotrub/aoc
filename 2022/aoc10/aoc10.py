input = []
with open('aoc10data.txt') as f:
    input = [l.rstrip() for l in f.readlines()]

x = 1
cycle = 1
screen = ['.' for _ in range(240)]
# solution = 0

def drawPixel():
    if x - 1 <= (cycle - 1) % 40 and x + 1 >= (cycle - 1) % 40:
        screen[cycle - 1] = '#'

def incCycle():
    global cycle
    drawPixel()
    # global solution
    # if (cycle - 20) % 40 == 0:
    #     solution += x * cycle
    cycle = (cycle % 241) + 1
    

for i in input:
    if i == 'noop':
        incCycle()
    else:
        incCycle()
        incCycle()
        x += int(i.split(' ')[1])

# print(solution)
for i in range(6):
    print(''.join(screen[i*40:(i+1)*40]))