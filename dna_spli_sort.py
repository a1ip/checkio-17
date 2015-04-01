__author__ = 'taras-sereda'


def golf(sequence, partition_number):
    return sequence

import re
import string
# re.findall('...',s)
#
# string.uppercase
#
s = "ACGGCATAACCCTCGA"
print (map(''.join, zip(*[iter(s)]*3)))
l = map(''.join, zip(*[iter(s)]*3))
#
# dict.fromkeys(string.ascii_uppercase)
# {i:j for i,j in enumerate(string.ascii_uppercase)}

# count number of invertions
# counter=0
# seq = 'SDA'
# len_seq = len(seq)
# for i in range(len_seq):
#  for j in range(i, len_seq):
#   if ord(seq[i]) > ord(seq[j]):
#    counter +=1

# print counter
d = []
for e in l:
    len_seq = len(e)
    counter=0
    for i in range(len_seq):
        for j in range(i, len_seq):
            if ord(e[i]) > ord(e[j]):
                counter +=1
    print (counter,e)
    d.append ((counter,e))

print d
sorted_d = sorted(d, key=lambda tup: tup[0])
print sorted_d
l = [i[1] for i in sorted_d]
print l
print (''.join(l))
import operator
# print (sorted(d.keys(), key=operator.itemgetter(0)))


def golf(s,p):
    l=map(''.join,zip(*[iter(s)]*p))
    d=[]
    for e in l:
        l_s=len(e)
        c=0
        for i in range(l_s):
            for j in range(i,l_s):
                if ord(e[i])>ord(e[j]):
                    c+=1
        d.append((c,e))
    s_d=sorted(d,key=lambda t:t[0])
    l=[i[1] for i in s_d]
    return ''.join(l)

print "golf func"
print golf(s,2)

golf=lambda s,p:''.join(v[1]for v in sorted([(sum(e[i]>e[j]for i in range(len(e))for j in range(i,len(e))),e)for e in map(''.join,zip(*[iter(s)]*p))],key=lambda t:t[0]))