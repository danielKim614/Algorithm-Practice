import heapq

INF = int(1e9)

def solution(n, paths, gates, summits):
    
    graph = [[] for __ in range(n + 1)]
    for path in paths:
        graph[path[0]].append((path[2], path[1]))
        graph[path[1]].append((path[2], path[0]))
    
    intensity = [INF for __ in range(n + 1)]
    q = []
    
    for gate in gates:
        heapq.heappush(q, (0, gate))
        intensity[gate] = 0
    
    while q:
        time, now = heapq.heappop(q)
        
        if intensity[now] < time or now in summits:
            continue
            
        for weight, next in graph[now]:
            new_intensity = max(time, weight)
            if intensity[next] > new_intensity:
                intensity[next] = new_intensity
                heapq.heappush(q, (new_intensity, next))
    
    summit_num, min_intensity = None, INF
    summits.sort()
    
    for summit in summits:
        if intensity[summit] < min_intensity:
            summit_num = summit
            min_intensity = intensity[summit]
            
    result = [summit_num, min_intensity]
    
    return result
