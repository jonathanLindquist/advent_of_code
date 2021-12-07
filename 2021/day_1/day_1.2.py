lines = []

with open('input.txt', 'r') as file:
  lines = file.readlines()

for i in range(len(lines)):
  lines[i] = int(lines[i])

start = 1
end = len(lines) - 1
increaseCount = 0
previousWindow = None

for i in range(start, end):

  window = lines[i-1] + lines[i] + lines[i+1]

  if previousWindow == None:
    previousWindow = window
    continue

  if previousWindow < window:
    print(f'window: {lines[i-1]} + {lines[i]} + {lines[i+1]} \n ++')
    increaseCount += 1
  # elif previousLine > line:
  #   print(f'{previousLine} > {line} 0')

  previousWindow = window
  print(increaseCount)

print(f'Count: {increaseCount}')