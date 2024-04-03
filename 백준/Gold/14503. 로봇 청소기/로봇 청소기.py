N,M=map(int,input().split())
r,c,d=map(int,input().split())

P=[ list(map(int,input().split())) for _ in range(N)]
cnt=0 # 청소한 칸의 개수

nd=0 # 현재 이동해야할 방향 1이면 앞, -1이면 뒤, 0이면 가만히

def func():
  global r,c,P,d,nd

  dx=[-1,0,1,0]
  dy=[0,1,0,-1]
  
  cnt2=0 # 주변의 청소할 수 없는 칸 개수
  for i in range(4):
    nx=r+dx[i]
    ny=c+dy[i]
    if nx>=0 and ny>=0 and nx<N and ny<M:
      if P[nx][ny]!=0: # 1 or 2면
        cnt2+=1
      else:
        continue
    else:
       cnt2+=1
  
  if cnt2<4: # 청소되지 않은 빈 칸이 있어서 반시계 방향으로 90도 회전함
    d=d-1
    if d<0:
      d+=4
    nd=1
  else:
    nd=-1
    
    
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while True:
  if P[r][c]==0:
    P[r][c]=2
    cnt+=1
  func()

  nx=dx[d]*nd+r
  ny=dy[d]*nd+c

  if nd==-1:
    if nx>=0 and ny>=0 and nx<N and ny<M and P[nx][ny]!=1:
      r=nx
      c=ny # 한 칸 후진함
      continue
    else:
      break
  elif nd==1:
    if nx>=0 and ny>=0 and nx<N and ny<M and P[nx][ny]==0:
      r=nx
      c=ny # 한 칸 전진함

print(cnt)
