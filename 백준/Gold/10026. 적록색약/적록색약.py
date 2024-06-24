import sys
from collections import deque

N=int(sys.stdin.readline())
graph=[list(sys.stdin.readline().rstrip()) for _ in range(N)]

def bfs(opt,x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    dx,dy=[0,0,-1,1],[1,-1,0,0]
    
    while q:
        vx,vy=q.popleft()

        for k in range(4):
            nx,ny=vx+dx[k],vy+dy[k]
            if not (0<=nx<N and 0<=ny<N):
                continue
            if visited[nx][ny]:
                continue
            if opt==2:
                if graph[x][y]=='B':
                    if graph[nx][ny]!='B':
                        continue
                else:
                    if graph[nx][ny]=='B':
                        continue
            else:
                if graph[x][y]!=graph[nx][ny]:
                    continue
            visited[nx][ny]=True
            q.append((nx,ny))
            
        
            

visited=[[False]*N for _ in range(N)]
cnt=0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(1,i,j)
            cnt+=1

sys.stdout.write(str(cnt)+' ')

visited=[[False]*N for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(2,i,j)
            cnt+=1

sys.stdout.write(str(cnt)+'\n')