import sys


N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

dp = [1 for i in range(N)]

for i in range(N):

        dp[i] = 1

        for j in range(i):

                if array[i] > array[j]:

                        dp[i] = max(dp[j]+1, dp[i])
            
        

print(max(dp))
