def vonNeuman(grid, c, rank, val):
    d = 1 + 2*rank
    top_left = c[0]-rank, c[1]-rank
    border_points = []
    for i in range(max(0,top_left[0]), min(top_left[0]+d,len(grid))):
        for j in range(max(0,top_left[1]), min(top_left[1]+d,len(grid[0]))):
            a = (i,j)
            # check only element on Manhattan distance of current rank
            if abs(a[0]-c[0])+abs(a[1]-c[1]) == rank:
                border_points.append(grid[i][j])
    if val == 1:
        return all(border_points)
    else:
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
    return max(greates_colony, key=lambda x: x[1])[0] if greates_colony else [0,0]