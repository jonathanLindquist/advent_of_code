input = []

with open('input.txt', 'r') as file:
    input = file.readlines()
    for index in range(len(input)):
        input[index] = input[index].strip().split(' -> ')
        print(input[index])


# def initMap(input):
#     highestValues = [0, 0]

#     for item in input:
#         highestValues = setHighestValues(item[0].split(','), highestValues)
#         highestValues = setHighestValues(item[1].split(','), highestValues)

#     for i in range(highestValues[0]):


# def setHighestValues(pair, highestValues):
#     x = int(pair[0])
#     y = int(pair[1])

#     if x > highestValues[0]:
#         highestValues[0] = x

#     if y > highestValues[1]:
#         highestValues[1] = y

#     return highestValues


def buildMap(input):
    map = dict()
    overlappingLines = 0

    for item in input:
        firstPair = item[0].split(',')
        secondPair = item[1].split(',')

        startX = getStartingPoint(firstPair[0], secondPair[0])
        distanceX = abs(int(firstPair[0]) - int(secondPair[0])) + 1
        startY = getStartingPoint(firstPair[1], secondPair[1])
        distanceY = abs(int(firstPair[1]) - int(secondPair[1])) + 1

        # do not map line if diagonal
        if distanceY > 1 and distanceX > 1:
            continue

        for xIndex in range(startX, startX + distanceX):
            for yIndex in range(startY, startY + distanceY):
                yMap = map.get(xIndex, dict())
                val = yMap.get(yIndex, 0)

                yMap[yIndex] = val + 1
                map[xIndex] = yMap
                # print(f'X val: {xIndex} Y val: {yIndex}')
                if val == 1:
                    overlappingLines += 1

    print(f' prettyPrint result + {prettyPrint(map)}')

    return overlappingLines


def getStartingPoint(p1, p2):
    if p1 <= p2:
        return int(p1)
    else:
        return int(p2)


def prettyPrint(map):
    keys = sorted(map.keys())
    result = 0

    for xKey in keys:
        yMap = map.get(xKey)
        yKeys = sorted(yMap.keys())

        for yKey in yKeys:
            item = yMap.get(yKey)

            if item > 1:
                result += 1

    return result

# def prettyPrintMap(map):
#     for vector in map:
#         for i in range(len(vector)):
#             print(f'{vector[i]}', end=' ')


# map = initMap(input)

overlappingLines = buildMap(input)
print(f'Overlapping lines: {overlappingLines}')
