def find_repetitions(lst):
    etalon = lst[0]
    amount = 1
    for i in range(1,len(lst)):
        if lst[i] == etalon:
            amount += 1
        else:
            etalon = lst[i]
            amount = 1
        if amount == 4 : return True
    return False

def get_rows(grid):
    return [[cell for cell in row] for row in grid]

def get_cols(grid):
    cols = [[] for col in grid[0]]
    for row in grid:
        for col_index, cell in enumerate(row):
            cols[col_index].append(cell)
    return cols

def get_forward_diagonals(grid):
    buff = ['X']*(len(grid[0])+1)
    buff_grid = []
    for row_index, row in enumerate(get_rows(grid)):
        buff_grid.append( buff[row_index:] + row + buff[:row_index+1] )
    cols = get_cols(buff_grid)[2:-1]
    for col in cols:
        while 'X' in col:
            col.remove('X')
    return cols

def get_backward_diagonals(grid):
    buff = ['X']*(len(grid[0])+1)
    buff_grid = []
    for row_index, row in enumerate(get_rows(grid)):
        buff_grid.append( buff[:row_index+1] + row + buff[row_index:] )
    cols = get_cols(buff_grid)[1:-2]
    for col in cols:
        while 'X' in col:
            col.remove('X')
    return cols

def checkio(matrix):
    forward =filter(lambda x: len(x)>=4 ,get_forward_diagonals(matrix))
    backward = filter(lambda x: len(x)>=4 ,get_backward_diagonals(matrix))
    cols = filter(lambda x: len(x)>=4 ,get_cols(matrix))
    rows = filter(lambda x: len(x)>=4 ,get_rows(matrix))

    return True if not (
    not any(find_repetitions(line) for line in cols) and not any(find_repetitions(line) for line in rows) and not any(
        find_repetitions(line) for line in forward) and not any(find_repetitions(line) for line in backward)) else False

if __name__ == '__main__':

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"