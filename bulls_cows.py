__author__ = 'taras-sereda'


from string import digits
import random


hiden_number = random.sample(digits,4)
guess = list(raw_input("Your guess:"))
guesses = 0
# print hiden_number
while hiden_number!=guess:
    buls = sum(a==b for a,b in  zip(hiden_number,guess))
    # print "hiden",hiden_number
    rest = [(a,b) for a,b in  zip(hiden_number,guess) if a!=b]
    hiden_part, guess_part = zip(*rest)
    cows = 0
    for i in guess_part:
        for j in hiden_part:
            if i==j:
                cows+=1
    print "b{0}c{1}".format(buls,cows)
    guess = list(raw_input("Your guess:"))
    guesses+=1

hiden_number = "".join(hiden_number)
print "hidden number {0}".format(hiden_number)
print "You win!!! in {0} guesses".format(guesses)
    # print "cows", cows
