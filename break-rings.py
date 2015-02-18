from collections import Counter
from itertools import chain

def find_least_connected_2(rings):
    return Counter(chain(*[i for i in rings if len(i) > 1])).most_common()[-1][0]

def find_least_connected(rings):
    return Counter([r for i in rings for r in i if len(i) > 1]).most_common()[-1][0]

def find_victim(least_connected, rings):
    return list([i for i in rings if least_connected in i and len(i) > 1][0].difference({least_connected}))[0]

def break_rings(rings):
    counter = 0
    while any([len(i)>1 for i in rings]):
        least_connected = find_least_connected(rings)
        ring_to_break = find_victim(least_connected,rings)
        for ring in rings:
            ring.discard(ring_to_break)
        counter += 1
    return counter

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"



