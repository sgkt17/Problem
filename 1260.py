import sys


def DFS(graf, V):
    
    stack = [V]
    visit = []
    
    while(stack):
        
        temp = stack.pop()
        
        if temp not in visit:
            visit.append(temp)
            
            graf[temp].sort(reverse = True)
            stack.extend(graf[temp])
                
    for i in (visit):

        print(i, end=' ')
    print('')
    return None
    

def BFS(graf, V):
    
    queue = [V]
    visit = []

    while(queue):

        temp = queue.pop(0)
        
        if temp not in visit:
            visit.append(temp)
            
            graf[temp].sort()
            
            queue.extend(graf[temp])
            
    for i in range(len(visit)):
        print(visit[i], end=' ')
        
    return None

        

def main():
    
    N, M, V = map(int, sys.stdin.readline().split())

    graf = {}
    
    for i in range(1,N+1,1):
        
        graf[i] = []
        
    for i in range(M):

        temp, tempp = map(int, sys.stdin.readline().split())

        graf[temp].append(tempp)
        graf[tempp].append(temp)

    DFS(graf, V)
    BFS(graf, V)
    
if __name__ == "__main__":

    main()
