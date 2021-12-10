class Line:
  movement = None
  amount = None

  def __init__(self, movement, amount):
      self.movement = movement
      self.amount = amount

distance = 0
depth = 0
aim = 0

def determineMovement(line):
  global distance
  global depth
  global aim
  
  if line.movement == 'forward':
    distance = distance + line.amount
    depth = depth + (aim * line.amount)
  elif line.movement == 'up':
    aim = aim - line.amount
  elif line.movement == 'down':
    aim = aim + line.amount

  print(f'distance: {distance}')
  print(f'depth: {depth}')

lines = []

with open('input.txt', 'r') as file:
  lines = file.readlines()

for i in range(len(lines)):
  lineList = lines[i].split(' ')
  line = Line(lineList[0], int(lineList[1]))

  determineMovement(line)
  # print(f'Movement = {line.movement}, Amount = {line.amount}')




print(distance * depth)