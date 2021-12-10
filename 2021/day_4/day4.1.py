class Board:

    def __init__(self) -> None:
        self.rows = []


input = []
boards = dict()
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
            board.rows.append(list(map(int, line.split())))
            print(f'Board {index}, rows {board.rows}')

# for i in (1, index):
    # print(boards[i].rows)
