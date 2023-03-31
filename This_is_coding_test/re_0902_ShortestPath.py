'''
미래 도시
'''

# Input
n, m = map(int, input().split())

# Define Variables
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

x, k = map(int, input().split())

# Algorithm
for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

distance = graph[1][k] + graph[k][x]

# Output
if distance >= INF:
    print(-1)
else:
    print(distance)