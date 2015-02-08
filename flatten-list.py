def flat_list(a):
    r=[]
    def f_l(a):
        for e in a: 
            if type(e)==int:
                r.append(e)
            else:
                f_l(e)
    f_l(a)
    return r
