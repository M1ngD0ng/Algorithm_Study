import sys

N,L=map(int,sys.stdin.readline().split())
A=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def test(code,idx):
  visited=[False]*N
  if code==1: # 가로줄
    for i in range(1,N):
      if A[idx][i]==A[idx][i-1]:
        continue
      if A[idx][i]<A[idx][i-1]:
        if A[idx][i-1]-A[idx][i]>1:
          return 0
        else:
          for j in range(L):
            ny=i+j
            if not (0<=ny<N):
              return 0
            if A[idx][ny]!=A[idx][i]:
              return 0
            visited[ny]=True
          i+=L
      else:
        if A[idx][i]-A[idx][i-1]>1:
          return 0
        else:
          for j in range(i-L,i):
            if not (0<=j<N):
              return 0
            if visited[j]:
              return 0
            if A[idx][j]!=(A[idx][i]-1):
              return 0
            visited[j]=True
  else: # 세로줄
    for i in range(1,N):
      if A[i][idx]==A[i-1][idx]:
        continue
      if A[i][idx]<A[i-1][idx]:
        if A[i-1][idx]-A[i][idx]>1:
          return 0
        else:
          for j in range(L):
            nx=i+j
            if not (0<=nx<N):
              return 0
            if A[nx][idx]!=A[i][idx]:
              return 0
            visited[nx]=True
          i+=L
      else:
        if A[i][idx]-A[i-1][idx]>1:
          return 0
        else:
          for j in range(i-L,i):
            if not (0<=j<N):
              return 0
            if visited[j]:
              return 0
            if A[j][idx]!=(A[i][idx]-1):
              return 0
            visited[j]=True

  return 1


ans=0
for idx in range(N):
  ans+=test(1,idx)
  ans+=test(2,idx)

print(ans)