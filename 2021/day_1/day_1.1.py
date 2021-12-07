lines = []

with open('input.txt', 'r') as file:
  lines = file.readlines()

previousLine = None
increaseCount = 0

for curline in lines:
  line = int(curline) ## for some reason this changes the result from 1373 to 1374
  if previousLine == None:
    previousLine = line

  if previousLine < line:
    print(f'{previousLine} < {line} ++')
    increaseCount += 1
  elif previousLine > line:
    print(f'{previousLine} > {line} 0')

  previousLine = line
  print(increaseCount)

print(f'Count: {increaseCount}')