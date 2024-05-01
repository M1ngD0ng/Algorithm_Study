import sys
from collections import deque
N=int(sys.stdin.readline())
K=int(sys.stdin.readline())

Body=deque([[0,0]])
cnt=0

S=[[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
  a,b=map(int,sys.stdin.readline().split())
  S[a-1][b-1]=1 # 사과의 위치 표시

L=int(sys.stdin.readline())
Dir=[-1 for _ in range(10000)]
for _ in range(L):
  M,C=sys.stdin.readline().split()
  Dir[int(M)]=C

curD=1 # 현재 방향
x,y=0,0 # 현재 위치

dy=[0,1,0,-1]
dx=[-1,0,1,0]

time=0
while True:

  if curD>=4:
    curD-=4
 # print('지금은 ',Dir[time], curD, time)
  
  nx=x+dx[curD] # 머리를 다음칸에 위치시킴
  ny=y+dy[curD]
  Body.append([nx,ny]) # 머리를 Body에 붙임
  

  if nx>=0 and nx<N and ny>=0 and ny<N:
    if S[nx][ny]==1: # 사과임
      S[nx][ny]=0
    #  print(1)
      x=nx
      y=ny
      cnt+=1
    elif Body.count([nx,ny])>1: # 꼬리랑 부딪힘
     # print(3)
      cnt+=1
      break
    else:
      Body.popleft()
    #  print(2)
      x=nx
      y=ny
      cnt+=1
  else: # 벽에 부딪힘
  #  print(4)
    cnt+=1
    break
 # print(Body)

  
  time+=1
  if Dir[time]==-1:
    continue
  elif Dir[time]=='L':
    curD+=3
  else:
    curD+=1

print(cnt)