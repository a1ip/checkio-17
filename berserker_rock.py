from collections import deque


def nearest_rocks(current, neighbours):
    nearest_neighbours = []
    vertical_neighbours = filter(lambda x: x[1] == current[1], neighbours) + [current]
    vertical_neighbours.sort(key=lambda x: x[0])
    current_pos = vertical_neighbours.index(current)
    left_pos_vertical = current_pos - 1
    right_pos_vertical = current_pos + 1
    if left_pos_vertical >= 0:
        nearest_neighbours.append(vertical_neighbours[left_pos_vertical])
    if right_pos_vertical <= len(vertical_neighbours) - 1:
        nearest_neighbours.append(vertical_neighbours[right_pos_vertical])
    horisontal_neighbours = filter(lambda x: x[0] == current[0], neighbours) + [current]
    horisontal_neighbours.sort(key=lambda x: x[1])
    current_pos = horisontal_neighbours.index(current)
    left_pos_horisontal = current_pos - 1
    right_pos_horisontal = current_pos + 1
    if left_pos_horisontal >= 0:
        nearest_neighbours.append(horisontal_neighbours[left_pos_horisontal])
    if right_pos_horisontal <= len(horisontal_neighbours) - 1:
        nearest_neighbours.append(horisontal_neighbours[right_pos_horisontal])
    return nearest_neighbours


def berserk_rook(berserker, enemies):
    queue = deque()
    queue.append((berserker, [berserker]))
    longest_path = 0
    while queue:
        current, path = queue.popleft()
        neighbours = [i for i in enemies if (i[0]==current[0] or i[1]==current[1]) and i not in path]
        nearest_neighbours = nearest_rocks(current, neighbours)
        if nearest_neighbours:
            for i in nearest_neighbours:
                queue.append((i,path+[i]))
        else:
            if len(path)>longest_path:
                longest_path = len(path)-1
    return longest_path

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook(u'd3', {u'd6', u'b6', u'c8', u'g4', u'b8', u'g6'}) == 5, "one path"
    assert berserk_rook(u'a2', {u'f6', u'f2', u'a6', u'f8', u'h8', u'h6'}) == 6, "several paths"
    assert berserk_rook(u'a2', {u'f6', u'f8', u'f2', u'a6', u'h6'}) == 4, "Don't jump through"

