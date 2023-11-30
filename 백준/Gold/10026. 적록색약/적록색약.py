import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]

for i in range(N):
	graph[i] = list(map(str, sys.stdin.readline().rstrip()))

ans1=0
ans2=0

def inRange(nx,ny):
  return nx>=0 and nx<N and ny>=0 and ny<N

def dfs(x,y):
  global visited
  visited[x][y]=True
  dx=[0,1,0,-1]
  dy=[1,0,-1,0]

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    
    if not inRange(nx,ny) or visited[nx][ny]==True:
      continue
    else:
      if graph[x][y]==graph[nx][ny]:
        dfs(nx,ny)


def cal():
  global visited
  x,y=0,0
  ans=0
  while True:
    dfs(x,y)
    ans+=1
    for i in range(N):
      if False in visited[i]:
        j=visited[i].index(False)
        nx,ny=i,j
        break
    if x!=nx or y!=ny:
      x,y=nx,ny
      continue
    else:
      break
  return ans

visited=[[False for _ in range(N)] for _ in range(N)]
ans1=cal()

for i in range(N):
  if 'G' in graph[i]:
    for j in range(N):
      if graph[i][j]=='G':
        graph[i][j]='R'
visited=[[False for _ in range(N)] for _ in range(N)]
ans2=cal()
print(ans1,ans2)