import sys


n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

dp = [0 for i in range(n)]

for i in range(n):

        if i == 0:
                
                dp[i] = arr[i]

                continue

        dp[i] = max(arr[i], dp[i-1]+arr[i])

print(max(dp))
