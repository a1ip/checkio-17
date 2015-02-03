def get_neighbours(maze,positions):
    seq_2 = { 
        (-1,0) : 'N',
        (0,-1) : 'W',
        (0,1) : 'E',
        (1,0) :'S'
    }
    res = [((positions[0]+i[0],positions[1]+i[1]),seq_2[i]) for i in seq_2 if not maze[positions[0]+i[0]][positions[1]+i[1]] ]
    return res
    
def checkio(maze_map):
    visited, queue = set(), [((1,1), "")]
    while queue:
        position, path = queue.pop(0)
        if position == (10,10):
            return path
        if position in visited:
            continue
        visited.add(position)
        #print visited
        #print get_neighbours(maze_map, position)
        for neigh_position, direction in get_neighbours(maze_map, position):
            #print neigh_position
            if neigh_position in visited:
                continue
            queue.append((neigh_position, path + direction))
    return path