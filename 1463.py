a = int(input())

dp = [0 for i in range(a +1)]

for i in range(a+1):

    if i in [0,1]:
        
        continue

    else:

        i3 = int(i/3)
        i2 = int(i/2)
        i1 = int(i-1)
        
        if i%3 == 0:

            if i %2 == 0:
                
                dp[i] = min(dp[i3], dp[i2],dp[i1])+1

            else:

                dp[i] = min(dp[i3],dp[i1]) +1

        else:
            
            if i % 2 == 0:
             
                dp[i] = min(dp[i1],dp[i2]) +1

            else:

                dp[i] = dp[i1] +1

print(dp[a])
