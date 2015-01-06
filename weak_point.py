__author__ = 'taras-sereda'

def weak_point(matrix):
    cols = map(sum,zip(*matrix))
    rows = map(sum,matrix)
    week_col = cols.index(min(cols))
    week_row = rows.index(min(rows))
    return week_row,week_col

import numpy as np

def weak_point_numpy(matrix):
    durability_matrix = np.matrix(matrix)
    sum_cols = durability_matrix.sum(axis=0).tolist()[0]
    sum_rows = np.reshape(durability_matrix.sum(axis=1), (1,-1)).tolist()[0]
    week_row = sum_rows.index(min(sum_rows))
    week_col = sum_cols.index(min(sum_cols))
    return [week_row,week_col]

# for learning purpose
# @Sim0000 on checkio
# def weak_point(matrix):
#     n = len(matrix)
#     row = min(range(n), key=lambda r:sum(matrix[r][c] for c in range(n)))
#     col = min(range(n), key=lambda c:sum(matrix[r][c] for r in range(n)))
#     return row, col
if __name__ == '__main__':



    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
