import sys

N,K=map(int,sys.stdin.readline().split())
A=list(sys.stdin.readline().rstrip())

dp=[False]*N
for i in range(N):
  if A[i]=='P':
    dp[i]=True
cnt=0
dx=[]
for i in range(1,K+1):
  dx.append(i)
  dx.append(-i)
dx.sort() 

for i in range(N):
  if A[i]=='P':
    for j in range(2*K):
      nx=i+dx[j]
      if not 0<=nx<N:
        continue
      if A[nx]=='H' and dp[nx]==False:
        dp[nx]=True
        cnt+=1 
        break

print(cnt)