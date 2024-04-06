import sys
sys.setrecursionlimit(10**6)
from collections import deque

N,M,K=map(int,sys.stdin.readline().split())
A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]


direc=1 # 처음에 동쪽으로 시작함

row=[4,1,3]
col=[2,1,5,6]
ans=0

def rotateDice(code, x):
  if code==1: # 시계 방향
    x+=1
    if x>4:
      x-=4
  elif code==2: # 반시계 방향
    x-=1
    if x<1:
      x+=4
  elif code==3: # 반대방향
    x+=2
    if x>4:
      x-=4
  return x

def rolltheDice(d): # d=1234중 하나, 해당 방향으로 굴린 다음의 주사위 모습을 리턴함
  if d==1:
    return [col[3],row[0],row[1]], [col[0],row[0],col[2],row[2]]
  elif d==2:
    return [row[0],col[0],row[2]], [col[3],col[0],col[1],col[2]]
  elif d==3:
    return [row[1],row[2],col[3]], [col[0],row[2],col[2],row[0]]
  elif d==4:
    return [row[0],col[2],row[2]], [col[1],col[2],col[3],col[0]]
  
def getScore(x,y,B):
  q=deque()
  q.append((x,y))
  dx,dy=[0,0,-1,1],[1,-1,0,0]

  visited=[[False]*M for _ in range(N)]
  visited[x][y]=True
  C=1

  while q:
    vx,vy=q.popleft()

    for i in range(4):
      ix,iy=dx[i]+vx,dy[i]+vy

      if not (0<=ix<N and 0<=iy<M):
        continue
      if A[ix][iy]!=B or visited[ix][iy]:
        continue
      visited[ix][iy]=True
      C+=1
      q.append((ix,iy))

  return C*B


def movetheDice(x,y,cnt):
  global ans, direc, row, col
  dxy=[[0,0],[0,1],[1,0],[0,-1],[-1,0]]
  nx,ny=dxy[direc][0]+x,dxy[direc][1]+y

  if not (0<=nx<N and 0<=ny<M):
    direc=rotateDice(3,direc)
    nx,ny=dxy[direc][0]+x,dxy[direc][1]+y 
  # 주사위가 이동 방향으로 한칸 굴러감

  row,col=rolltheDice(direc)
  # 굴러갔으니 주사위 좌표도 수정함

  B=A[nx][ny] # 주사위가 도착한 칸에 있는 정수

  ans+=getScore(nx,ny, B)
  # 점수 획득함
  
  if cnt+1==K:
    print(ans)
    return
  else:
    if col[3]>B:
      direc=rotateDice(1,direc)
    elif col[3]<B:
      direc=rotateDice(2,direc)
    movetheDice(nx,ny,cnt+1)

movetheDice(0,0,0)


