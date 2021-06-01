import sys


def check(Number):

    if Number%2 == 0:

        Number = Number/2
        
    else:

        Number = (Number + 1)/2


    return Number
        

N, Kim, Han = map(int, sys.stdin.readline().split())

count = 0


while 1:

    count += 1
    
    if Han - Kim == 1 and Han%2 == 0:

        break
    
    elif Kim - Han == 1 and Kim%2 == 0:

        break
    
    else:
       
        N = check(N)
        Kim = check(Kim)
        Han = check(Han)

print(count)
