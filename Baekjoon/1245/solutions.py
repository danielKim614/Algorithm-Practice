import sys
input = sys.stdin.readline

# Input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(n)]
visited = [[False for __ in range(m)] for __ in range(n)]

# Define Variables
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
result = 0

# Define Functions
def dfs(x, y):
    global is_peak
    visited[x][y] = True
    for i in range(8):
        px = x + dx[i]
        py = y + dy[i]
        if 0 <= px < n and 0 <= py < m:
            if graph[x][y] < graph[px][py]:
                is_peak = False
            if graph[x][y] == graph[px][py] and visited[px][py] == False:
                dfs(px, py)

# Alogrithm 
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            is_peak = True
            dfs(i, j)
            if is_peak == True:
                result += 1

# Output
print(result)