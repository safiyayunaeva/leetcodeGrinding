def initDP(row, col):
    dp = []
    for i in range(row):
        r = []
        for j in range(col):
            r.append(-1)
        dp.append(r)
    return dp


def traverseMatrix(grid):
    row = len(grid)
    col = len(grid[0])
    dp = initDP(row, col)
    print(dp)
    for i in range(row):
        for j in range(col):
            if grid[i][j] != -1:
                print(grid[i][j])


def matrixProblems():
    grid = [[0, 1], [-1, 0]]
    grid1 = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    grid2 = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
