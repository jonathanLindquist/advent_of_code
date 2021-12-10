class BitContainer:
    ones = 0
    zeros = 0

    def __init__(self) -> None:
        pass


lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()


def buildMap(lines, column):
    container = BitContainer()
    for i in range(len(lines)):
        line = lines[i]

        if line[column] == '1':
            container.ones += 1
        elif line[column] == '0':
            container.zeros += 1

    return container


oxygenList = lines.copy()

for i in range(len(lines[0])):
    container = buildMap(oxygenList, i)

    higherValue = None
    if container.ones >= container.zeros:
        higherValue = '1'
    else:
        higherValue = '0'

    print(f'Ones: {container.ones}, Zeros: {container.zeros}, Index: {i}')

    oxygenList = list(filter(
        lambda x: x[i] == higherValue,
        oxygenList
    ))

    print(oxygenList)
    if len(oxygenList) <= 1:
        break

c02List = lines.copy()

for i in range(len(lines[0])):
    container = buildMap(c02List, i)

    lowerValue = None
    if container.zeros <= container.ones:
        lowerValue = '0'
    else:
        lowerValue = '1'

    print(
        f'Ones: {container.ones}, Zeros: {container.zeros}, Index: {i}, LowerValue {lowerValue}')

    c02List = list(filter(
        lambda x: x[i] == lowerValue,
        c02List
    ))

    if len(c02List) <= 1:
        print(c02List)
        break

print(f'Oxygen: {oxygenList[0]}, Number: {int(oxygenList[0], 2)}')
print(f'C02: {c02List[0]}, Number: {int(c02List[0], 2)}')

print(int(oxygenList[0], 2) * int(c02List[0], 2))
