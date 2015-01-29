__author__ = 'taras-sereda'


def checkio(data):
    if len(data) == 1:
        return data[0]
    else :
        return data[0] + checkio(data[1:])


def checkio_veky(d):
    r=''.join(map(lambda x:"+"*x+"-"*-x,d)).count
    return r("+")-r("-")

if __name__ == '__main__':
    print checkio([1,2,-3])
    print checkio_veky([1,2,-3])
    # nice property  sequence multiplication treats negative numbers as 0.
    print "a"*-1
    print "a"*1