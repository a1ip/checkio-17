__author__ = 'taras-sereda'

from pprint import pprint
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
        print lborder_idx, rborder_idx

dimond = make_diamond()
pprint(dimond)
check_border(dimond)





