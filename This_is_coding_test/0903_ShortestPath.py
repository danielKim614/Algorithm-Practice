'''
전보
'''
import heapq
import sys

input = sys.stdin.readline

# Input
n, m, c = map(int, input().split())
graph = [[] for __ in range(n + 1)]
for __ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# Define Variables
INF = int(1e9)
distance = [INF] * (n + 1)
count = 0
max_distance = 0

# Define Functions
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# Algorithm
dijkstra(c)
for i in range(1, n + 1):
    if distance[i] != INF and i != c:
        count += 1
        max_distance = max(max_distance, distance[i])

# Output
print(count, end=' ')
print(max_distance)