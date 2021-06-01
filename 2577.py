
num1 = int(input())
num2 = int(input())
num3 = int(input())

num = num1 * num2 * num3

num = str(num)

count = [0 for i in range(10)]

for i in range(len(num)):

    temp = int(num[i])

    count[temp] = count[temp] + 1

for i in count:
    
    print(i)
