class Monkey:
    inspectCount = 0

    def __init__(self, items, operation, test, trueCase, falseCase):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueCase = trueCase
        self.falseCase = falseCase

    def inspect(self, item):
        self.inspectCount += 1
        op = self.operation.replace('old', f'int({item})')
        return eval(f'int({item}) {op}') // 3

    def testItem(self, item):
        if item % self.test == 0:
            return self.trueCase
        else:
            return self.falseCase
    
    def addItem(self, item):
        self.items.append(item)
        

monkeys = []
input = []
with open('aoc11data.txt') as f:
    input = [l.rstrip() for l in f.readlines()]

def initializeMonkeys():
    items = []
    operation = ''
    test = 0
    trueCase = 0
    falseCase = 0
    for i in input:
        # print(i)
        if i == '':
            monkeys.append(Monkey(items, operation, test, trueCase, falseCase))
        if 'Starting items:' in i:
            items = i.replace('  Starting items: ', '').split(', ')
        if 'Operation:' in i:
            operation = i.replace('  Operation: new = old ', '')
        if 'Test:' in i:
            test = int(i.replace('  Test: divisible by ', ''))
        if 'If true' in i:
            trueCase = int(i.replace('    If true: throw to monkey ', ''))
        if 'If false' in i:
            falseCase = int(i.replace('    If false: throw to monkey ', ''))

initializeMonkeys()

# print(input)
# print(monkeys)

for _ in range(1000):
    for m in monkeys:
        while len(m.items) > 0:
            item = m.items.pop(0)
            item = m.inspect(item)
            throwTo = m.testItem(item)
            monkeys[throwTo].addItem(item)

for m in monkeys:
    print(m.inspectCount)