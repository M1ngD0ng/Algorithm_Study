import sys
sys.setrecursionlimit(10**6)
from copy import deepcopy

A=[[[] for _ in range(4)] for _ in range(4)]

temp=[list(map(int,sys.stdin.readline().split())) for _ in range(4)]
for i in range(4):
  for j in range(0,7,2):
    A[i][j//2]=[temp[i][j],temp[i][j+1]]
del temp

direc={1:[-1,0],2:[-1,-1],3:[0,-1],4:[1,-1],5:[1,0],6:[1,1],7:[0,1],8:[-1,1]}


def rotateFish(x):
  x+=1
  if x>8:
    x-=8
  return x

def moveFish(A):
  for i in range(1,17):
    x,y=-1,-1
    for j in range(4):
      for k in range(4):
        if A[j][k][0]==i:
          x,y=j,k
          break
      if (x,y)!=(-1,-1):
        break
    if (x,y)==(-1,-1):
      continue
    
    Dir=A[x][y][1]
    
    while True:
      nx,ny=direc[Dir][0]+x,direc[Dir][1]+y

      if (not (0<=nx<4 and 0<=ny<4)) or A[nx][ny][0]==-1:
        Dir=rotateFish(Dir)
      elif A[nx][ny][0]==0:
        A[nx][ny]=[i,Dir]
        
        A[x][y]=[0,0]
        break
      else:
        A[x][y]=[A[nx][ny][0],A[nx][ny][1]]

        A[nx][ny]=[i,Dir]
        break

      if Dir==A[x][y][1]:
        break

def dfs(sx,sy,A,answer): 
  global ans
  answer+=A[sx][sy][0]
  sDir=A[sx][sy][1]
  A[sx][sy]=[-1,sDir]
  moveFish(A)
  
  for i in range(1,4):
    nx,ny=sx+direc[sDir][0]*i,sy+direc[sDir][1]*i

    if (not (0<=nx<4 and 0<=ny<4)):
      break
    elif A[nx][ny][0]==0:
      continue
    else:
      A[sx][sy]=[0,0]
      dfs(nx,ny,deepcopy(A),answer)
      A[sx][sy]=[-1,sDir]

  ans=max(ans,answer)
  

ans=0
dfs(0,0,A,0)
print(ans)