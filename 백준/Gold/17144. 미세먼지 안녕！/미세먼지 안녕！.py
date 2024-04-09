import sys

R,C,T=map(int,sys.stdin.readline().split())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(R)]
cleaner=[-1,-1]

for i in range(R):
  if A[i][0]==-1:
    cleaner=[i,i+1]
    break

def doClean():
  for a in range(cleaner[0]-1,0,-1):
    A[a][0]=A[a-1][0]
  for a in range(cleaner[1]+1,R-1):
    A[a][0]=A[a+1][0]

  for a in range(C-1):
    A[0][a]=A[0][a+1]
    A[R-1][a]=A[R-1][a+1]

  for a in range(cleaner[0]):
    A[a][C-1]=A[a+1][C-1]
  for a in range(R-1,cleaner[1],-1):
    A[a][C-1]=A[a-1][C-1]

  for a in range(C-1,0,-1):
    A[cleaner[0]][a]=A[cleaner[0]][a-1]
    A[cleaner[1]][a]=A[cleaner[1]][a-1]

  A[cleaner[0]][1]=0
  A[cleaner[1]][1]=0
  

def combineDust(dust):
  for r in range(R):
    for c in range(C):
      A[r][c]+=dust[r][c]  
  doClean()

def calDust():
  dust=[[0]*C for _ in range(R)]
  dx,dy=[0,0,-1,1],[1,-1,0,0]

  for x in range(R):
    for y in range(C):
      if A[x][y]>0:
        cnt=0
        
        for z in range(4):
          nx,ny=x+dx[z],y+dy[z]

          if not (0<=nx<R and 0<=ny<C):
            continue
          if ny==0 and nx in cleaner:
            continue # 공기청정기가 있는 곳
          cnt+=1
          dust[nx][ny]+=int(A[x][y]/5)

        A[x][y]=A[x][y]-int(A[x][y]/5)*cnt

  combineDust(dust)

for _ in range(T):
  calDust()

ans=0
for i in range(R):
  for j in range(C):
    if A[i][j]!=-1:
      ans+=A[i][j]

print(ans)