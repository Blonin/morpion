import math


class Plane:
    def __init__(self, length):
        self.length = length
        self.__activateCells()
        super().__init__()

    def __activateCells(self):
        self.__plane = []
        for i in range(self.length):
            col = []
            for j in range(self.length):
                col.append('-')
            self.__plane.append(col)

    def printInstance(self):
        for col in self.__plane:
            for i in col:
                print(i, end=' | ')
            print("\n" + '-' * (self.length * 4 - 1))

    def markCell(self, row, col, mode):
        if (self.length < row or self.length < col):
            raise Exception(f"{row} {col} is not inside plane")

        # checking if the point is already taken
        if (not self.cellIsEmpty(row, col)):
            raise Exception(f"{row} {col} is already taken")

        row -= 1
        col -= 1

        self.__plane[row][col] = 'X' if mode == "user" else 'O'

    def clearCell(self, row, col):
        if (self.length < row or self.length < col):
            return "Invalid Move"
        row -= 1
        col -= 1
        self.__plane[row][col] = '-'

    def cellIsEmpty(self, row, col):
        return self.__plane[row - 1][col - 1] == '-'

    def isComplete(self):
        plane = self.__plane

        # checking column wise
        for col in plane:
            if (col.count(col[0]) == len(col)) and col[0] != '-':
                return col[0] == 'X'

        # generating rows
        rows = []
        for col in plane:
            for i in range(len(col)):
                if (col is plane[0]):
                    rows.append([col[i]])
                else:
                    rows[i].append(col[i])

        # checking for rows
        for row in rows:
            if (row.count(row[0]) == len(row)) and row[0] != '-':
                return row[0] == 'X'

        # generating diagonals
        diagonals = [[], []]
        for i in range(len(plane)):
            n = len(plane) - 1
            diagonals[0].append(plane[i][n - i])
            diagonals[1].append(plane[n - i][n - i])

        # checking for diagonals
        for diagonal in diagonals:
            if (diagonal.count(diagonal[0]) == len(diagonal)) and diagonal[0] != '-':
                return diagonal[0] == 'X'

        for col in plane:
            if ('-' in col):
                return None

        return 'DRAW'


def botMove(gamePlane):
    bestScore = -math.inf
    bestMove = ()
    for i in range(1, gamePlane.length + 1):
        for j in range(1, gamePlane.length + 1):
            if gamePlane.cellIsEmpty(i, j):
                gamePlane.markCell(i, j, 'bot')
                score = minMax(gamePlane, False)
                gamePlane.clearCell(i, j)
                if (score > bestScore):
                    bestMove = (i, j)
                    bestScore = score
    return bestMove


def minMax(gamePlane, botTurn):

    win = gamePlane.isComplete()
    dead = gamePlane
    if win is not None:
        return mapState(win)

    if botTurn:
        bestScore = -math.inf
        for i in range(1, gamePlane.length + 1):
            for j in range(1, gamePlane.length + 1):
                if gamePlane.cellIsEmpty(i, j):
                    gamePlane.markCell(i, j, 'bot')
                    score = minMax(gamePlane, False)
                    gamePlane.clearCell(i, j)
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(1, gamePlane.length + 1):
            for j in range(1, gamePlane.length + 1):
                if gamePlane.cellIsEmpty(i, j):
                    gamePlane.markCell(i, j, 'user')
                    score = minMax(gamePlane, True)
                    gamePlane.clearCell(i, j)
                    bestScore = min(score, bestScore)
        return bestScore


def mapState(win):
    if win is True:
        return 10
    if win is False:
        return -10
    return 0


def checkIfWin(gamePlane):
    win = gamePlane.isComplete()
    if (win == "DRAW"):
        raise Exception('It is a draw!')
    if (win is not None):
        raise Exception('Match Ends\n' + ('You won' if (win) else 'bot won'))


level = int(input('which level do you want to play?\n'))
gamePlane = Plane(level)
while True:
    inp = input('type \'end\' to exit\nYour move: \n\'row\' \'col\'\n')
    if (inp == 'end'):
        print("you exited the game")
        break

    try:
        x, y = map(int, inp.split())
    except:
        if inp == 'end':
            break

    try:
        gamePlane.markCell(x, y, "user")
        gamePlane.printInstance()
        print()
    except Exception as e:
        print(e)
        continue

    try:
        checkIfWin(gamePlane)
    except Exception as e:
        print(e)
        break

    x, y = botMove(gamePlane)
    gamePlane.markCell(x, y, 'bot')
    gamePlane.printInstance()
    try:
        checkIfWin(gamePlane)
    except Exception as e:
        print(e)
        break
    finally:
        print()
