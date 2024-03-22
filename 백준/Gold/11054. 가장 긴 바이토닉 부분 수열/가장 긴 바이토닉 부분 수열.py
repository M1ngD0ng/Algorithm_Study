import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

dp1=[1]*N
dp2=[1]*N

for i in range(1,N):
  for j in range(i):
    if A[j]<A[i]:
      dp1[i]=max(dp1[i],dp1[j]+1)

for i in range(N-2,-1,-1):
  for j in range(i+1,N):
    if A[j]<A[i]:
      dp2[i]=max(dp2[i],dp2[j]+1)

ans=0
for i in range(N):
  ans=max(dp1[i]+dp2[i],ans) 
print(ans-1)