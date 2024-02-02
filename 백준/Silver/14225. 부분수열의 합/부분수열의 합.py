import sys
from itertools import combinations

N=int(sys.stdin.readline())
S=list(map(int,sys.stdin.readline().split()))


dp=[False]*(sum(S)+1)
for i in range(N):
  dp[S[i]]=True

ans=1e8
for i in range(2,N+1): 
  for da in list(combinations(S,i)):
    dp[sum(da)]=True


for i in range(1,len(dp)):
  if not dp[i]:
    print(i)
    sys.exit(0)
print(sum(S)+1)