import sys
from collections import deque

R,C=map(int,sys.stdin.readline().split())

A=[list(sys.stdin.readline().rstrip()) for _ in range(R)]

N=int(sys.stdin.readline())
H=list(map(int,sys.stdin.readline().split()))

dx,dy=[0,0,-1,1],[1,-1,0,0]

def bfs(x,y):
  q=deque()
  q.append((x,y))
  visited[x][y]=True
  dp[x][y]=chk

  while q:
    vx,vy=q.popleft()

    for k in range(4):
      nx=vx+dx[k]
      ny=vy+dy[k]

      if not (0<=nx<R and 0<=ny<C):
        continue
      if visited[nx][ny]:
        continue

      if A[nx][ny]=='x':
        dp[nx][ny]=chk # 한 클러스터 당 하나의 번호를 가짐
        visited[nx][ny]=True
        q.append((nx,ny))
      

def gravity(index):
  temp=[] 
  for j in range(R):
    for k in range(C):
      if dp[j][k]==index: 
        temp.append((j,k))

  isPossible=True 

  for tx,ty in temp:
    if tx+1==R:
      isPossible=False
      break
    if A[tx+1][ty]=='x':
      if dp[tx+1][ty]!=index:
        isPossible=False
        break
  if not isPossible: 
    return
  
  for i in range(len(temp)-1,-1,-1):
    x,y=temp[i][0],temp[i][1]

    dp[x+1][y]=index
    dp[x][y]=0
    A[x+1][y]='x'
    A[x][y]='.'
  gravity(index)




for n in range(N):
  visited=[[False]*C for _ in range(R)]
  dp=[[0]*C for _ in range(R)]
  chk=1

  for i in range(R):
    for j in range(C):
      if A[i][j]=='x' and not visited[i][j]:
        bfs(i,j)
        chk+=1 
  
  mx,my=R-H[n],-1 # 깨지는 미네랄의 좌표
  if n%2==0: # 왼쪽에서 쏨
    for i in range(C):
      if A[mx][i]=='x':
        my=i
        break
  else: # 오른쪽에서 쏨
    for i in range(C-1,-1,-1):
      if A[mx][i]=='x':
        my=i
        break

  if my==-1: # 아무것도 안쐈으면 continue
    continue

  chkNum=dp[mx][my]
  A[mx][my]='.' # 쏴서 사라졌기 때문에 빈 칸으로 바꿔줌

  for i in range(R):
    for j in range(C):
      if dp[i][j]==chkNum:
        dp[i][j]=0
      
  near=[]
  visited=[[False]*C for _ in range(R)]
  visited[mx][my]=True
  for i in range(4):
    vnx=mx+dx[i]
    vny=my+dy[i]

    if not (0<=vnx<R and 0<=vny<C):
      continue
    if A[vnx][vny]=='x':
      near.append((vnx,vny))
      if not visited[vnx][vny]:
        bfs(vnx,vny)
        chk+=1

  if not near: # 주변에 이 칸을 포함한 클러스터가 없기 때문에 이 미네랄만 파괴하고 continue
    continue 

  if len(near)==1:
    gravity(dp[near[0][0]][near[0][1]])
  else:
    tempNum=set()
    for i in range(1,len(near)):
      if near[i-1][0]!=near[i][0] or near[i-1][1]!=near[i][1]:
        tempNum.add(dp[near[i-1][0]][near[i-1][1]])
        tempNum.add(dp[near[i][0]][near[i][1]])

    for i in list(tempNum):
      gravity(i)

for i in range(R):
  for j in range(C):
    sys.stdout.write(str(A[i][j]))
  print()