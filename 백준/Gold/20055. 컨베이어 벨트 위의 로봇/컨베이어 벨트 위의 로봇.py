import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
B=[False]*2*N

upIdx=0
downIdx=N-1
cnt=0 
while True: 
  if A.count(0)>=K: 
    break
  cnt+=1  
  if upIdx==0:
    upIdx=2*N-1
  else:
    upIdx-=1
  if downIdx==0:
    downIdx=2*N-1
  else:
    downIdx-=1 # 벨트 한칸 이동(1단계) 

  B[downIdx]=False # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다
  t=downIdx
  while True:
    if t==upIdx:
      break
    t-=1
    if t==-1:
      t=2*N-1 
    if B[t]==False:
      continue
    else:
      next=t+1
      if next==2*N:
        next=0
      if A[next]>=1:
        if B[next]==False:
          B[next]=True
          B[t]=False
          A[next]-=1
          if next==downIdx:
            B[next]=False

      else:
        continue 
  if A[upIdx]>=1:
    B[upIdx]=True
    A[upIdx]-=1  
print(cnt)