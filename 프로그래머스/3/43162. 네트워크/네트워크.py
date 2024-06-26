from collections import deque
def bfs(node,graph,visited):
    q=deque()
    q.append(node)
    visited[node]=True
    
    while q:
        v=q.popleft()
        
        for k in graph[v]:
            if visited[k]:
                continue
            visited[k]=True
            q.append(k)
        
    
    
def solution(N, A):
    ans = 0
    graph=[[] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            if A[i][j]==1:
                graph[i].append(j)
                
    
    visited=[False]*N
    for i in range(N):
        if visited[i]:
            continue
        if not graph[i]:
            ans+=1
            visited[i]=True
        else:
            bfs(i,graph,visited)
            ans+=1
                
    
    return ans
