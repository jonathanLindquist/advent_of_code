class BitContainer:
    ones = 0
    zeros = 0

    def __init__(self) -> None:
        pass


lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

hashMap = dict()

for i in range(len(lines)):
    line = lines[i]
    for column in range(len(line)-1):
        container = hashMap.get(column, BitContainer())

        if line[column] == '1':
            container.ones += 1
        elif line[column] == '0':
            container.zeros += 1

        hashMap[column] = container

gamma = ''

for i in range(len(hashMap)):
    container = hashMap[i]
    if container.ones > container.zeros:
        gamma = gamma + '1'
    else:
        gamma = gamma + '0'
    # print(f'ones: {hashMap[i].ones}, zeros: {hashMap[i].zeros}')


def inverseBits(input):
    result = input.replace('1', '2')
    result = result.replace('0', '1')
    result = result.replace('2', '0')
    return result


print(int(gamma, 2) * int(inverseBits(gamma), 2))
