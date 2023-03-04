# Input
t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))

# Define Variables
maximum = max(arr)
d = [[0, 0] for i in range(maximum + 2)]
d[0] = [1, 0]
d[1] = [0, 1]

# Define Functions
def fibonacci(n):
    global d
    for i in range(2, n + 1):
        d[i][0] = d[i - 1][0] + d[i - 2][0]
        d[i][1] = d[i - 1][1] + d[i - 2][1]
# Algorithm
fibonacci(maximum)
for case in arr:
    print("{} {}".format(d[case][0], d[case][1]) ,end='\n')