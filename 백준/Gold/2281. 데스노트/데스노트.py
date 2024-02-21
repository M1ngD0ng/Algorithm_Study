import sys
sys.setrecursionlimit(10**6)
N,M=map(int,sys.stdin.readline().split())
A=[int(sys.stdin.readline()) for _ in range(N)]

dp=[1e9]*N
dp[-1]=0

def cal(idx):
  global dp

  if dp[idx]<1e9:
    return dp[idx]
  
  blank=M-A[idx]
  next=idx+1

  while blank>=0:
    if next==N:
      dp[idx]=0
      break
    
    dp[idx]=min(dp[idx],blank**2+cal(next))
    blank-=A[next]+1
    next+=1

  return dp[idx]


print(cal(0))