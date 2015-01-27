from collections import deque
def rotate(state, pipe_numbers):
    initial_queue = deque(state)
    size_queue = len(state) 
    res = []
    for i in range(size_queue):
        if all([initial_queue[n] for n in pipe_numbers]): res.append(i)
        initial_queue.rotate(1)
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
