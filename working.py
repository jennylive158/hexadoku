doku_size = 4

# # example 3 x 3 doku
# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
# ]


def read_challenge_doku(filename):
    file = open(filename, "r")

    num_boards = file.readline().strip()

    for x in range(int(num_boards)):
        new_board = []
        # fill the board
        for i in range(doku_size * doku_size):
            line = file.readline()
            new_board.append(line.split())

        # solve the doku
        solve(new_board)

        # write solved soku to new text file
        # didn't implement this
        print_board(new_board)

        # go to next doku
        file.readline()

    file.close()


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, doku_size * doku_size + 1):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # check box
    box_y = pos[0] // doku_size
    box_x = pos[1] // doku_size

    for i in range(box_y * doku_size, box_y * doku_size + doku_size):
        for j in range(box_x * doku_size, box_x * doku_size + doku_size):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % doku_size == 0 and i != 0:
            print("- " * doku_size * doku_size)

        for j in range(len(bo[0])):
            if j % doku_size == 0 and j != 0:
                print(" | ", end="")
            if j == doku_size * doku_size - 1:
                print(str(bo[i][j]))
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] not in range(1, doku_size * doku_size + 1):
                return i, j
    return None


read_challenge_doku("hard.txt")
