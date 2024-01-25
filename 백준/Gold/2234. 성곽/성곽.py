import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

def findWall():
  num=[8,4,2,1]

  for j in range(N):
    temp=[False]*4 # [남,동,북,서]
    for k in range(4):
      if A[j]-num[k]>=0:
        temp[k]=True
        A[j]-=num[k]
    graph[i].append(temp)
    
  

graph=[[] for _ in range(M)]
dp=[[0]*N for _ in range(M)]
area=dict() # 방을 탐색할때마다 그 방 넘버를 dp에 적어두고 나오면서 마지막에 넓이를 이 배열에 추가함


for i in range(M):
  A=list(map(int,sys.stdin.readline().split()))
  findWall()
  


dx,dy=[1,0,-1,0],[0,1,0,-1]
def bfs(x,y,cnt):
  q=deque()
  q.append((x,y))
  visited=[[False]*N for _ in range(N)]
  visited[x][y]=True
  roomSize=1
  
  dp[x][y]=cnt

  while q:
    vx,vy=q.popleft()

    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]

      if not (0<=nx<M and 0<=ny<N):
        continue
      if graph[vx][vy][i]: # 가려는 방향으로 벽이 있을 때
        continue
      if visited[nx][ny]:
        continue
      visited[nx][ny]=True
      roomSize+=1
      dp[nx][ny]=cnt
      q.append((nx,ny))
  area[cnt]=roomSize


cnt=0
for i in range(M):
  for j in range(N):
    if dp[i][j]==0:
      cnt+=1
      bfs(i,j,cnt)

ans1=len(area)
print(ans1)
print(max(area.values()))

dp2=[[False]*(ans1+1) for _ in range(ans1+1)]
ans3=0
for i in range(M):
  for j in range(N):
    for k in range(4):
      nx=i+dx[k]
      ny=j+dy[k]
      if not (0<=nx<M and 0<=ny<N):
        continue
      if dp[i][j]==dp[nx][ny]:
        continue
      if dp2[dp[i][j]][dp[nx][ny]]:
        continue
      dp2[dp[i][j]][dp[nx][ny]]=True
      dp2[dp[nx][ny]][dp[i][j]]=True
      ans3=max(ans3,area[dp[i][j]]+area[dp[nx][ny]])
      
      

print(ans3)