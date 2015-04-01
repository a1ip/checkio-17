def golf(s,p):
    l=map(''.join,zip(*[iter(s)]*p))
    d=[]
    for e in l:
        l_s=len(e)
        c=0
        for i in range(l_s):
            for j in range(i,l_s):
                if ord(e[i])>ord(e[j]):
                    c+=1
        d.append((c,e))
    s_d=sorted(d,key=lambda t:t[0])
    l=[i[1] for i in s_d]
    return ''.join(l)