from heapq import *


def golf(building, time):
    return sum([building[i][i] for i in range(1, len(building)) if dfs(building, i, time) <= time])


def get_neighbours(building, position):
    return [(i, k) for k, i in enumerate(building[position]) if k != position and i != 0]


def dfs(building, i, time):
    visited, h = set(), [(0,i)]
    while h:
        length, position = heappop(h)
        # print length, position
        if position == 0:
            return length
        if position in visited:
            continue
        visited.add(position)
        for l,neigh_position in get_neighbours(building, position):
            if neigh_position in visited:
                continue
            heappush(h, (length + l,neigh_position))
            # print h
    return 1000000


building = [[0, 0, 36, 0, 64, 60, 0, 20, 22],
            [0, 7, 41, 30, 30, 64, 0, 40, 0],
            [36, 41, 6, 0, 0, 0, 0, 0, 50],
            [0, 30, 0, 2, 0, 0, 0, 0, 0],
            [64, 30, 0, 0, 5, 50, 0, 0, 0],
            [60, 64, 0, 0, 50, 9, 72, 41, 0],
            [0, 0, 0, 0, 0, 72, 1, 31, 0],
            [20, 40, 0, 0, 0, 41, 31, 9, 0],
            [22, 0, 50, 0, 0, 0, 0, 0, 7]]

print golf([[0,0,36,0,64,60,0,20,22],
[0,7,41,30,30,64,0,40,0],
      [36,41,6,0,0,0,0,0,50],
      [0,30,0,2,0,0,0,0,0],
      [64,30,0,0,5,50,0,0,0],
      [60,64,0,0,50,9,72,41,0],
      [0,0,0,0,0,72,1,31,0],
      [20,40,0,0,0,41,31,9,0],
      [22,0,50,0,0,0,0,0,7]], 58)

# print dfs(building, 6, 58)