import sys
from collections import deque

def bfs():
  global isPossible

  q=deque()
  visited=[False]*N
  for i in range(N):
    temp=abs(B[0][0]-A[i][0])+abs(B[0][1]-A[i][1]) # 출발지에서 각 편의점에 한번에 갈수있나?
    if temp<=1050:
      q.append((i))

  while q:
    idx=q.popleft()

    temp=abs(B[1][0]-A[idx][0])+abs(B[1][1]-A[idx][1]) # 도착지까지 갈 수 있나?
    if temp<=1050:
      isPossible=True
      return
    if idx==N-1:
      continue
      
    else:
      for i in range(N):
        if i==idx:
          continue

        if visited[i]:
          continue 

        dist1=abs(A[idx][0]-A[i][0])+abs(A[idx][1]-A[i][1]) # 다음 편의점까지 갈수있나?

        if dist1<=1050:
          visited[i]=True
          q.append((i))
          


T=int(sys.stdin.readline())
for _ in range(T):
  N=int(sys.stdin.readline())
  B=[]
  B.append(list(map(int,sys.stdin.readline().split())))

  A=[]

  for _ in range(N):
    x,y=map(int,sys.stdin.readline().split())
    A.append([x,y])
  B.append(list(map(int,sys.stdin.readline().split())))

  if abs(B[0][0]-B[1][0])+abs(B[0][1]-B[1][1])<=1000:
    print('happy')
    continue
  isPossible=False
  bfs()

  if isPossible:
    print('happy')
  else:
    print('sad')