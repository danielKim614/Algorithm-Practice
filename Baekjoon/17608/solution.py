import sys

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]
highest = 0
count = 0

for _ in range(n):
    tmp = arr.pop()
    if tmp > highest:
        count += 1
        highest = tmp

print(count)