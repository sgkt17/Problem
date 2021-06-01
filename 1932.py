import sys

num = int(sys.stdin.readline())

array = []

for _ in range(num):
    
    temp = list(map(int, sys.stdin.readline().split()))
    array.append(temp)


dp = [[0]*(i+1) for i in range (num)]


for i in range(num):

    for j in range(0, i+1, 1):

        if i == 0 and j == 0:

            dp[i][j] = array[0][0]

            continue

        if j==0:

            dp[i][j] = array[i][j] + dp[i-1][j]

        elif j==i:

            dp[i][j] = array[i][j] + dp[i-1][j-1]

        else:

            dp[i][j] = array[i][j] + max(dp[i-1][j], dp[i-1][j-1])
