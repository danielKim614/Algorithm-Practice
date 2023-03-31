'''
개미 전사
'''

# Input
n = int(input())
arr = list(map(int, input().split()))

# Define Variables
d = [0] * 100
d[0], d[1] = arr[0], arr[1]
# Algorithm
for i in range(2, n):
    if d[i-2] + arr[i] > d[i-1]:
        d[i] = d[i-2] + arr[i]
    else:
        d[i] = d[i-1]

# Output
print(d[n-1])
