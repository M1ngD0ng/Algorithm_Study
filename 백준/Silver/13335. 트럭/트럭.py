import sys
from collections import deque

N,W,L=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
q=deque()
for i in range(N):
  q.append((0,A[i])) 
del A

nq=[] # 다리 위에 있는 트럭들
time=0
curL=0
curW=0
while True:
  if not q and not nq:
    break
  if q:
    vW,vI=q.popleft() # 지금 대기열1번인것을 팝
    if (curL+vI)<=L: # 현재상태에서 올라갈 수 있는 무게인지 판별
      curL+=vI
      nq.append([vW+1,vI])
    else:
      q.appendleft((vW,vI)) # 못올라가면 다시 큐로 가라...

  temp=[]
  for i in range(len(nq)):
    if nq[i][0]==W:
      curL-=nq[i][1]
      temp.append([nq[i][0],nq[i][1]])
    else:
      nq[i][0]+=1
  for i,j in temp:
    nq.remove([i,j])
   
  time+=1

print(time+1)