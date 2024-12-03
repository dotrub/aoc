data = ''
with open('aoc6data.txt') as f:
    data = f.readline()

def checkPacket(pack):
    for i in range(14):
        if pack[i] in pack[i+1:]:
            return False
    return True

x = 13
packet = data[:13]
for c in data[13:]:
    if checkPacket(packet + c):
        break
    packet = packet[1:] + c
    x += 1

print(x+1)