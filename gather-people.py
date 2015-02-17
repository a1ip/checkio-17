from heapq import *
def golf(b,t):
    return sum([b[i][i]for i in range(1,len(b))if d(b,i)<=t])
def n(b,p):
    return [(i,k)for k,i in enumerate(b[p])if k!=p and i!=0]
def d(b, i):
    v,h=set(),[(0,i)]
    while h:
        t,p=heappop(h)
        if not p:
            return t
        if p in v:
            continue
        v.add(p)
        for l,k in n(b,p):
            if k in v:
                continue
            heappush(h,(t+l,k))
    return 100