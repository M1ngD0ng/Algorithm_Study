import sys
N=int(sys.stdin.readline())

graph=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

visited=[[False]*N for _ in range(N)]
queue=[[0,0]]
dx, dy=[0,1],[1,0]
while queue :
  x,y=queue.pop(0) 
  c=graph[x][y]

  if c==-1:
    sys.stdout.write('HaruHaru')
    exit(0)
  for i in range(2):
    nx=x+c*dx[i]
    ny=y+c*dy[i]
    if nx>=0 and nx<N and ny>=0 and ny<N and not visited[nx][ny]: 
      visited[nx][ny]=1
      queue.append([nx,ny])
    
sys.stdout.write('Hing')