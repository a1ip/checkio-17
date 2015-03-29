import math
def simple_areas(*args):
    if len(args) == 1:
        res = math.pi*(args[0]*1.0/2)**2
    elif len(args) == 2:
        res = args[0]*args[1]
    elif len(args) == 3:
        p2 = sum(args)*1.0/2
        res = math.sqrt(p2*(p2-args[0])*(p2 - args[1])*(p2 -args[2])) 
    return round(res,2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
