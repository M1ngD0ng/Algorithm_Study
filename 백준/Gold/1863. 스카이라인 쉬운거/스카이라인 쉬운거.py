import sys

N=int(sys.stdin.readline())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited=[False]*N

cnt=0
for i in range(N):
  if A[i][1]==0:
    visited[i]=True
    continue
  if visited[i]:
    continue
  cnt+=1
  visited[i]=True
  for j in range(i+1,N):
    if A[j][1]>A[i][1]:
      continue
    elif A[j][1]==A[i][1]:
      visited[j]=True
    else:
      break

print(cnt)