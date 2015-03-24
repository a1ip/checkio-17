from collections import deque
from heapq import *
ofsets = [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]

def min_distance(current,target):
    current0 = ord(current[0])-96
    target0 = ord(target[0])-96
    return abs(current0 - target0) + abs(int(current[1])-int(target[1]))
def possible_moves(pos):
    p1,p2 = pos
    p2 = int(p2)
    p1 = ord(p1) - 96

    moves = [(p1-i,p2-j) for i,j in ofsets]
    legal_moves = filter(lambda x: 0<x[0]<=8 and 0<x[1]<=8, moves)
    board_moves = [chr(i+96)+str(j) for i,j in legal_moves]

    return board_moves
    
    
def checkio(cells):
    current, target = cells.split('-')
    queue = deque()
    queue.append((current,[current]))
    result = 999
    while queue:
        current, path = queue.popleft()
        # print path
        moves = possible_moves(current)
        for i in moves:
            if i not in path:
                queue.append((i,path+[i]))
            if i == target:
                if len(path) < result:
                    return len(path)

def checkio(cells):
    current, target = cells.split('-')
    queue = []
    heappush(queue,(1,current,[current]))
    result = 999
    while queue:
        l,current, path = heappop(queue)
        # print path
        moves = possible_moves(current)
        for i in moves:
            if i not in path:
                heappush(queue,(l+1,i,path+[i]))
            if i == target:
                return len(path)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"b1-d5") == 2, "1st example"
    assert checkio(u"a6-b8") == 1, "2nd example"
    assert checkio(u"h1-g2") == 4, "3rd example"
    assert checkio(u"h8-d7") == 3, "4th example"
    assert checkio(u"a1-h8") == 6, "5th example"
