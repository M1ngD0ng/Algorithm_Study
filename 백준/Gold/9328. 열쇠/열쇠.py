import sys
from collections import deque, defaultdict

T=int(sys.stdin.readline())
dx,dy=[1,-1,0,0],[0,0,1,-1]

def whatIs(x,y):
  if A[x][y]=='.':
    return 1
  elif A[x][y]=='*':
    return 2
  elif A[x][y]=='$':
    return 3
  else:
    if A[x][y].isupper(): # 대문자
      return 4
    else: # 소문자
      return 5
  
def checkOutside(x,y):
  global ans
  num=whatIs(x,y)
  if num==2:
    return
  if num==3:
    A[x][y]='.'
    ans+=1
  elif num==4:
    if A[x][y] in Key: # 대문자인데 마침 키가 있으면 열고 빈칸으로 만듦
      A[x][y]='.'
    else:
      alpha[A[x][y]].append((x,y))
      return
  elif num==5:
    up=A[x][y].upper()
    Key.add(up)
    A[x][y]='.'
    if alpha[up]:
      for a,b in alpha[up]:
        findKey(a,b)
  findKey(x,y) 


def findKey(x,y):
  global ans
  visited[x][y]=True
  q=deque()
  q.append((x,y))

  while q: 
    vx,vy=q.popleft()

    for k in range(4):
      nx=vx+dx[k]
      ny=vy+dy[k]

      if not (0<=nx<H and 0<=ny<W):
        continue
      if visited[nx][ny]:
        continue
      temp=whatIs(nx,ny)
      if temp ==2:
        continue
      if temp==3:
        ans+=1
        A[nx][ny]='.'
      elif temp==4:
        if A[nx][ny] in Key: # 대문자인데 마침 키가 있으면 열고 빈칸으로 만듦
          A[nx][ny]='.'
        else:
          alpha[A[nx][ny]].append((nx,ny))
          continue
      elif temp==5:
        up=A[nx][ny].upper()
        Key.add(up)
        A[nx][ny]='.'
        if alpha[up]:
          for na,nb in alpha[up]:
            A[na][nb]='.'
            q.append((na,nb))
      visited[nx][ny]=True
      q.append((nx,ny))
          
def bfs(x,y):
  global ans
  q=deque()
  q.append((x,y))
  visited[x][y]=True
  if A[x][y]=='$':
    ans+=1

  while q:
    vx,vy=q.popleft()

    for k in range(4):
      nx=vx+dx[k]
      ny=vy+dy[k]

      if not (0<=nx<H and 0<=ny<W):
        continue
      if visited[nx][ny]:
        continue
      if whatIs(nx,ny) in {1,3}:
        if A[nx][ny]=='$':
          ans+=1
          A[nx][ny]='.'
        q.append((nx,ny))
      visited[nx][ny]=True

for _ in range(T):
  H,W=map(int,sys.stdin.readline().split())
  A=[list(sys.stdin.readline().rstrip()) for _ in range(H)]

  Key=set(sys.stdin.readline().rstrip().upper())
  if '0' in Key:
    Key=set()
  alpha=defaultdict(list)
  outside=set()
  ans=0
  visited=[[False]*W for _ in range(H)]
  for i in range(H):
    if i in {0, H-1}: # 전체 확인
      for j in range(W):
        checkOutside(i,j)            
    else:
      for j in [0, W-1]: # 양 끝만 확인
        checkOutside(i,j)
 
  visited=[[False]*W for _ in range(H)]
  for i in range(H):
    if i in {0, H-1}: # 전체 확인
      for j in range(W):
        if whatIs(i,j) in {1,3}:
          bfs(i,j)        
    else:
      for j in [0, W-1]: # 양 끝만 확인
        if whatIs(i,j) in {1,3}:
          bfs(i,j)
  print(ans)