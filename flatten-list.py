def flat_list(a):
    r=[]
    def l(a):
        for e in a: 
            r.append(e) if type(e)==int else l(e)   
    l(a)
    return r