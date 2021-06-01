import sys


def BFS(N,M,array,count,queue,tomato):

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    if tomato == N*M:
        return 0

    while 1:

        new_queue = []

        while len(queue):
            
            temp = queue.pop()

            for i in range(4):

                curx = temp[0]+dx[i]
                cury = temp[1]+dy[i]

                if curx < M and curx > -1 and cury > -1 and cury < N and array[curx][cury] == 0:
                    
                    array[curx][cury] = 1
                    new_queue.append((curx,cury))
                    tomato += 1
                    
        queue = new_queue
        
        if len(queue) == 0:
            break
        count += 1


    if tomato < N*M:

        return -1
        
    else: 
        return count
        

N, M = map(int, sys.stdin.readline().split())

array = []
count = 0
queue = []
tomato = 0

for i in range(M):

    temp = list(map(int,sys.stdin.readline().split()))

    array.append(temp)

    for j in range(N):

        if array[i][j] == 1:
            queue.append((i,j))
            tomato += 1 

        elif array[i][j] == -1:
            tomato += 1
            
print(BFS(N,M,array,count,queue,tomato))
