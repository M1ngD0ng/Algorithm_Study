import sys
sys.setrecursionlimit(10**6)
N=int(sys.stdin.readline())
dp=[1,0,3,0]+[0]*27

if N<4:
  print(dp[N])
  sys.exit(0)
if N%2==1:
  print(0)
  sys.exit(0)


def recur(n):
  if n==0:
    return dp[0]
  if dp[n-2]==0:
    dp[n]=recur(n-2)*3
  else:
    dp[n]=dp[n-2]*3
  for i in range(4,n+1,2):
    if dp[n-i]==0:
      dp[n]+=(recur(n-i)*2)
    else:
      dp[n]+=dp[n-i]*2
  
  return dp[n]
      
      



print(recur(N))