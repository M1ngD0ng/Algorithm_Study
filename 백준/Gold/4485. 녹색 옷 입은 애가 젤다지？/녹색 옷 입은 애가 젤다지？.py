import sys
import heapq

def dijstra():
  q=[]
  heapq.heappush(q,((0,0),graph[0][0]))
  distance=[[1e8]*N for _ in range(N)]
  distance[0][0]=graph[0][0]
  dx,dy=[0,1,0,-1],[1,0,-1,0]

  while q:
    now,dist=heapq.heappop(q)

    for i in range(4):
      nx=now[0]+dx[i]
      ny=now[1]+dy[i]

      if not (0<=nx<N and 0<=ny<N):
        continue
      if dist+graph[nx][ny]<distance[nx][ny]:
        distance[nx][ny]=dist+graph[nx][ny]
        heapq.heappush(q,((nx,ny),dist+graph[nx][ny]))

  return distance[N-1][N-1]


idx=0

while True:
  idx+=1
  N=int(sys.stdin.readline())
  if N==0:
    break
  graph=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
  sys.stdout.write('Problem '+str(idx)+': '+str(dijstra())+'\n') 