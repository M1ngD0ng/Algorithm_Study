import sys

N=int(sys.stdin.readline())
A=[ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
_key=[[-1,0,1],[-2,-1,2],[-1,-1,7],[-1,-2,10],[0,-3,5],[1,-2,10],[1,-1,7],[1,0,1],[2,-1,2]]

def rotate():
  B=[[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      B[j][N-1-i]=A[i][j]

  return B

xX,xY=N//2, N//2 # 시작점, 현재위치

ans=0 
for i in range(1,N):
  cnt=2
  if i==N-1:
    cnt=3
  for j in range(cnt):
    for k in range(i): 
      sand=A[xX][xY-1]
      if sand==0:
        xY-=1
        continue 

      for a,b,c in _key:
        nx,ny=xX+a,xY+b
        temp2=int((A[xX][xY-1]/100)*c)
        
        if not (0<=nx<N and 0<=ny<N):
          ans+=temp2
        else:
          A[nx][ny]+=temp2
        sand-=temp2
      
      if (0<=(xY-2)<N):
        A[xX][xY-2]+=sand
      else:
        ans+=sand
      A[xX][xY-1]=0
      xY-=1 
    A=rotate() 
    xX,xY=xY,N-1-xX
       
print(ans)