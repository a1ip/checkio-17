VOWELS = "aeiouy"
import re
def translate(phrase):
    phrase_size =  len(phrase)
    i = 0
    res = ''
    while (i<phrase_size):
        if phrase[i] in VOWELS:
            res += phrase[i]
            i += 2
        elif phrase[i] not in VOWELS and  phrase[i] != ' ':
            res += phrase[i]
            i += 1
        elif phrase[i] == ' ':
            res += phrase[i]
        i += 1
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
