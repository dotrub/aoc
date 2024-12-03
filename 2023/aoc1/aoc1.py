# # PART 1
# # input = []
# # with open('aoc1data.txt') as f:
# #     input = [''.join(c for c in l.rstrip() if c.isdigit()) for l in f.readlines()]

# # sum = 0
# # for n in input:
# #     sum += int(n[0] + n[-1])

# # print(sum)

# PART 2
input = []
with open('aoc1data.txt') as f:
    input = [l.rstrip() for l in f.readlines()]

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def replaceDigitText(line):
    replacedText = line
    foundDigits = [(d, line.find(d)) for d in digits if line.find(d) != -1]
    foundDigits.sort(key=lambda idxOfDigit: idxOfDigit[1])
    # print(foundDigits)
    for fD in foundDigits:
        replacedText = replacedText.replace(fD[0], f'{digits.index(fD[0]) + 1}')
    # if len(foundDigits) > 0:
    #     replacedText = replacedText.replace(foundDigits[0][0], f'{digits.index(foundDigits[0][0]) + 1}')
    #     replacedText = replacedText.replace(foundDigits[-1][0], f'{digits.index(foundDigits[-1][0]) + 1}')
    return replacedText

# print(replaceDigitText('eightwone'))

sum = 0
for idx_n, n in enumerate(input):
    # print(n)
    transform_value = replaceDigitText(n)
    # print(transform_value)
    transform_value = ''.join(c for c in transform_value if c.isdigit())
    # print(transform_value)
    # input[idx_n] = transform_value
    print(f'{n} {transform_value} {int(transform_value[0] + transform_value[-1])}')
    sum += int(transform_value[0] + transform_value[-1])
    # print(sum)

# print(input)
print(sum)