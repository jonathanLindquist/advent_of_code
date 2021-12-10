class Board:

    def __init__(self) -> None:
        self.rows = []


class Square:

    def __init__(self, number, marked) -> None:
        self.number = number
        self.marked = marked


def prettyPrint(boards, printNumbers):
    for index in range(1, len(boards) + 1):
        board = boards[index]
        print(f"Board {index}")
        for row in board.rows:
            if printNumbers:
                print(
                    f'{row[0].number} {row[1].number} {row[2].number} {row[3].number} {row[4].number}')
            else:
                print(
                    f'{row[0].marked} {row[1].marked} {row[2].marked} {row[3].marked} {row[4].marked}')
        print()


def initBoards(boards):
    index = 0
    with open('input.txt', 'r') as file:
        input = list(map(int, file.readline().split(',')))
        print(input)

        for line in file.readlines():
            if not line.strip():
                index += 1
                boards[index] = Board()
            else:
                board = boards[index]
                rowRaw = list(map(int, line.split()))
                row = list(map(
                    lambda x: Square(x, False),
                    rowRaw
                ))
                board.rows.append(row)

        return input


def markBoards(input, boards):
    winningBoard = None
    for index in range(len(input)):
        number = input[index]
        print(f'Number: {number}')

        finalBoard = False
        if len(boards) <= 1:
            finalBoard = True

        for key, val in dict(boards).items():
            winner = markBoard(boards[key], number)
            if winner:
                if finalBoard:
                    winningBoard = boards[key]
                    break
                del boards[key]
        if winningBoard:
            break

    return winningBoard


def markBoard(board, number):
    winner = False
    for rowI in range(len(board.rows)):
        for i in range(len(board.rows[rowI])):
            square = board.rows[rowI][i]
            if square.marked == False and square.number == number:
                square.marked = True
                winner = isWinner(board, rowI, i)
                if winner:
                    break
        if winner == True:
            break
    return winner


def isWinner(board, row, col):
    winnerRow = True
    winnerColumn = True

    rowDown = row
    rowUp = row
    colLeft = col
    colRight = col

    while rowDown >= 0 and winnerRow == True:
        square = board.rows[rowDown][col]
        if square.marked == False:
            winnerRow = False
        rowDown -= 1

    while rowUp < len(board.rows) and winnerRow == True:
        square = board.rows[rowUp][col]
        if square.marked == False:
            winnerRow = False
        rowUp += 1

    while colLeft >= 0 and winnerColumn == True:
        square = board.rows[row][colLeft]
        if square.marked == False:
            winnerColumn = False
        colLeft -= 1

    while colRight < len(board.rows[0]) and winnerColumn == True:
        square = board.rows[row][colRight]
        if square.marked == False:
            winnerColumn = False
        colRight += 1

    return winnerRow or winnerColumn


def sumUnmarkedNumbers(board):
    total = 0
    for row in board.rows:
        for square in row:
            if square.marked == False:
                total += square.number
    return total


input = []
boards = dict()

input = initBoards(boards)

prettyPrint(boards, True)

winner = markBoards(input, boards)

sum = sumUnmarkedNumbers(winner)

print(sum)
