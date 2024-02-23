import sys
from collections import defaultdict,deque

X=int(sys.stdin.readline())

M,N=map(int,sys.stdin.readline().split())
A=deque(int(sys.stdin.readline()) for _ in range(M))
B=deque(int(sys.stdin.readline()) for _ in range(N)) 

dp1=defaultdict(int)
dp2=defaultdict(int)

def cal(d,arr,L):
  for _ in range(L):
    temp=0
    for i in range(L-1):
      temp+=arr[i]
      if temp>X:
        break
      else:
        d[temp]+=1
    arr.append(arr.popleft())
    
  d[0]=1
  if sum(arr)<=X:
    d[sum(arr)]=1

cal(dp1,A,M)
cal(dp2,B,N)

ans=0
for i in dp1.keys():
  if X-i in dp2.keys():
    ans+=(dp1[i]*dp2[X-i])

print(ans)