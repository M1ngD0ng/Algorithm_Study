import sys

N=int(sys.stdin.readline())
d=dict()
for i in range(1,N+1):
  a,b=map(int,sys.stdin.readline().split())
  d[i]=[a,b]
  
dp=[0]*(N+2)

for i in range(N,0,-1):
  if i+d[i][0]>N+1: # N일 이후에 종료되는 상담
    dp[i]=dp[i+1]
  else:
    dp[i]=max(d[i][1]+dp[i+d[i][0]],dp[i+1])

print(max(dp))    