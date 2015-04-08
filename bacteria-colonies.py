from pprint import pprint
import pprint
MIN = ((0,1,0),
       (1,1,1),
       (0,1,0),)
pp = pprint.PrettyPrinter(width=33)

def sliding_window(grid):
    for i in range(len(grid)-len(MIN)+1):
        for j in range(len(grid[0])-len(MIN)+1):
            tile = tuple(tuple(grid[i+k][j+f] for f in range(3)) for k in range(3))
            # pp.pprint(tile)
            if tile == MIN:
                # pp.pprint(make_diamond(len(MIN)+2))
                center = [i+1, j+1]
                # print center
                return center if check_peaks(center, len(MIN), grid) else [0,0]

def vonNeuman(grid,c,rank, val):
    # print "call of vanNeuman"
    # print "center", c
    d = 1 + 2*rank
    top_left = c[0]-rank, c[1]-rank
    grid_slice = grid[top_left[0]:top_left[0]+d][top_left[1]:top_left[1]+d]
    border_points = []
    for i in range(max(0,top_left[0]), min(top_left[0]+d,len(grid))):
        for j in range(max(0,top_left[1]), min(top_left[1]+d,len(grid[0]))):
            # print i,j
            a = (i,j)
            if abs(a[0]-c[0])+abs(a[1]-c[1]) == rank:
                # print 'adding', i,j
                border_points.append(grid[i][j])
    # pp.pprint(grid_slice)
    if val == 1:
        return all(border_points)
    else:
        # print "zero" ,border_points
        return all(k == 0 for k in border_points)


def healthy(grid):
    greates_colony = []
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            # find center of colony
            if grid[i][j] == 1:
                center = [i,j]
                rank = 0
                vonNeuman_colony = True
                while vonNeuman_colony:
                    rank+=1
                    vonNeuman_colony = vonNeuman(grid, center, rank, 1)
                else:
                    if vonNeuman(grid,center,rank, 0):
                        greates_colony.append((center,rank-1))

                # print center
    # print greates_colony
    if greates_colony:
        # print greates_colony

        max_size = max(greates_colony, key=lambda x: x[1])[1]

        result = [colony[0] for colony in greates_colony if colony[1]==max_size]
        return result[0]
    return [0,0]

                # print 'Yuhhu!'
def check_peaks(center, col_size, grid):
    rows = len(grid)-1
    cols = len(grid[0])-1
    S = center[0]+(col_size/2+1), center[1]
    W = center[0], center[1]-(col_size/2+1)
    N = center[0]-(col_size/2+1), center[1]
    E = center[0], center[1]+(col_size/2+1)
    # print S,W,N,E
    sides = filter(lambda x: 0 <= x[0] <= rows and 0 <= x[1] <= cols, [S, W, N, E])
    # print sides
    return all(not grid[s[0]][s[1]] for s in sides)




def make_diamond(l=9):
    t = 1
    d = []
    while t <= l:
        w = (l - t) / 2
        d.append('0' * w + '1' * t + '0' * w)
        t += 2
    t -= 4
    while t >= 1:
        w = (l - t) / 2
        d.append('0' * w + '1' * t + '0' * w)
        t -= 2
    return d

def check_border(dimond):
    dlen = len(dimond)
    for line in dimond:
        lborder_idx = line.index('1')-1
        rborder_idx = dlen-line[::-1].index('1')
        # print lborder_idx, rborder_idx

dimond = make_diamond()
# pp.pprint(dimond)
check_border(dimond)


if __name__ == '__main__':


    healthy(((0,1,0),
                     (0,1,1),
                     (1,1,1),
                     (0,1,0)))

    healthy(((0, 0, 1, 0, 0),
                     (0, 1, 1, 1, 0),
                     (0, 0, 1, 0, 0),
                     (0, 0, 0, 0, 0),
                     (0, 0, 1, 0, 0),))
    healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check(result, answers):
        return list(result) in answers

    check(healthy(((0, 1, 0),
                   (1, 1, 1),
                   (0, 1, 0),)), [[1, 1]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0),
                   (0, 0, 1, 0, 0),)), [[1, 2]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),)), [[0, 0]])
    check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])
