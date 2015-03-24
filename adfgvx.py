__author__ = 'taras-sereda'

import string
from itertools import izip_longest
from math import ceil
MASK = ['A','D','F','G','V','X']
def encode(text, alphabet, key):
    text = text.lower()
    textl = list(text)
    textf = filter(lambda x: x in string.ascii_lowercase or x in string.digits, textl)
    # print textf
    # len(MASK)
    tab = [alphabet[i*len(MASK):i*len(MASK)+len(MASK)] for i in range(len(MASK))]

    # print "tab", tab
    message = [(MASK[j],MASK[tab[j].index(i)]) for i in textf for j in range(len(tab)) if i in tab[j]]
    message = [j for i in message for j in i]
    # print message
    # print message

    unique_letters = set(key)
    text_indexes = [key.index(i) for i in unique_letters]
    text_indexes.sort()
    cipher = [key[i] for i in text_indexes]
    # print "cipher", cipher
    amount_of_rows = int(ceil(len(message)*1.0/len(cipher)))
    ciphered = [message[i*len(cipher):i*len(cipher)+len(cipher)] for i in range(amount_of_rows)]
    # print ciphered
    ciphered = filter(lambda x: x, ciphered)
    # print "ciphered", ciphered
    ciphered2 = list(izip_longest(*ciphered))
    # print ciphered2
    mapping = {cipher[j]:ciphered2[j] for j in range(len(ciphered2))}
    sorted_cipher = sorted(cipher)
    ciphered3 = [mapping[i] for i in sorted_cipher]
    # print ciphered3
    encoded = [j for i in ciphered3 for j in i if j!=None]
    return "".join(encoded)

def decode(encoded, alphabet, key):

    unique_letters = set(key)
    text_indexes = [key.index(i) for i in unique_letters]
    text_indexes.sort()
    cipher = [key[i] for i in text_indexes]
    # max in column
    column_max = int(ceil(len(encoded)*1.0/len(cipher)))
    # print column_max
    wrong_rows = [encoded[i*len(cipher):i*len(cipher)+len(cipher)] for i in range(column_max)]
    row_lens = [len([j for j in i if j is not None]) for i in list(izip_longest(*wrong_rows))]

    # print wrong_rows
    # print row_lens
    cipher_lens_map = {cipher[i]:row_lens[i] for i in range(len(row_lens))}
    # print cipher_lens_map

    sorted_cipher = sorted(cipher)
    # print sorted_cipher
    cp_encoded = encoded[:]
    parts = {}
    for i in sorted_cipher:
        parts[i] = cp_encoded[:cipher_lens_map[i]]
        cp_encoded = cp_encoded[cipher_lens_map[i]:]
    # print parts

    # for i in
    sorted_parts = [parts[i] for i in cipher]
    # print sorted_parts
    near_finish = list(izip_longest(*sorted_parts))
    flattened  = [j for i in near_finish for j in i if j is not None]
    # print flattened
    pairs = zip(flattened[::2],flattened[1::2])

    tab = [alphabet[i*len(MASK):i*len(MASK)+len(MASK)] for i in range(len(MASK))]

    return  "".join([tab[MASK.index(i)][MASK.index(j)] for i,j in pairs])






if __name__ == "__main__":

    # encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher')
    assert encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'FXGAFVXXAXDDDXGA'
    assert decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'iamgoing'
    #
    #
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am","na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX","na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"

    print encode("One 1, Two 2, Three 3, Four 4, Five 5, Six 6, Seven 7, Eight 8, Nine 9, Zero 0", "d9sr4qxvaz75yu2hkwpm8j63b1legot0ifnc", "monty")

    # assert  list('VXXVVGVDXAFXVXDGXAFGAGVGVGGXXGVXFDAGXGXFDDVGDXAFXFDAGVAFVGDDVGXVDVVGXFVVFGXAGFXVXFXVVGADDGVGAGVXXD')  == ['V', 'X', 'X', 'V', 'V', 'G', 'V', 'D', 'X', 'A', 'F', 'X', 'V', 'X', 'F', 'F', 'X', 'A', 'F', 'G', 'A', 'G', 'V', 'G', 'V', 'G', 'G', 'X', 'X', 'G', 'V', 'X', 'F', 'D', 'A', 'G', 'A', 'V', 'X', 'G', 'X', 'F', 'D', 'D', 'V', 'G', 'D', 'X', 'A', 'F', 'X', 'F', 'D', 'A', 'G', 'V', 'A', 'F', 'V', 'G', 'D', 'D', 'V', 'G', 'X', 'V', 'D', 'V', 'V', 'G', 'X', 'F', 'V', 'V', 'F', 'G', 'X', 'A', 'G', 'F', 'X', 'V', 'X', 'F', 'X', 'V', 'V', 'G', 'A', 'D', 'D', 'G', 'V', 'G', 'A', 'G', 'V', 'X', 'X', 'D']
    # print list('VXXVVGVDXAFXVXFFXAFGAGVGVGGXXGVXFDAGXGXFDDVGDXAFXFDAGVAFVGDDVGXVDVVGXFVVFGXAGFXVXFXVVGADDGVGAGVXXD')
