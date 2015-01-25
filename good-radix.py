import string
radixes = string.digits  + string.ascii_uppercase

def checkio(number):
    num_lst = sorted(number)
    least_radix = radixes.index(num_lst[-1])
    while least_radix<=len(radixes):
        try:
            res = int(number, least_radix+1)
        except:
            return 0
        if not res%least_radix:
            return least_radix+1
        least_radix +=1



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    print('Local tests done')
