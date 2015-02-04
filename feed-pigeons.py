
def checkio(food):
    minute = 0
    fed_pigeons = 0
    pigeons = 0
    while True:
        minute += 1
        old_pigeons = pigeons
        pigeons += minute   
        if food < pigeons:
            # to feed sombody from newly arrived pegions
            # if remains_food < 0, means that only 3 distinct pigeons fed
            # remains_food hold amount of newly arrived pegions which we able to feed
            remains_food = food - old_pigeons
            if remains_food > 0:
                fed_pigeons += remains_food
            break
        else:
            food -= pigeons
            fed_pigeons += minute
    return fed_pigeons

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"