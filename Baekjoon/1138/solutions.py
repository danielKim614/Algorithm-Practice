import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

output = [0 for _ in range(n)]

for i in range(n):
    count = 0
    for j in range(n):
        if count == arr[i] and output[j] == 0:
            output[count] = i + 1
            break
        elif output[j] == 0:
            count += 1 
            

print(*output)
