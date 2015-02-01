

def count_neighbours(grid, row, col):
    size_row = len(grid)
    size_col = len(grid[0])
    seq = [(i,j) for i in range(-1,2) for j in range(-1,2) if i!=0 or j!=0]
    res = sum(grid[row+i[0]][col+i[1]] for i in seq if 0 <= row+i[0] < size_row and 0 <= col+i[1] < size_col)
    return res



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"


    grid = ((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 8),)
    # last elemnt of the matrix
    # 8
    print grid[-1][-1]
