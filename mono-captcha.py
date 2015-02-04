FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")

from pprint import pprint 

def divide_font(FONT):
    numbers = [FONT[num:num+40] for num in range(0,len(FONT), 41)]
    #pprint (numbers)
    num_arr = []
    for i in range(0,len(numbers[0]),4):
        a = [j[i:i+4] for j in numbers]
        a = [j for i in a for j in i]
        a = map(lambda x : 0 if x == '-' else 1, a)
        num_arr.append(a)
        #pprint(a)
        #print '\n'
    #pprint(num_arr)
    #print len(num_arr)
    last = num_arr.pop()
    num_arr.insert(0, last)
    #num_arr[-1] + num_arr[:-1] 
    pprint (num_arr)
    return num_arr

def checkio(image):
    num_img = ''
    numbers = divide_font(FONT)
    for i in range(0,len(image[0])-1,4):
        num = [j[i:i+4] for j in image]
        num = [j for i in num for j in i]
        #print num    
        #print '\n'
        for j,i in enumerate(numbers):
            #sum(k[0]!=k[1] for k in zip(num,i))
            if sum(k[0]!=k[1] for k in zip(num,i)) < 2 :
                #print sum(k[0]!=k[1] for k in zip(num,i))
                #print zip(num,i)        
                #print 'bingo'
                #print j+1
                num_img += str(j)
        #print num_img
    return int(num_img)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
