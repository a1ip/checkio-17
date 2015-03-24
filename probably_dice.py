__author__ = 'taras-sereda'

from itertools import product

def probability(dices, sides, target):

    side_values = [i for i in range(1,sides+1)]
    values = filter(lambda x: sum(x)==target, product(side_values, repeat=dices))
    # print side_values
    # for i in product(side_values, repeat=dices):
        # print i
    prob = len(values)*1.0/sides**dices
    return round(prob,4)
if __name__ == "__main__":
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"