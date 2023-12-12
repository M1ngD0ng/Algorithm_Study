import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

dp=[0]*(N)
dp[0]=A[0] 
for i in range(1,N):
  temp=[]
  for j in range(i-1,-1,-1):
    if A[j]<A[i]:
      temp.append(dp[j])
    else:
      dp[i]=A[i]
  if temp:
    dp[i]=max(temp)+A[i]

print(max(dp))