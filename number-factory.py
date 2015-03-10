def is_prime(number):
   return not any(number%i == 0 for i in range(9,1,-1))

def checkio(number):
    if is_prime(number): return 0
    factors = []
    while number>1:
        for i in range(9,0,-1):
            if number%i == 0:
                factors.append(i)
                number/=i
                # print number
                if is_prime(number) and number!=1:
                    return 0
                break

    factors.sort()
    factors = map(str,factors)
    # print factors
    result = int("".join((factors)))
    if result==1: result=0
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    # print is_prime(17)
