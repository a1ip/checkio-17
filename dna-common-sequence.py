''' http://en.wikipedia.org/wiki/Longest_common_subsequence_problem?oldformat=true '''
def lcs_len(xs,ys):
    # +1 is neccessary due to be in mat bound
    m=len(ys)+1
    n=len(xs)+1
    mat = [[0 for j in range(m)] for i in range(n)]

    for i in range(len(xs)):
        for j in range(len(ys)):
            if xs[i] == ys[j]:
                mat[i+1][j+1] = mat[i][j] + 1
            else:
                mat[i+1][j+1] = max(mat[i+1][j], mat[i][j+1])
    return mat

def backtrackAll(mat, xs, ys):
    if not xs or not ys:
        return set([""])
    elif xs[-1] == ys[-1]:
        return set([z + xs[-1] for z in backtrackAll(mat, xs[:-1], ys[:-1])])
    else:
        R = set()
        i = len(xs)
        j = len(ys)
        if mat[i][j-1] >= mat[i-1][j]:
            R.update(backtrackAll(mat, xs, ys[:-1]))
        if mat[i-1][j] >= mat[i][j-1]:
            R.update(backtrackAll(mat, xs[:-1], ys))
    return R

def common(s1,s2):
    mat = lcs_len(s1, s2)
    return ",".join(sorted(backtrackAll(mat, s1, s2)))
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
