from collections import deque

N=int(input())

dx,dy=[1,0,-1,0],[0,1,0,-1]

graph=[list(map(int,input().split())) for _ in range(N)]

visited=[[False]*N for _ in range(N)]
res=[] # 각 섬에서 모은 최솟값들 중에서 진짜 최솟값을 가리기 위한 배열

def miniBfs(xx,yy): # 섬의 경계에 있는 칸들만 모아서 다른 섬과의 거리 재기위함
  miniVst=[[False]*N for _ in range(N)]
  qq=deque()
  qq.append((xx,yy,0))

  miniVst[xx][yy]=True
  while qq:
    vvx,vvy,cnt=qq.popleft() 
    for i in range(4):
      nx=vvx+dx[i]
      ny=vvy+dy[i]
      if not (0<=nx<N and 0<=ny<N):
        continue
      if (graph[nx][ny]==1 and visited[nx][ny]) or miniVst[nx][ny]:
        continue
      if graph[nx][ny]==1:
        return cnt+1
      qq.append((nx,ny,cnt+1))
      miniVst[nx][ny]=True 

  return 200



def bfs(x,y): 
  q=deque()
  q.append((x,y))

  visited[x][y]=True

  tempQ=deque()

  while q:
    vx,vy=q.popleft()

    for i in range(4):
      nx=vx+dx[i]
      ny=vy+dy[i]
      if not (0<=nx<N and 0<=ny<N):
        continue
      if visited[nx][ny]:
        continue
      if graph[nx][ny]==0:
        tempQ.append((vx,vy))
      else:
        q.append((nx,ny))
      visited[nx][ny]=True 

  ans=[]
  for tx,ty in tempQ:
    ans.append(miniBfs(tx,ty)) 
  if not ans:
    res.append(200)
  else:
    res.append(min(ans))
  return


for i in range(N):
  for j in range(N):
    if (not visited[i][j]) and graph[i][j]==1: 
      bfs(i,j)
print(min(res)-1)