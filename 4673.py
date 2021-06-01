def init(n, arr):

    sumn = n
    
    if arr[sumn] == 1:
    
            return arr
    
    arr[sumn] = 1
    n = str(n)
    sumn = int(n)

    if sumn >= 10001:
            
            return arr
        
    else:
            for i in range(len(n)):

                    sumn += int(n[i]) 

            init(sumn,arr)


arr = [0]*10100

for i in range(1,10000):

        if arr[i] == 0:
                
                print(i)
                init(i, arr)
                
        else:
                continue
